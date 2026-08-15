# Airbnb 데이터 모델 (GraphQL 타입·enum 역추출)

> 출처: 로그인 웹 `niobeClientData` 응답 스키마 + APK dex의 GraphQL Input 타입(566) · enum 문자열.
> 33m2의 `data-model.md`에 대응. Airbnb는 GraphQL이라 **응답은 오퍼레이션별 프레젠테이션 트리**, **요청은 Input 타입**.
> 원본: `_shared/captures/airbnb.graphql-inputs.txt`, `airbnb.pdp.sections.json`, `airbnb.search.json`

---

## 1. 응답 아키텍처 — 프레젠테이션 지향

33m2가 도메인 엔티티(`Room`, `Contract`)를 반환하는 반면, Airbnb는 **화면 조립용 트리**를 반환합니다.
공통 루트: `presentation.{screen}` (화면 섹션) · `viewer` (로그인 사용자) · `node` (엔티티, Relay Global ID)

**Relay 커넥션 패턴** (목록):
```
viewer.trips { edges[], pageInfo { hasNextPage, endCursor, totalCount } }
```
Global ID는 base64: `atob("VXNlcjo0OTU0NzA1MjE=")` = `User:495470521`, `StayListing:{id}`, `DemandStayListing:{id}`

---

> **필드 단위 스키마는 `airbnb/entity-schemas.md`** — Listing 198경로 · SearchResult 95 · BookIt 119 · Policies 46 (웹 실측 전개).

## 2. Listing (숙소) — `node.pdpPresentation` ✅ 웹 확인 (198 필드 경로)

27개 섹션 / 198 필드 경로. 전체 필드는 `entity-schemas.md`, 요약은 `listing-entity.md`. 요약:
```
amenities · descriptions · title · heroMedia · highlights · localizedLocation
location · personCapacity · sleepingArrangements · quality · hostInfo
accessibilityFeatures · bathroomsTour · addOnServices · seoLinks · pdpType
availabilityCalendarDescriptionItems · reportTermsDisclaimer · mediaTour · overview
```
> 33m2 `Room`(89필드) 대비 미디어·접근성·수면배치·부가서비스가 풍부. 보증금·관리비 개념은 없음.

---

## 3. User / Viewer ✅ 웹 확인 (`PersonalInfoQuery`)
```
viewer {
  timeZone, preferredLocale, nativeCurrency, preferredTimeZone,
  user {
    id(Global), isServiceHost, isExperienceHostV2, hostsWithCount,
    profileInfo { hostDisplayName },
    owner { preferredLanguageOthers }
  }
}
presentation.accountSetting.personalInfo {
  userPersonalInfo, addressFields[33], countries[242], languages[82]
}
```

## 4. Wishlist ✅ 웹 확인 (`WishlistIndexPageQuery`)
```
wishlist {
  createdBy: "USER",
  currentUserRole: "PRIVATE_OWNER" | (COLLABORATOR 등),
  collaboratorUsers[],
  dateRangeDetails { checkIn, checkOut },
  formattedDateRange,
  guestCount, guestDetails { numberOfAdults, numberOfChildren, numberOfInfants, ... }
}
```
> 위시리스트에 **날짜·게스트 컨텍스트가 붙음** (찜 목록이 곧 여행 계획). 협업(공유) 위시리스트 지원.

## 5. Checkout (예약) ✅ 웹 확인 — `airbnb/guest/checkout.md`
입력 `CheckoutFlowInput` / `CheckoutQuickPayDataInput` / `CompleteCheckOutInput`
식별자 4단: `orderId` · `bookingAttemptId` · `bookingQuoteId` · `confirmationCode`

---

## 6. GraphQL Input 타입 (566개, dex) — 요청 페이로드

### 예약·체크아웃
```
CheckoutFlowInput · CheckoutQuickPayDataInput · CheckoutTokenDataInput · CompleteCheckOutInput
AcceptReservationAlterationInput · CancelReservationAlterationInput · BookingRulesInput
CheckOutGuidePreviewInput · ActivityCheckoutFlowInput · BasePriceByMonthInput
```
### 결제 (PG별 — 지역 대응)
```
AdyenCreditCardPaymentOptionInput · BraintreeCreditCardPaymentOptionInput
CreatePaymentInstrumentInput · CheckoutPixCpfTextInput(브라질) · CheckoutFcUpiTextInput(인도)
CheckoutMBWayTextInput(포르투갈) · ClientPaymentErrorContextInput
```
### 검색
```
SearchInput(27회) · PriceInput · FilterInput 등
```
### 인증·챌린지 (에어락)
```
ChallengeUserInput · {Email,Sms,Voice,WhatsApp,Naver,Google,Apple,WeChat,Passkey,Password}ChallengeStepInput
IdentifyEmailStepInput · IdentifyPhoneStepInput · SignupFormStepInput · EmailOtpChallengeStepInput
```
> 🆕 **소셜 로그인 광범위**: 네이버·구글·애플·위챗·왓츠앱 + 패스키. 다단계 챌린지(OTP/음성/SMS).

전체 목록: `_shared/captures/airbnb.graphql-inputs.txt`

---

## 7. Enum (dex 확정)

| Enum | 값 |
|---|---|
| **RoomType** | `ENTIRE_HOME` · `PRIVATE_ROOM` · `SHARED_ROOM` |
| **BookingType** | `INSTANT_BOOK` · `REQUEST_TO_BOOK` |
| **CancellationPolicy** | `FLEXIBLE` · `MODERATE` · `STRICT` · `LONG_TERM` (+ FIRM/SUPER_STRICT 계열) |
| **ReservationStatus** | `NEW` · `INQUIRY` · `PENDING` · `PREAPPROVED` · `ACCEPTED` · `CONFIRMED` · `DECLINED` · `CANCELLED` · `COMPLETED` · `AT_CHECKPOINT`(에어락) · `TIMEDOUT` |
| **HostBadge** | `SUPERHOST` |
| **WishlistRole** | `PRIVATE_OWNER` · `COLLABORATOR` (추정) |

> 🔀 **33m2 대비 예약 상태가 더 세분**: 문의(INQUIRY)·사전승인(PREAPPROVED)·에어락(AT_CHECKPOINT) 상태 존재.
> 33m2엔 없는 **즉시예약/예약요청 이원화**(`INSTANT_BOOK`/`REQUEST_TO_BOOK`)가 예약 플로우의 근간.

---

## 8. 33m2와의 모델 차이 (구현 시 결정)

| 축 | 33m2 | Airbnb |
|---|---|---|
| API | REST 도메인 엔티티 | GraphQL 프레젠테이션 트리 |
| 요청 | REST body DTO (49) | GraphQL Input (566) |
| 목록 | Spring Page (content/page/size) | Relay 커넥션 (edges/pageInfo/cursor) |
| ID | 정수 (rid, cid) | base64 Global ID |
| 예약단위 | 주(week) + 계약 | 박(night) + 예약(reservation) |
| 보증금 | 33만 고정 엔티티 | 없음 (AirCover) |
| 위시리스트 | 단순 찜(rooms/favorites) | 날짜·게스트 컨텍스트 + 협업 |
| 결제 | 토스 단일 | 다중 PG(Adyen/Braintree) + 지역결제 |

> 새 서비스(웹 우선·REST 지향)는 **33m2식 REST + 도메인 엔티티**가 적합.
> 단 Airbnb의 **Relay 커넥션 페이지네이션**, **위시리스트 여행 컨텍스트**, **예약 상태 세분화**는 차용 가치 있음.
