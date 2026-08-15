# 33m2 전체 API 엔드포인트 (APK 정적 분석)

> 출처: **안드로이드 앱 APK 디컴파일**(`com.samsamm2.mobileapp`, jadx). 경로가 코드에 상수로 존재 → **확실(📦)**.
> HTTP 메서드는 R8 최적화로 정수 상수화되어 문자열로 남지 않음 → RESTful 규약으로 **추론(⇒)**. 실호출로 검증된 것은 ✅.
> 원본 목록: `_shared/captures/33m2.api-endpoints.txt`

**159개 고유 경로.** 웹 Server Action이 감싸던 실체가 이 REST API입니다.

## 규약

- Base: `https://web.33m2.co.kr`
- 성공 `{code:"SCSS_001", data}` · 에러 `{code, message:{type,content}, data?}` (HTTP 400)
- `{mode}` / `{type}` / `{loginType}` = `guest` | `host` — **역할 공통 엔드포인트를 파라미터화**
- `{cid}` = ContractMaster ID · `{initialContractId}` = 마스터의 최초 계약 ID · `{contractId}` = 개별 계약 · `{rid}` = Room ID

---

## 1. 인증 · 계정 (`/v1/user`, `/v1/cert`)

| 메서드⇒ | 경로 | 의미 |
|---|---|---|
| POST | `/v1/user/login` | 로그인 |
| POST | `/v1/user/logout` | 로그아웃 |
| POST | `/v1/user/refresh` | 토큰 갱신 |
| POST | `/v1/user/join/{joinType}` | **회원가입** (joinType = 역할/가입경로) |
| GET | `/v1/user/me` ✅ | 내 정보 |
| PUT | `/v1/user/me/guest-profile` | 임차인 프로필 수정 |
| PUT | `/v1/user/me/host-profile` | 임대인 프로필 수정 (소개·정산계좌) |
| GET | `/v1/user/me/firebase-token` | **Firebase 커스텀 토큰** (채팅/푸시용) |
| POST | `/v1/user/me/cert` | 본인인증 등록 |
| POST | `/v1/user/me/cert/passport` | 여권 인증 등록 |
| POST | `/v1/user/me/email/send` · `/verify` | 이메일 인증 |
| POST | `/v1/user/find-id` | 아이디 찾기 |
| POST | `/v1/user/email/validation` · `/phone-number/validation` | 중복/형식 검증 |
| POST | `/v1/user/password-reset` (+ `/email`, `/email/send`, `/email/verify`, `/validation`) | 비밀번호 재설정 |
| POST | **`/v1/user/host-conversion`** (+ `/validation`) | 🆕 **임차인 → 임대인 전환** |

**본인인증(`/v1/cert`)**
| 경로 | 의미 |
|---|---|
| `/v1/cert/mok/terms` · `/send` · `/resend` · `/verify` | **MOK 휴대폰 본인인증** (드림시큐리티) |
| `/v1/cert/email/send` · `/verify` | 이메일 인증 |
| `/v1/cert/passport/ocr` | **여권 OCR** |
| `/v1/cert/phone-number` | 휴대폰 번호 |

---

## 2. 매물 조회 (`/v1/rooms`, `/v1/map`)

| 메서드⇒ | 경로 | 의미 |
|---|---|---|
| GET | `/v1/rooms` | 매물 목록 |
| GET | `/v1/rooms/{rid}` | 매물 상세 |
| GET | `/v1/rooms/{rid}/schedules` ✅ | 예약 가능 일정 (점유일만) |
| GET | `/v1/rooms/{rid}/available-weeks` | **선택 가능 주수** (기간 그리드) |
| GET | `/v1/rooms/{rid}/contract-availability` | 계약 가능 여부 |
| GET | `/v1/rooms/{rid}/contract/{contractId}` | 특정 계약 컨텍스트의 매물 |
| PUT/DEL | `/v1/rooms/{rid}/favorites` · `/v1/rooms/favorites` | **찜 토글/목록** |
| GET/POST | `/v1/rooms/recent-views` · `/v1/rooms/recent/view` | 최근 본 방 |
| GET | `/v1/rooms/recommend/search-keywords` ✅ | 추천 검색어 |
| GET | `/v1/rooms/hosts/{hostUid}` | 임대인의 매물 |
| GET | `/v1/map/rooms` ✅ | 지도 bbox 매물 |
| GET | `/v1/map/search-keywords` | 지도 검색어 |

**주소(`/v1/address`)**: `/search`(검색) · `/details`(상세) — 우편번호/도로명 조회

---

## 3. 매물 관리 — 호스트 (`/v1/host/rooms`) ★

**등록/수정이 필드 그룹별 엔드포인트로 분리** (위저드 5단계와 대응):

| 메서드⇒ | 경로 | 위저드 단계 |
|---|---|---|
| POST | `/v1/host/rooms` | 신규 생성 |
| GET | `/v1/host/rooms/{rid}` | 매물 조회 |
| POST | `/v1/host/rooms/address/validation` | 주소 검증 (1단계 전) |
| PUT | `/v1/host/rooms/{rid}/space-info` | **1 공간** (구조·면적·주차) |
| PUT | `/v1/host/rooms/{rid}/fee-info` | **2 임대료** (요금·할인·환불) |
| PUT | `/v1/host/rooms/{rid}/options` | **3 옵션** |
| PUT | `/v1/host/rooms/{rid}/description` | **4 방 설명** (이름·사진·소개) |
| PUT | `/v1/host/rooms/{rid}/contract-policy` | **5 일정** (최소기간·턴오버) |
| GET | `/v1/host/rooms/{rid}/progress` | 등록 진행률 |
| PUT | `/v1/host/rooms/{rid}/visibility` | **공개/비공개 전환** |
| POST | `/v1/host/rooms/{rid}/deletion` | 삭제 |
| POST | **`/v1/host/rooms/{sourceRid}/clone`** | **복제** (다호실 운영) |
| GET | `/v1/host/rooms/{rid}/preview` | 미리보기 |
| POST | `/v1/host/rooms/{rid}/review-request` | 후기 요청 |
| GET/PUT | `/v1/host/rooms/{rid}/schedules` · `/schedules/unavailable` | 일정 관리 (차단일) |
| GET | `/v1/host/rooms/survey-requirements` | 등록 설문 요건 |

> 💡 **필드 그룹별 PUT 분리**는 위저드 단계별 저장·검증에 최적. 새 서비스도 이 구조 권장.

---

## 4. 계약 — 게스트 (`/v1/guest/contracts`) ★

| 메서드⇒ | 경로 | 의미 |
|---|---|---|
| GET | `/v1/guest/contracts/masters` | 계약 마스터 목록 |
| GET | `/v1/guest/contracts/masters/{initialContractId}` | 마스터 상세 |
| GET | `/v1/guest/contracts/{contractId}` | 개별 계약 상세 |
| GET | `/v1/guest/contracts/last-active` ✅ | 매물별 활성 계약 |
| POST | `/v1/guest/contracts/estimate` | **견적 계산** |
| **POST** | **`/v1/guest/contracts/request`** | ★ **계약 요청** (인사 메시지 동반) |
| POST | `/v1/guest/contracts/{contractId}/cancel` | **계약 취소** |
| GET | `/v1/guest/contracts/{contractId}/refund-reasons` | 취소 사유 목록 |
| POST | `/v1/guest/contracts/{contractId}/refund` | 환불 실행 |
| GET | `/v1/guest/contracts/{contractId}/refund/checklist` | 환불 체크리스트 |
| PUT | `/v1/guest/contracts/{contractId}/refund-account` · `/refund-card` | 환불 수단 |
| PUT | `/v1/guest/contracts/{contractId}/deposit-return-account` · `/deposit-return-card` | 보증금 반환 수단 |
| PUT | `/v1/guest/contracts/{contractId}/receipt-info` (+ `/bill-url`) | 영수증 정보 |
| POST | `/v1/guest/contracts/{initialContractId}/check-in` | **입주 확인** |
| GET | `/v1/guest/contracts/{contractId}/check-in/checklist` | 입주 체크리스트 |
| POST | `/v1/guest/contracts/{initialContractId}/check-out` | **퇴실 신청** |
| GET | `/v1/guest/contracts/{initialContractId}/check-out/checklist` | 퇴실 체크리스트 |
| POST | `/v1/guest/contracts/{initialContractId}/simple-review` | 간이 리뷰 |
| GET | `/v1/guest/contracts/need-checkin` · `/need-review` | 입주확인/후기 필요 계약 |
| GET | `/v1/guest/contracts/notifications` | 계약 알림 |

**일정 변경 (게스트)**
```
GET  /v1/guest/contracts/masters/{initialContractId}/schedule-changes
GET  /v1/guest/contracts/masters/{initialContractId}/schedule-changes/availability
POST /v1/{mode}/contracts/masters/{initialContractId}/schedule-change        ← 공통
GET  /v1/{mode}/contracts/masters/{initialContractId}/schedule-change/history
POST /v1/guest/contracts/schedule-changes/{scheduleId}/cancel
GET  /v1/guest/contracts/schedule-changes/result
POST /v1/guest/contracts/schedule-changes/{scheduleId}/result/read
```

**리뷰 (게스트)**
```
GET  /v1/guest/contracts/reviews
GET  /v1/guest/contracts/reviews/{initialContractId}
POST /v1/guest/contracts/reviews/{contractId}/popup/read
```

---

## 5. 계약 — 호스트 (`/v1/host/contracts`) ★

| 메서드⇒ | 경로 | 의미 |
|---|---|---|
| GET | `/v1/host/contracts/masters/{initialContractId}` | 마스터 상세 |
| GET | `/v1/host/contracts/{contractId}` | 개별 계약 |
| **POST** | **`/v1/host/contracts/{contractId}/approval`** | ★ **계약 승인** |
| **POST** | **`/v1/host/contracts/{contractId}/rejection`** | ★ **계약 거절** |
| GET | `/v1/host/contracts/{contractId}/calculated-refund-info` | 환불 금액 계산 |
| **POST** | **`/v1/host/contracts/{initialContractId}/confirm-checkout`** | ★ **퇴실 확인** (보증금 반환 트리거) |
| **POST** | **`/v1/host/contracts/{initialContractId}/hold-checkout`** | ★ **보증금 지급 유예** |
| GET | `/v1/host/contracts/masters/{initialContractId}/care-link` | 삼삼케어 링크 |
| GET | `/v1/host/contracts/masters/actions/count` · `/status/count` | 할 일/상태 카운트 (대시보드) |
| GET/`v2` | `/v2/host/contracts/masters` | 계약 마스터 목록 (v2) |

**일정 변경 응답 (호스트)**
```
GET  /v1/host/contracts/schedule-changes/{scheduleId}
POST /v1/host/contracts/schedule-changes/{scheduleId}/approval   ← 승인
POST /v1/host/contracts/schedule-changes/{scheduleId}/rejection  ← 거절
```

**리뷰 답글 (호스트)**
```
GET  /v1/host/contract/reviews  ·  /summary  ·  /{contractId}
POST /v1/host/contract/reviews/{contractId}/replies    ← ★ 답글 작성
```

---

## 6. 정산 (`/v1/settlements`)

| 경로 | 의미 |
|---|---|
| `/v1/settlements/ready` | 정산 예정 |
| `/v1/settlements/complete` | 정산 완료 |
| `/v1/settlements/{contractId}` | 정산 상세 |
| `/v1/settlements/rooms` | 매물별 정산 |

---

## 7. 채팅 (`/v1/chat`) — REST 메타 + Firebase RDB 메시지

| 경로 | 의미 |
|---|---|
| `/v1/chat/{cid}` ✅ | 스레드 메타 (`roomName, picMain, contract`) — **키 = cid** |
| `/v1/chat/{cid}/actions` ✅ | 상태별 UI 액션 (floating/header) |
| `/v1/chat/{cid}/read` | 읽음 처리 |
| `/v1/chat/{cid}/contract-masters` · `/contract-period` | 스레드의 계약 정보 |
| `/v1/chat/{cid}/messages/{msg_idx}/translation` | **메시지 번역** (외국인 대응) |
| `/v1/chat/{cid}/messages/search/hint` | 메시지 검색 힌트 |
| `/v1/chat/messages` | 메시지 (발송/조회) |
| `/v1/chat/scheduled` · `/{id}` · `/connectable-rooms` | **자동 메시지** 관리 |

**Firebase RDB 구조** ✅ (APK 모델 클래스 확정)
```
messagequeue/{cid}/{msgKey} → ChattingItem{ msgKey, item: ChatItem }
  ChatItem{ chatData, creationDate, loginMode, systemMessage, systemTitle,
            systemMessageButton: ChatButton, translations[] }
  ChatButton{ type: ChatButtonType(INFO|RE_REQUEST_CONTRACT|…), target, parameters[] }
{cid}/last_message_time   ← 스레드 정렬
{cid}/activity            ← 온라인/타이핑 추정
```
- 시스템 메시지에 **액션 버튼 임베드**(계약 재요청 등). 계약 이벤트를 채팅 카드로 표시.
- `translations[]` 메시지별 번역 캐시(외국인), `loginMode`로 화자 구분.
- RDB 인증 토큰: `GET /v1/user/me/firebase-token`.
> 메시지 스트림 = RDB, 스레드 메타·액션·자동메시지·번역요청 = REST(`/v1/chat/*`).
> 상세 스키마는 `33m2/api-contract.md` §8 + `data-model.md`.

---

## 8. 공통 (`/v1/{type}`, `/v1/support`, `/v1/campaigns`, …)

**알림 (역할 공통)**
```
GET/PUT /v1/{type}/notification-settings
GET/PUT /v1/{type}/notification-settings/channels        ← 앱푸시/카카오톡/문자/이메일
GET/PUT /v1/{type}/notification-settings/do-not-disturb  ← 방해금지 시간대
GET     /v1/{type}/inbox  ·  /inbox/categories  ·  /inbox/{id}/read
```

**고객지원 (역할 공통)**
```
GET  /v1/support/{type}/faqs  ·  /faq-categories  ·  /notices  ·  /notices/{id}
GET  /v1/support/{loginType}/top-faqs
POST /v1/support/inquiries      ← 1:1 문의
```

**설문**: `/v1/surveys/{type}` · `/v1/surveys/{type}/submit` (가입 설문)

**콘텐츠·캠페인**
```
GET /v1/contents/guest/home  ·  /contents/host/home   ← 홈 위젯 데이터
GET /v1/campaigns/articles  ·  /articles/editor-pick/{loginType}
GET /v1/campaigns/events  ·  /campaigns/partnerships  ·  /campaigns/{id}
```

**호스트 공개 프로필**: `/v1/hosts/{hostUid}/profile` · `/v1/hosts/{hostUid}/reviews`

**공통 코드/계좌**
```
GET  /v1/accounts/bank-codes ✅       ← 은행코드 (4자리 금융결제원)
POST /v1/accounts/verification         ← 예금주 실명 확인
```

**앱/디바이스**: `/v1/apps/*`(버전·설정) · `/v1/devices/app-installations`(FCM 토큰 등록)

**리뷰 공통**: `/v1/contracts/recent-reviews` · `/v1/contracts/simple-review-templates` ✅

---

## 9. 웹 전용 (Next.js 라우트 핸들러)

앱에 없는 웹 전용 경로 (세션 관리):
```
/api/auth/session · /api/auth/refresh · /api/auth/sign-out
/api/log/search-keywords · /api/log/click-keyword
```

---

## 10. 새 서비스 설계 시사점

1. **역할 공통 엔드포인트를 `{mode}` 파라미터화** — 알림·일정변경 등 게스트/호스트 로직이 같은 곳. 코드 중복 제거
2. **매물 등록을 필드 그룹별 PUT으로 분리** — 위저드 단계별 부분 저장·검증에 최적
3. **동사형 액션 경로** (`/approval` `/rejection` `/cancel` `/confirm-checkout` `/hold-checkout`) — 상태 전이를 명시적 엔드포인트로. RESTful하면서 의도가 분명
4. **`/estimate` 를 별도 엔드포인트로** — 요청 전 견적을 서버가 계산 (가격 불일치 방지)
5. **채팅 하이브리드** (REST 메타 + 실시간 DB 메시지)
6. **`host-conversion`** — 임차인이 임대인이 되는 전환 플로우를 1급으로
7. 앱은 이 REST를 직접, 웹은 Server Action으로 래핑 — **API를 REST로 두면 웹·앱 공용**
