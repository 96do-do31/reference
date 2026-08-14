# 33m2 API 카탈로그 (역추출)

> 출처: JS 번들 35청크(2.5MB) 경로 문자열 마이닝 + 실호출 검증 + 네트워크 관찰.
> `✅` = 실호출로 응답 확인 · `👁` = 네트워크에서 관찰 · `🔍` = 번들에서 경로만 발견(미검증)

**Base**: `https://web.33m2.co.kr`
**네임스페이스**: `/v1/use-auth/…` (인증 사용) · `/v1/no-auth/…` (비인증) · `/v2/…` (신규) · `/api/…` (Next.js 라우트 핸들러)

---

## 0. 아키텍처 요약

| 계층 | 방식 |
|---|---|
| **조회(Read)** | REST `/v1/use-auth/…` + **RSC 서버 렌더링** (페이지 데이터 대부분) |
| **변경(Write)** | **Next.js Server Actions** — 번들에서 `createServerReference` 94곳, 액션 ID 71개 확인. REST 쓰기 엔드포인트가 아님 |
| **실시간(채팅)** | **Firebase Realtime Database** (`onValue` 34, `onChildAdded`, `limitToLast`) |
| **푸시** | **Firebase Cloud Messaging** (`getToken`, `onMessage`, service worker) |
| **인증** | Firebase Auth → 자체 JWT (`/api/auth/session`, `/api/auth/refresh`, `/api/auth/sign-out`) |
| **본인인증** | **MOK** (드림시큐리티) — `/v1/cert/mok/terms` |
| **결제 PG** | **토스페이먼츠** — `/payments/toss/widget-info` |

> ⚠️ **쓰기 API를 REST로 기대하지 마세요.** 계약 요청·승인·취소·리뷰 작성 등은 모두 서버 액션입니다.
> 새 서비스가 웹+앱(2차) 구조라면 **앱에서도 쓸 수 있도록 REST로 설계**하는 편이 낫습니다.

---

## 1. 공통 규약

**성공** `{ "code": "SCSS_001", "data": … }`
**에러** ✅
```jsonc
{
  "code": "ROOM_001",
  "message": { "type": "ALERT", "content": "존재하지 않는 방입니다" },
  "data": { "month": "올바른 월을 입력해주세요" }   // 필드별 검증 에러(선택)
}
```
- 비즈니스/검증 오류 = **HTTP 400** + 도메인 코드
- 없는 경로 = 404 (빈 본문)
- 코드 도메인: `AUTH_*`(12) `USER_*`(20) `CERT_*`(19) `CTR_*`(45) `CARE_*`(3) `ROOM_*` `ADDR_*` `VLD_*`(2) `SYS_*` → `33m2/enums.md`

---

## 2. 인증 · 계정

| M | 경로 | 상태 | 비고 |
|---|---|---|---|
| GET | `/v1/use-auth/user/me` | ✅ | 로그인 사용자. `{email, name, profileImageUrl, phoneNumber, userType, isCertificated, …}` |
| POST | `/api/auth/session` | 🔍 | 세션 생성 |
| POST | `/api/auth/refresh` | 🔍 | 토큰 갱신 |
| POST | `/api/auth/sign-out` | 🔍 | 로그아웃 |
| POST | `/v1/token` | 🔍 | Firebase 토큰 교환 (refresh_token grant) |
| GET | `/v1/cert/mok/terms` | 🔍 | **MOK 본인인증 약관** |

**`user/me` 응답 (실측)**
```jsonc
{ "code":"SCSS_001", "data": {
  "email":"…", "name":"…", "profileImageUrl":"profile/{uuid}.png",
  "phoneNumber":"010…", "userType":"host",        // ★ enum: host | guest
  "isCertificated":true, …                        // 전체 17필드 → zod-schemas.md S06
}}
```

---

## 3. 매물 조회 · 검색

| M | 경로 | 상태 | 파라미터 |
|---|---|---|---|
| GET | `/v1/use-auth/map/rooms` | ✅ | `swLat swLng neLat neLng size page` + 필터 12종 |
| GET | `/v1/use-auth/map/markers` | 👁 | `zoomLevel swLat swLng neLat neLng` |
| GET | `/v1/use-auth/map/search-keywords` | 🔍 | 지도 검색어 |
| GET | `/v1/use-auth/rooms` | 🔍 | 매물 목록 |
| GET | `/v1/use-auth/rooms/{rid}/schedules` | ✅ | `year month` → 점유일만 반환 |
| GET | `/v1/use-auth/rooms/{rid}/available-weeks` | 🔍 | **선택 가능 주수** (기간 그리드) |
| GET | `/v1/use-auth/rooms/recommend/search-keywords` | ✅ | `{keywords:["서울","부산","인천","제주","강원도","강남","홍대","수원","성남","서울역"]}` |
| GET | `/v1/use-auth/rooms/favorites` | 🔍 | **찜 목록** |
| GET | `/v1/use-auth/rooms/recent-views` | 🔍 | **최근 본 방 목록** |
| POST | `/v1/use-auth/rooms/recent/view` | 🔍 | 최근 본 방 기록 |
| GET | `/v1/use-auth/rooms/hosts/{uid}` | 🔍 | 임대인의 매물 |
| GET | `/v1/use-auth/rooms/{rid}/preview` | 🔍 | 미리보기 (호스트) |
| POST | `/v1/use-auth/rooms/{rid}/contact-host` | 🔍 | **임대인에게 문의** |

**검색 필터 전체** → `_synthesis/api-observed.md` §검색 API 계약
`roomCounts` `propertyTypes` `pyeongSizes` `floors` `popularOptions` `basicOptions` `additionalOptions` `roomDiscounts` `minUsingFee` `maxUsingFee` `startDate` `endDate`

---

## 4. 계약 (게스트)

| M | 경로 | 상태 | 비고 |
|---|---|---|---|
| GET | `/v1/use-auth/guest/contracts/last-active` | ✅ | `rid` — 해당 매물의 진행 중 계약 |
| GET | `/v1/guest/contracts/need-checkin` | 🔍 | **입주 확인 필요 계약** |
| GET | `/v1/guest/contracts/need-review` | 🔍 | **후기 작성 필요 계약** |
| GET | `/v1/guest/contracts/schedule-changes/result` | 🔍 | 일정 변경 결과 |
| GET | `/v1/use-auth/…/admin/guest/contracts/estimate` | 🔍 | **견적 계산** |
| GET | `…/payment-eligibility` | 🔍 | 결제 가능 여부 |
| GET | `…/calculated-refund-info` | 🔍 | **환불 금액 계산** |
| GET | `…/refund/checklist` | 🔍 | 환불 체크리스트 |
| GET | `…/check-in/checklist` | 🔍 | **입주 체크리스트** |
| GET | `…/check-out/checklist` | 🔍 | **퇴실 체크리스트** |
| GET/PUT | `…/deposit-return-account` | 🔍 | 보증금 반환 계좌 |
| GET/PUT | `…/deposit-return-card` | 🔍 | 보증금 카드 환불 |
| GET/PUT | `…/refund-account` | 🔍 | 환불 계좌 |
| GET/PUT | `…/refund-card` | 🔍 | 환불 카드 |
| GET/PUT | `…/receipt-info` | 🔍 | 영수증 정보 |
| GET | `…/receipt-info/bill-url` | 🔍 | 영수증 URL |
| GET | `…/bill` | 🔍 | 결제내역서 |
| GET | `…/care-link` | 🔍 | **삼삼케어 링크** |

## 5. 일정 변경 (Schedule Change)

| M | 경로 | 비고 |
|---|---|---|
| GET/POST | `…/schedule-change` | 요청 생성·조회 |
| GET | `…/schedule-change/history` | **변경 이력** |
| GET | `…/schedule-changes/availability` | 변경 가능 일정 |

> 엔티티 `ScheduleChange` → `zod-schemas.md` S09/S12
> `{scheduleId, initialContractId, roomId, status, isAnswerable, unanswerableReason, guestMessage, hostMessage, currentStartDate, currentEndDate, requestedStartDate, requestedEndDate, requestedAt, completedAt, sequence}`

## 6. 계약 (호스트)

| M | 경로 | 비고 |
|---|---|---|
| GET | **`/v2/host/contracts/masters`** | ★ **v2 API** — 계약 마스터 목록 |

> `ContractMaster` → `33m2/DOMAIN.md` §1

## 7. 리뷰

| M | 경로 | 상태 |
|---|---|---|
| GET | `/v1/use-auth/contracts/simple-review-templates` | ✅ 태그 리뷰 템플릿 8종 |
| GET/POST | `…/review` | 🔍 |
| GET | `…/my/review` | 🔍 |

## 8. 결제

| M | 경로 | 비고 |
|---|---|---|
| GET | `/v1/use-auth/payments/toss/widget-info` | **토스페이먼츠 위젯 정보** |

> PG = **토스페이먼츠**. 위젯 방식(결제창 SDK) 사용.

## 9. 공통 코드

| M | 경로 | 상태 | 응답 |
|---|---|---|---|
| GET | `/v1/use-auth/accounts/bank-codes` | ✅ | `[{name:"국민은행", code:"0004"}, {name:"농협",code:"0011"}, {name:"신한은행",code:"0088"}, {name:"우리은행",code:"0020"}, {name:"기업은행",code:"0003"}, {name:"KEB하나은행",code:"…"}, …]` |

> 은행 코드 = **4자리 금융결제원 표준 코드**.

## 10. 로깅

| M | 경로 |
|---|---|
| POST | `/api/log/search-keywords` |
| POST | `/api/log/click-keyword` |

---

## 11. 채팅 — REST(메타) + Firebase RDB(메시지) 하이브리드 ★

### 11.1 REST — 스레드 메타·액션 ✅ 실측

| M | 경로 | 응답 |
|---|---|---|
| GET | `/v1/use-auth/chat/{cid}` | `{ roomName, picMain, contract }` |
| GET | `/v1/use-auth/chat/{cid}/actions` | `{ floatingAction, headerActions[] }` |

> ⭐ **스레드 키가 `cid`(ContractMaster ID)** — 채팅이 **계약 마스터 단위**임이 확정됩니다.
> 연장으로 계약이 여러 건이 되어도 **스레드는 하나**로 유지됩니다.
>
> `actions` 는 상태에 따라 바뀌는 **UI 액션 정의**(플로팅 버튼/헤더 액션)를 서버가 내려주는 구조.
> 서버 주도 액션 플래그(`isCallAvailable` 등)와 같은 설계 철학.

### 11.2 메시지 스트림 — Firebase Realtime Database

메시지 본문은 REST가 아닙니다. 번들 분석에서 확인:
```
Firebase Realtime Database (project: *-rdb, databaseURL: *-rtdb.firebaseio.com)
  ├─ onValue()        (34회)  스레드/메시지 구독
  ├─ onChildAdded()   신규 메시지 수신
  ├─ push()           메시지 발송
  ├─ limitToLast(n)   (6회)   최근 N건
  └─ startAt / endAt  (14회)  페이지네이션
```
- 인증: Firebase Auth 토큰 (세션의 `firebaseToken`)
- 자동 메시지는 **서버가 발행** (스케줄러) — `33m2/host/screens-and-model.md` §자동 메시지

> ⚠️ RDB 연결은 WebSocket이라 확장 프로그램 네트워크 로그에 잡히지 않았습니다.
> **RDB 경로 스키마는 미확인** — 실제 메시지 송수신 관찰이 필요합니다.
> ⚠️ 보안 규칙(Firebase Rules)은 관찰 불가.

> 💡 **역할 분리가 좋은 설계입니다**: 메타데이터·권한·액션은 백엔드 REST가,
> 고빈도 메시지 스트림은 실시간 DB가 담당. 새 서비스도 채택 권장.

---

## 12. 푸시 알림 — FCM

- `getToken()` 으로 디바이스 토큰 발급 → 서버 등록
- `onMessage()` 포그라운드 수신
- Service Worker 백그라운드 수신
- 채널: 앱 푸시 / **카카오톡** / 문자 / 이메일 (알림 설정 §`33m2/guest/screens.md`)

---

## 13. 미확인 (원리상/접근상)

- [ ] 서버 액션 71개의 **실제 파라미터·응답** — 액션 ID는 확보했으나 호출 시그니처는 서버 코드에 있음
- [ ] Firebase RDB **데이터 구조**(경로 스키마) — 실제 채팅 세션 관찰 필요
- [ ] Firebase 보안 규칙
- [ ] 토스페이먼츠 연동 상세(결제 승인 콜백)
- [ ] MOK 본인인증 콜백 플로우
- [ ] 관리자(어드민) API
