# 역설계 명세 저장소

새 서비스(중장기 임대 + 숙박 예약) 개발을 위해 **33m2**와 **Airbnb**를 역설계한 명세 모음.
Claude Code가 이 문서들을 입력으로 새 서비스를 구현하는 것이 최종 목적입니다.

👉 **먼저 [`CLAUDE.md`](CLAUDE.md)를 읽으세요** — 사용법·ID 체계·신뢰도 표기·금지사항.

## 진행 상황

| # | 작업 | 상태 |
|---|---|---|
| 1 | 33m2 게스트(임차인) 모드 | ✅ 완료 |
| 2 | 33m2 임대인 모드 | ✅ 완료 |
| 3 | Airbnb 게스트 모드 | ✅ 완료 |
| 4 | Airbnb 호스트 모드 | 🟢 GraphQL 오퍼레이션·화면으로 클론 레벨 (실화면 일부 제약) |
| 5 | 두 서비스 비교 분석 | ✅ 완료 |
| 6 | Claude Code용 명세 세트 | ✅ 완료 |
| — | 새 서비스 명세 | ⬜ 방향성 확정 후 |

## 문서

```
CLAUDE.md                        ← 사용법 · ID 체계 · 확정 수치 · 금지사항
_synthesis/
  GAP-ANALYSIS.md                완성도 감사 + 보완 계획 + 실행 결과
  comparison.md                  두 서비스 대조 + 강약점 + 가져올것/버릴것/새로만들것
  permissions.md                 권한 모델 (PERM-01~08)
  responsive-web.md              ★ 웹 반응형 (데스크톱↔모바일, UA쌍 실측)
  state-machines.md              ★ 상태머신 mermaid (계약 2축 · 예약 라이프사이클)
  mobile-apps.md                 ★ 안드로이드 앱 역설계 (33m2 · Airbnb)
  CLONE-READINESS.md             ★ 클론 구현 가능성 검증
  api-observed.md                API 명세 · 에러 엔벨로프 · 검색 계약
33m2/
  api-contract.md                ★★ API 계약 180메서드 (verb·path·body·resp)
  openapi.yaml                   ★ OpenAPI 3.1 사이드카 (자동생성, 161path/178op/235schema)
  api-endpoints.md               경로 카탈로그 159개
  api.md                         API 규약·의미
  data-model.md                  ★ 응답 DTO 179클래스/1,045필드
  ARCHITECTURE.md                기술 스택 · API 표면 · 도메인 어휘
  faq.md                         FAQ 전문 40건 (비즈니스 규칙)
  DOMAIN.md                      ★ 계약 도메인 — 상태머신 · 서브플로우 · 규칙
  auth-and-account.md            인증 · 계정 · 본인인증 · 접근 경계
  design-system.md               타이포 22종 · 컬러 73종 · 브레이크포인트
  enums.md                       Enum 카탈로그 52그룹 + 에러코드 103개
  zod-schemas.md                 클라이언트 Zod 스키마 44종 / 463필드
  i18n-reference.md              전체 UI 문구 79 네임스페이스 / 1,876키
  guest/
    screens.md                   화면 인벤토리 (라우트 17종, SCR-G01~17)
    flows.md                     유저 플로우 · 요금 산식 · 환불 정책
    entities.md                  Room 엔티티 · Host · ReviewTag · ListItem
  host/
    screens-and-model.md         호스트 화면 · 등록 위저드 5단계 · 정산 · 수수료 역산
airbnb/
  graphql-api.md                 ★★ GraphQL API 1,363 오퍼레이션 (Q751·M612)
  data-model.md                  ★ GraphQL 타입·Input 566·enum
  entity-schemas.md              ★ 응답 필드 스키마 (Listing198·Search95·BookIt119)
  flows-and-screens.md           ★ 예약·리뷰·메시징 플로우 · 화면 1,756
  design-system.md               DLS 토큰 — 팔레트 349 · 타이포 104 · CSS변수 1,615
  guest/
    screens-and-api.md           GraphQL 아키텍처 · 검색 · PDP · 여행/메시지/계정
    listing-entity.md            ★ node.pdpPresentation 27필드 (Room 대응)
    pdp-sections.md              PDP 28섹션 스키마
    search-filters.md            검색 필터 카탈로그 112개 파라미터 매핑
    checkout.md                  ★ stayCheckout — 결제·요금·식별자 모델
  host/
    listing-wizard.md            등록 위저드 16단계 중 1~7 · 접근 제약
_shared/captures/                기계 판독용 원본 JSON + 모바일 UI 덤프
  33m2.i18n.ko.json · 33m2.room.4684.json · 33m2.design-tokens.json
  airbnb.pdp.sections.json · airbnb.search.json · airbnb.design-tokens.json
  airbnb.graphql-operations.txt(1,363) · airbnb.graphql-inputs.txt(566)
  mobile/  (Android uiautomator XML 20+ · 스크린샷)
```

## 방법론

UI 관찰만으로는 필드명·타입·enum을 알 수 없으므로,
**클라이언트가 실제로 받는 서버 데이터를 직접 추출**했습니다.

| 서비스 | 추출 경로 |
|---|---|
| 33m2 | Next.js RSC 플라이트 페이로드(`self.__next_f`) + REST API(`/v1/use-auth/…`) 직접 호출 |
| Airbnb | GraphQL 응답 캐시(`<script id="data-deferred-state-0">` → `niobeClientData`) |

수치는 가능한 한 **교차 검증**했습니다.
예: 33m2 임대인 수수료율은 정산 완료 7건 전부에서 `이용금액 × 0.967`로 일치.

## 원칙

- 코드·디자인 자산·콘텐츠를 복제하지 않습니다. **동작과 구조**만 기록합니다.
- 실제 계약 체결·결제·메시지 발송 등 **외부에 영향을 주는 행위는 하지 않았습니다**.
  (계약 요청·예약 결제 모두 최종 버튼 직전에서 중단)
- 실계정 관찰 시 개인정보(성명·주소·연락처·계좌)는 **구조만 기록하고 값은 생략**합니다.
- 약관 동의 등 법적 효력이 있는 선택은 **대신 수행하지 않았습니다**.

## ⚠️ 정리 필요 (사용자 조치)

Airbnb 호스트 입력 모델 추출을 위해 생성한 **테스트용 draft 리스팅**이 남아 있습니다.

- listingId: `1752152568959500777`
- 주소: 서울특별시 중구 세종대로 110 (서울시청 — 실제 소유 부동산과 무관한 공공건물)
- 상태: **게시되지 않음(draft, "진행중")**

삭제 방법: `airbnb.co.kr/hosting/listings` → 「변경된 약관 및 정책」 모달 처리 → 해당 카드에서 삭제.
(모달은 법적 동의라 대신 처리하지 않았습니다.)
