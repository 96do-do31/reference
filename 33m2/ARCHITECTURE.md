# 33m2 (삼삼엠투) — 아키텍처 역설계 노트

> 출처: `web.33m2.co.kr` 실사용 세션 관찰 (2026-08-14). 코드/자산 복제 없음, 동작·구조 관찰 기록.

## 1. 기술 스택 (관찰 기반)

| 레이어 | 확인된 내용 | 근거 |
|---|---|---|
| 웹 프레임워크 | **Next.js App Router (RSC)** | `?_rsc=` 프리페치 요청, `self.__next_f` 플라이트 페이로드, `static/chunks/*` |
| 렌더링 전략 | 대부분 **서버 컴포넌트** — 페이지 데이터가 RSC 페이로드로 인라인 전달 | 상세/목록 페이지에서 클라이언트 XHR 없음 |
| 백엔드 | **Java/Spring Boot 추정** | 응답 엔벨로프 `{code:"SCSS_001", data:{content:[], ...}}` = Spring `Page` 직렬화 형태 |
| 인증 | **Firebase Authentication** | `identitytoolkit.googleapis.com` 호출 |
| 지도(검색) | **네이버 지도 API** | `oapi.map.naver.com/openapi/v3/maps.js?ncpKeyId=…` |
| 지도(상세) | **카카오 지도 타일** | `mts.daumcdn.net/api/v1/tile/…` |
| 이미지 CDN | CloudFront + 온더플라이 리사이즈/워터마크 | `d1pviohoskiraj.cloudfront.net/{room\|profile\|campaign}/{uuid}.jpg?b=samsamm2&d=720x480&v=wm` |
| 정적 자산 CDN | `dsti6pxai92pb.cloudfront.net` | |
| 관측/분석 | Datadog RUM(+Session Replay), GA4, GTM, Airbridge(앱 어트리뷰션), Meta Pixel, Kakao/Criteo 픽셀 | |
| i18n | 다국어 지원 (`ko` 로케일 프리픽스, `translationApplied` 필드) | `/ko/host/main`, 룸 응답의 `translationApplied` |

### 이미지 CDN 파라미터 규약
```
{cdn}/{scope}/{uuid}.{ext}?b=samsamm2&d={W}x{H}&v=wm
  scope : room | profile | campaign
  d     : 목표 크기. 높이 0 이면 비율 유지 (예: 720x0)
  v=wm  : 워터마크 적용
```
관찰된 크기 프리셋: `240x240`, `360x240`, `480x480`, `720x0`, `720x480`

---

## 2. API 표면

베이스: `https://web.33m2.co.kr/v1/`

네임스페이스가 인증 요구 여부로 갈립니다:
- `/v1/use-auth/…` — 인증 컨텍스트를 사용 (로그인 시 개인화, 예: `like` 필드)
- `/v1/no-auth/…` — 비인증 (추정, 명명 규약상)

### 확인된 엔드포인트

```http
GET /v1/use-auth/map/rooms?swLat&swLng&neLat&neLng&size&page
GET /v1/use-auth/map/markers?zoomLevel&swLat&swLng&neLat&neLng
```

**공통 응답 엔벨로프**
```jsonc
{
  "code": "SCSS_001",        // 성공 코드. 에러 시 다른 코드 체계로 추정
  "data": {
    "content": [ /* … */ ],  // Spring Page
    // page/size/totalElements 등 동반 추정
  }
}
```

> ⚠️ 페이지 데이터 대부분은 REST가 아니라 **RSC 페이로드**로 전달됩니다. 지도(bbox 기반 갱신)처럼 클라이언트 상호작용이 필요한 부분만 REST를 씁니다.

---

## 3. 라우트 인벤토리 (관찰된 것)

### 게스트(임차인)
| 경로 | 화면 |
|---|---|
| `/guest/main` | 홈 — 검색바, 매물유형 숏컷, 지도 진입 배너, 최근 본 방, 캠페인 |
| `/guest/search?lat&lng&zoomLevel` | 지도 검색 — 좌측 리스트 + 우측 지도, 상단 필터 |
| `/guest/room/{rid}` | 매물 상세 (**새 탭으로 열림**) |
| `/guest/contract` | 계약 목록 |
| `/guest/chat` | 채팅 |
| `/guest/notification` | 알림 |

### 호스트(임대인)
| 경로 | 화면 |
|---|---|
| `/host/main`, `/ko/host/main` | 호스트 홈 |

> 게스트↔호스트는 **동일 계정 내 모드 전환** (헤더 "임대인 모드로 전환"). 별도 계정이 아님.

---

## 4. 도메인 어휘 (i18n 사전에서 추출)

`common` 네임스페이스 상위 키: `actual_cost, agree_to_all, bathroom(ba), bedroom(br), kitchen(kit), living_room(lr), cleaning_fee, deposit, discount{immediate,long_term}, move_in, move_out, property_type, basic_option, additional_option, popular_option, rent, service_fee, total_payment, utility_fee, week_unit, price_manwon, landlord, tenant, sort, share, upload, toast, notice`

**드러난 비즈니스 규칙**
- `deposit_notice`: "보증금은 삼삼엠투에서 보관하며, 퇴실 후 반환됩니다." → **플랫폼 에스크로 모델**
- `dialog.title`: "규정 위반으로 이용이 중지되었습니다" → 계정 정지 상태 존재
- `error.restricted`: 비정상 트래픽 감지 시 접속 제한 → 레이트리밋/봇 방어
- 가격 표기 단위 이원화: `won` / `price_manwon` (만원)
- 역할 명칭: **landlord(임대인) / tenant(임차인)** — Airbnb의 host/guest와 다른 임대차 프레이밍

---

## 5. 관찰된 UX 특징

- 매물 상세가 **새 탭**으로 열림 (한국 부동산 서비스 관행)
- 검색 상태가 **URL 쿼리에 반영** (`lat`, `lng`, `zoomLevel`) → 공유/뒤로가기 가능
- 지도 갱신은 **bbox(sw/ne) + zoomLevel** 기반, 마커와 리스트가 별도 엔드포인트
- 요금이 **주 단위(1주)** 로 표시 — 단기임대 특화
- "우수 임대인" 배지 (`isSuperHost`)
- 카드에 할인 배지 노출: "장기계약 ~10% 할인", "즉시입주 ~7만 원 할인"
