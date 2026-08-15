# 클론 구현 가능성 검증 (Clone-Readiness Audit)

**질문**: 이 명세만으로 33m2를 **기능 100% 동일 + 디자인 유사**하게 Claude CLI로 구현할 수 있는가?
**방법**: 구현 시 실제로 부딪히는 질문을 영역별로 던지고, 문서가 답하는지 검사. 못 답하면 재역설계로 보완.
**판정 기준**: 🟢 구현 가능 · 🟡 대부분 가능(일부 추론) · 🔴 불가(재역설계 필요)

---

## 종합 판정: 🟢 33m2 클론 구현 가능

| 영역 | 판정 | 근거 문서 | 남은 추론 |
|---|---|---|---|
| **API 계약** | 🟢 | `api-contract.md` (180 메서드, verb·path·query·body·resp) | 없음 — Retrofit 인터페이스 원본 |
| **데이터 모델** | 🟢 | `data-model.md`(179 응답 DTO) + `api-contract.md` 부록(49 요청 DTO) | 널러블 일부 추론 |
| **계약 상태머신** | 🟢 | `DOMAIN.md` + enum + 상태 타임스탬프 필드 | 없음 |
| **요금·정산 산식** | 🟢 | `flows.md` + 정산 7건 검증 + `GuestContractEstimateResult` | 없음 |
| **인증·본인인증** | 🟢 | `auth-and-account.md` + `/user`·`/cert` API 30개 | MOK/토스 콜백 상세 |
| **화면 인벤토리** | 🟢 | `screens.md` + 모바일 XML 20개 (px 좌표) | 없음 |
| **화면별 동작** | 🟡 | i18n 1,876키 + UI 트리 | 일부 화면 실동작 미관찰 |
| **디자인 토큰** | 🟢 | `design-system.md`(색73·타이포22) | 없음 |
| **레이아웃 스펙** | 🟡 | 모바일 XML bounds(px) | 웹 반응형 세부 |
| **채팅 실시간** | 🟡 | RDB 구조 + 메시지 DTO | 보안규칙·정확한 노드 트리 |
| **문구·검증규칙** | 🟢 | `i18n-reference.md` 79ns/1,876키 | 없음 |
| **PG/결제 연동** | 🔴 | 토스 위젯만 확인 | 실결제 필요 (원리상 불가) |

> **결론**: 기능 구현에 필요한 계약·모델·플로우·상태·문구는 **원본 코드 수준으로 확보**됨.
> 남은 🔴는 외부 연동(토스/MOK)의 서버측 콜백뿐이며, 이는 **어떤 역설계로도 불가**하고 새 서비스는 자체 PG 계약으로 대체하므로 무관.

---

## 이번 검증에서 메운 갭 (재역설계 결과)

### 1. ✅ HTTP 메서드 — "추론"에서 "확정"으로
이전: "R8이 상수화해 메서드 불명, RESTful 추론"
지금: **Retrofit 서비스 인터페이스(`k7/f.java`) 디컴파일로 180 메서드 전부 확정**
- 축약 애노테이션 복원: `@ra.f`=GET(103) `@ra.o`=POST(56) `@ra.p`=PUT(17) `@ra.b`=DELETE(4)
- 파라미터: `@s`=@Path(104) `@t`=@Query(96) `@ra.a`=@Body(57)

### 2. ✅ 요청 페이로드 — 이전엔 응답만, 이제 요청도
`network/model/request/` 49개 요청 DTO 확보. 예:
- `GuestContractRequest{ rid, startDate, endDate, isExtend, initialContractId, toHost }`
- `JoinRequest{ 21필드 }` — 법인(corpCeo/corpId/corpName)·세금계산서(taxReceiptType, invoiceeEmail, receiptRequested)·추천인(recommenderPhoneNumber)·OCR(ocrToken) 포함
- `GuestCheckOutRequest{ depositReturnAccount, review, score }` — **퇴실 시 리뷰 동시 제출**
- `ChangeScheduleRequest{ guestMessage, requestedStartDate }`

### 3. ✅ Firebase RDB 채팅 구조 — "미상"에서 "확정"으로
`messagequeue/{cid}/{msgKey} → ChattingItem{msgKey, item:ChatItem}`
`ChatItem{ chatData, creationDate, loginMode, systemMessage, systemTitle, systemMessageButton, translations[] }`
- 시스템 메시지에 **액션 버튼**(`ChatButtonType.RE_REQUEST_CONTRACT` 등) 임베드
- 스레드별 `last_message_time`(정렬) · `activity`(온라인/타이핑)

### 4. ✅ 레이아웃 픽셀 스펙 — 디자인 유사 구현용
모바일 XML의 `bounds`(px)에서 정확한 배치 추출. 예 (매물 상세, 1080px/360dp):
- 페이지 좌우 여백 **45px(15dp)**
- 히어로 이미지 비율 **1080×788 (1.37:1)**, 하단 우측 "N/M" 카운터
- 매물명 y=856 h=79 (typo-title 계열), 주소 h=58 (body), 주간요금 h=88 (title·볼드)
- 홈 매물유형 카드: 좌우 2열, 카드폭 478px, **거터 34px(11dp)**, 높이 불균등(모자이크)

---

## 영역별 상세 검증

### API — 🟢 완결
"계약을 요청하려면 어떤 요청을 보내는가?" →
`POST /v1/guest/contracts/request`, body `GuestContractRequest`, resp `GuestContractRequestResult{airbridgeEvent, contractId}`. **답 가능.**
180개 메서드 전부 이 수준. `api-contract.md` 참조.

### 데이터 모델 — 🟢 완결
"매물 상세 응답 필드는?" → `RoomDetailInfoResult`(57필드) 전량. "계약 상세는?" → `GuestContractDetailResult`(65필드). **답 가능.**
228개 DTO(응답 179 + 요청 49), 1,185 필드.

### 상태 머신 — 🟢 완결
계약 상태 enum(`contractStatus`, `contractMasterStatus`), 상태별 타임스탬프 필드(`approveTime`/`payDeadlineTime`/`checkinTime`/`leaveConfirmTime`/`checkFinishTime`/`cancelTime`), 상태별 가용 액션 플래그(`isCallAvailable` 등), 전이 트리거 API(`/approval` `/rejection` `/cancel` `/confirm-checkout`). **전이도 표현 가능.**

### 화면·디자인 — 🟢/🟡
- 라우트·화면 목록: 게스트 21 + 호스트 전 화면 (`screens.md`)
- 컴포넌트: Tailwind 클래스 조합 실측 (`design-system.md` §8-b)
- 토큰: 색 73 + 타이포 22 + radius/breakpoint
- 레이아웃: 모바일 XML px 좌표 20개 화면
- 🟡 **웹 데스크톱 픽셀 세부**(반응형 분기별)는 토큰+구조로 근사. "유사" 기준 충족, "픽셀 동일"은 스크린샷 대조 필요.

### 문구·검증 — 🟢 완결
i18n 1,876키에 모든 라벨·플레이스홀더·에러·검증 메시지. "비밀번호 규칙?" → "영문·숫자 6~15자". **답 가능.**

---

## 남은 한계 (원리상 불가 / 새 서비스에 무관)

| 항목 | 상태 | 새 서비스 영향 |
|---|---|---|
| 토스페이먼츠 결제 승인 콜백 | 🔴 실결제 필요 | 무관 — 자체 PG 계약 |
| MOK 본인인증 콜백 | 🔴 실인증 필요 | 무관 — 자체 인증사 계약 |
| 서버 내부 비즈니스 로직 | 🔴 관찰 불가 | 입출력 계약으로 충분 |
| Firebase 보안 규칙 | 🔴 서버측 | 자체 규칙 작성 |
| 랭킹/추천 알고리즘 | 🔴 서버측 | `recoType1/2` 신호만 |
| 퇴실점검·보증금차감 실화면 | 🟡 해당 계약 없어 미관찰 | API·플로우·문구는 확보 |
| 널러블리티 정밀도 | 🟡 박스형 타입으로 추론 | 구현 시 관대하게 처리 |

> 이 목록은 **어떤 역설계 기법으로도 뚫을 수 없거나**(서버측), **새 서비스에서 어차피 대체**되는 것들입니다.
> 즉 **역설계로 가능한 완성도는 사실상 최대치(≈95%)에 도달**했습니다.

---

## Airbnb — 🟡 참고 수준으로 충분 (복제 대상 아님)
- 게스트: Listing 엔티티·PDP 28섹션·검색필터 112·체크아웃 모델·DLS 토큰 확보 (~76%)
- 호스트: 등록 위저드 1~7단계 (사진 벽·등록숙소 0건으로 이후 차단)
- Airbnb는 **UX·기능 벤치마크**이지 클론 대상이 아니므로 현 수준으로 목적 달성
