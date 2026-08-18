#!/usr/bin/env python3
"""33m2 REST 계약(api-full.json + dto.json + req-dto.json) → OpenAPI 3.1 YAML 사이드카."""
import json, re, sys

BASE = "/Users/dusan/jamkkan/reference/_shared/captures"
api = json.load(open(f"{BASE}/33m2.api-full.json"))
resp_dtos = json.load(open(f"{BASE}/33m2.dto.json"))    # 179 응답 DTO
req_dtos  = json.load(open(f"{BASE}/33m2.req-dto.json")) # 49 요청 DTO

# 모든 DTO 병합 (요청/응답 공용 스키마 컴포넌트)
all_dtos = {}
all_dtos.update(resp_dtos)
all_dtos.update(req_dtos)

# DTO 목록에 없지만 계약에 등장하는 보조 타입(정직한 근사 정의)
# ❗ 필드명을 지어내지 않음 — 단순 래퍼/enum/자유객체로만 표기
EXTRA_SCHEMAS = {
    "SimpleStringResult":  {"type": "object", "description": "단순 문자열 결과 래퍼 (필드 구조 미관찰)"},
    "SimpleBooleanResult": {"type": "object", "description": "단순 불리언 결과 래퍼 (필드 구조 미관찰)"},
    "EmailVerifyResult":   {"type": "object", "description": "이메일 인증 결과 (필드 구조 미관찰)"},
    "JsonObject":          {"type": "object", "additionalProperties": True, "description": "Gson JsonObject — 자유 형식"},
    "ResponseMessageType": {"type": "string", "description": "enum — 값은 33m2/enums.md 참조"},
    "SurveyOptionType":    {"type": "string", "description": "enum — 값은 33m2/enums.md 참조"},
    "SurveyQuestionType":  {"type": "string", "description": "enum — 값은 33m2/enums.md 참조"},
}

PRIMITIVE = {
    "String": ("string", None, False),
    "int":    ("integer", "int32", False),
    "Integer":("integer", "int32", True),   # 박스형 → nullable
    "long":   ("integer", "int64", False),
    "Long":   ("integer", "int64", True),
    "boolean":("boolean", None, False),
    "Boolean":("boolean", None, True),
    "double": ("number", "double", False),
    "Double": ("number", "double", True),
    "float":  ("number", "float", False),
    "Float":  ("number", "float", True),
}

def is_dto(name): return name in all_dtos or name in EXTRA_SCHEMAS

def type_to_schema(t):
    """Java 타입 문자열 → OpenAPI 3.1 스키마 dict."""
    t = t.strip()
    # 컬렉션: "List X" / "ArrayList X" / "List<X>" / "ArrayList<X>"
    m = re.match(r'^(?:List|ArrayList|Set|Collection)[\s<]+(.+?)>?$', t)
    if m:
        inner = m.group(1).strip()
        return {"type": "array", "items": type_to_schema(inner)}
    # Map (드묾)
    if t.startswith("Map"):
        return {"type": "object", "additionalProperties": True}
    if t in PRIMITIVE:
        ptype, fmt, nullable = PRIMITIVE[t]
        # OpenAPI 3.1: nullable은 type 유니온으로 표기
        s = {"type": [ptype, "null"] if nullable else ptype}
        if fmt: s["format"] = fmt
        return s
    if is_dto(t):
        return {"$ref": f"#/components/schemas/{t}"}
    # 미상 참조 타입 → object (실패 안전)
    return {"type": "object", "description": f"unresolved type: {t}"}

# --- components/schemas ---
schemas = {}
for name, fields in all_dtos.items():
    props = {}
    for fname, ftype in fields:
        props[fname] = type_to_schema(ftype)
    schemas[name] = {"type": "object", "properties": props}
schemas.update(EXTRA_SCHEMAS)

# resp 값이 DTO가 아닌 경우 처리: "v"=void(204), 원시형 래퍼 등
def resp_schema(resp):
    if resp in (None, "", "v", "void", "Void", "Unit"):
        return None  # 204
    if resp in PRIMITIVE:
        return type_to_schema(resp)
    m = re.match(r'^(?:List|ArrayList|Set)[\s<]+(.+?)>?$', resp.strip())
    if m:
        return type_to_schema(resp)
    if is_dto(resp):
        return {"$ref": f"#/components/schemas/{resp}"}
    # 미등록 응답 타입 → object
    return {"type": "object", "description": f"unresolved response type: {resp}"}

# --- 오버로드 병합: 같은 (verb,path)는 쿼리 파라미터 합집합으로 통합 ---
merged = {}
for e in api:
    key = (e["verb"], e["path"])
    if key not in merged:
        merged[key] = json.loads(json.dumps(e))  # deep copy
    else:
        m = merged[key]
        have = {q[1] for q in m["query"]}
        for q in e["query"]:
            if q[1] not in have:
                m["query"].append(q); have.add(q[1])
        # 응답 타입이 다르면 대체 응답으로 메모
        if e["resp"] != m["resp"]:
            m.setdefault("_alt_resp", []).append(e["resp"])

# --- paths ---
paths = {}
for e in merged.values():
    verb = e["verb"].lower()
    path = e["path"]
    op = {}
    # tag: 경로 첫 세그먼트 계열 (/v1/guest/... → guest)
    seg = [s for s in path.split("/") if s and not s.startswith("{")]
    tag = seg[1] if len(seg) > 1 and seg[0] == "v1" else (seg[0] if seg else "misc")
    op["tags"] = [tag]
    op["operationId"] = f"{verb}_" + re.sub(r'[^a-zA-Z0-9]+', '_', path).strip('_')
    params = []
    for kind, pname, ptype in e.get("path_params", []):
        params.append({
            "name": pname, "in": "path", "required": True,
            "schema": type_to_schema(ptype),
        })
    for kind, pname, ptype in e.get("query", []):
        sch = type_to_schema(ptype)
        # 박스형(널 허용)=선택, 원시형=필수 추정
        t = sch.get("type")
        required = not (isinstance(t, list) and "null" in t)
        params.append({
            "name": pname, "in": "query", "required": required,
            "schema": sch,
        })
    if params:
        op["parameters"] = params
    body = e.get("body")
    if body:
        op["requestBody"] = {
            "required": True,
            "content": {"application/json": {"schema": type_to_schema(body)}},
        }
    rs = resp_schema(e.get("resp"))
    if rs is None:
        op["responses"] = {"204": {"description": "No Content"}}
    else:
        desc = "OK — 33m2 성공 엔벨로프 {code:'SCSS_001', data:<schema>}"
        if e.get("_alt_resp"):
            desc += f" (대체 응답 타입 관찰됨: {', '.join(e['_alt_resp'])})"
        op["responses"] = {"200": {
            "description": desc,
            "content": {"application/json": {"schema": rs}},
        }}
    op["responses"]["4XX"] = {"$ref": "#/components/responses/Error"}
    if verb in paths.get(path, {}):
        print(f"  ⚠ 중복 (path,verb): {verb.upper()} {path} — 기존 것 유지", file=sys.stderr)
    paths.setdefault(path, {})[verb] = op

doc = {
    "openapi": "3.1.0",
    "info": {
        "title": "33m2 REST API (역설계 사이드카)",
        "version": "0.1.0-reverse-engineered",
        "description": (
            "33m2 Retrofit 인터페이스에서 역추출한 180 메서드 계약. "
            "성공 응답은 {code:'SCSS_001', data:<schema>} 엔벨로프로 감싸짐 "
            "(여기 schema는 data 부분). 에러는 HTTP 400 + {code, message:{type,content}}. "
            "박스형 타입(Integer/Long/Boolean/Double)은 nullable=true로 표기(추론). "
            "출처: _shared/captures/33m2.api-full.json + dto.json + req-dto.json. "
            "정본은 33m2/api-contract.md."
        ),
    },
    "servers": [{"url": "https://web.33m2.co.kr", "description": "관찰된 호스트 (실제 API 게이트웨이는 별도 추정)"}],
    "tags": sorted({p[list(p.keys())[0]]["tags"][0] for p in paths.values()}),
    "paths": dict(sorted(paths.items())),
    "components": {
        "schemas": dict(sorted(schemas.items())),
        "responses": {
            "Error": {
                "description": "에러 엔벨로프 (HTTP 400)",
                "content": {"application/json": {"schema": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "example": "ERR_XXX_000"},
                        "message": {"type": "object", "properties": {
                            "type": {"type": "string"},
                            "content": {"type": "string"},
                        }},
                        "data": {"type": "object", "nullable": True},
                    },
                }}},
            }
        },
    },
}
# tags를 [{name:...}] 형식으로
doc["tags"] = [{"name": t} for t in doc["tags"]]

# ---------------- 최소 YAML 직렬화기 ----------------
def needs_quote(s):
    if s == "": return True
    if re.search(r'[:#\{\}\[\],&\*!\|>%@`"\']', s): return True
    if s[0] in "-?" or s.strip() != s: return True
    if s.lower() in ("true","false","null","yes","no","on","off","~"): return True
    if re.match(r'^[+-]?\d', s): return True
    return False

def yscalar(v):
    if v is True: return "true"
    if v is False: return "false"
    if v is None: return "null"
    if isinstance(v, (int, float)): return str(v)
    s = str(v)
    if needs_quote(s):
        return '"' + s.replace('\\','\\\\').replace('"','\\"') + '"'
    return s

def dump(v, indent=0):
    sp = "  " * indent
    out = []
    if isinstance(v, dict):
        if not v: return sp + "{}\n"
        for k, val in v.items():
            ks = yscalar(str(k))
            if isinstance(val, (dict, list)) and val:
                out.append(f"{sp}{ks}:\n")
                out.append(dump(val, indent + 1))
            elif isinstance(val, (dict, list)):
                out.append(f"{sp}{ks}: {'{}' if isinstance(val,dict) else '[]'}\n")
            else:
                out.append(f"{sp}{ks}: {yscalar(val)}\n")
    elif isinstance(v, list):
        if not v: return sp + "[]\n"
        for item in v:
            if isinstance(item, (dict, list)) and item:
                inner = dump(item, indent + 1)
                # 첫 줄에 '- ' 붙이기
                first, *rest = inner.split("\n")
                stripped = first[len(sp)+2:] if first.startswith(sp) else first.strip()
                out.append(f"{sp}- {first.strip()}\n")
                for r in rest:
                    if r: out.append(r + "\n")
            else:
                out.append(f"{sp}- {yscalar(item)}\n")
    else:
        out.append(f"{sp}{yscalar(v)}\n")
    return "".join(out)

yaml_text = dump(doc)
out_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/openapi.yaml"
open(out_path, "w", encoding="utf-8").write(yaml_text)
print(f"written {out_path}: {len(yaml_text)} bytes, "
      f"{len(paths)} paths, {sum(len(v) for v in paths.values())} operations, "
      f"{len(schemas)} schemas")
