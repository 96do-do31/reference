# Airbnb 유저 플로우 · 화면 인벤토리 (앱+웹 종합)

> 출처: APK dex의 화면 클래스(1,756 Fragment/Activity/Screen) + GraphQL 오퍼레이션(1,363) + 로그인 웹/앱 UI 관찰.
> 33m2의 `flows.md`+`screens.md`에 대응.

---

## 1. 앱 정보구조 (하단 5탭) ✅ 실기기 확인

```
검색 │ 위시리스트 │ 여행 │ 메시지 │ 프로필
```
액티비티: `HomeActivity` (`feat.homescreen`). 화면은 대부분 Fragment/Screen 컴포넌트.

---

## 2. FLOW-A01 예약 (검색 → 확정) ★ 핵심 전환

```
검색 탭
  카테고리: 전체 │ 숙소 │ 체험 │ 서비스
  → StaysSearch (SearchInput: 위치·날짜·게스트·필터)
      결과: 카드 리스트 + 지도 (Relay 커넥션 페이지네이션)
      ↓ 카드 탭
PDP  (StaysPdpSections + node.pdpPresentation, 28섹션)
  BasePdpSectionsFragment / BasePdpCalendarFragment / BasePdpSubpageFragment
  예약 카드: 날짜(PdpAvailabilityCalendarQuery) · 게스트 · [예약하기]
  즉시예약(INSTANT_BOOK) → 바로 체크아웃 / 예약요청(REQUEST_TO_BOOK) → 호스트 승인
      ↓
체크아웃 (CheckoutActivity / CheckoutFlowScreen)  ← stayCheckout 쿼리
  서브스크린 (dex 확정):
   ├─ CheckoutDatePickerScreen        날짜 변경
   ├─ CheckoutAddOnScreen             부가(탄소상쇄·기부)
   ├─ CheckoutCheckInTimeScreen       체크인 시간
   ├─ CheckoutFirstMessageScreen      호스트에게 첫 메시지
   ├─ CheckoutCardOnFileScreen / AddPayPalFragment  결제수단
   ├─ CheckoutCancellationOptionsSectionFragment    취소정책 선택
   ├─ CheckoutEditAdditionalRequirementScreen       추가 요건
   ├─ CheckoutAttestationSectionFragment            (지역별 법적 확인)
   ├─ CheckoutCountdownTextFragment                 결제 마감 카운트다운
   └─ CheckoutAbandonScreen           이탈 방지
      ↓ ConfirmAndPayStaysCheckoutMutation
   CheckoutFulfillmentPlaceOrderResultFragment → 예약 확정 (confirmationCode)
```
> 식별자 4단(orderId/bookingAttemptId/bookingQuoteId/confirmationCode)은 `checkout.md` 참조.
> 결제 마감 카운트다운·이탈 방지 화면 = 전환 최적화 장치.

## 3. FLOW-A02 예약 라이프사이클 (상태 머신)

```
INQUIRY → PREAPPROVED ─┐
                        ├→ (REQUEST_TO_BOOK) PENDING → 호스트 ACCEPTED/DECLINED
NEW ────────────────────┘
(INSTANT_BOOK) → CONFIRMED → 체크인 → 체크아웃 → COMPLETED → 상호 리뷰
                    └ CANCELLED (게스트/호스트)  · AT_CHECKPOINT (에어락 검문)
```
관련 오퍼레이션: `AcceptRtbMutation` · `AcceptReservationAlterationMutation`(일정변경) · `CancelReservationThroughConfirmMutation` · `AutoConfirmPendingThirdPartyReservationMutation`
관리 화면: `ReservationDetailsScreen` · `ReservationCardsFragment` · `ReservationFiltersScreen` · `CanceledReservationScreen`

> 33m2 대비: **일정변경(Alteration)이 정식 오퍼레이션**, INQUIRY(문의)·PREAPPROVED(사전승인) 상태 존재.

## 4. FLOW-A03 상호 리뷰 ★ (33m2엔 없는 양방향)

```
COMPLETED 후:
  게스트 → 호스트/숙소 리뷰:  GuestReviewHostFlowScreen → GuestReviewHostScreen (다단계 Step)
       ActivityGuestReviewHostLoadStepQuery → ActivityGuestReviewHostStepMutation
  호스트 → 게스트 리뷰:       HostPublicReviewScreen
  공개: 양측 제출 시 또는 14일 후 (Airbnb 규칙)
프로필 노출: ContextualGuestUserProfileReviews / ContextualHostUserProfileReviews
```
카테고리 평점 6종(청결도/정확도/체크인/의사소통/위치/가격대비) — `airbnb/guest/screens-and-api.md` §5.

## 5. FLOW-A04 메시징 (인박스 동기화 프로토콜)

```
메시지 탭
  InboxSyncProtocolItemFetchQuery / NewerThanQuery / NextPageQuery / SearchQuery
  → 증분 동기화 (33m2 Firebase RDB와 다른 자체 sync 프로토콜)
스레드: GetMessagesQuery → CreateMessageMutation
  스레드 생성: CreateDirectMessageThreadMutation / CreateMessageThreadMutation
  시스템: AcceptMessageLegalDisclosureMutation (법적 고지 동의)
  고객지원 참여 (스레드에 CS 봇)
```

## 6. FLOW-A05 위시리스트

```
위시리스트 탭 (WishlistIndexPageQuery)
  '최근 조회' 자동 위시리스트 + 사용자 생성 위시리스트
  CreateWishlistMutation · AddWishlistItemMutation · CastWishlistItemVoteMutation(협업 투표)
  CreateWishlistItemNoteMutation(메모) · DeleteWishlistShareTokenMutation(공유)
  협업: currentUserRole PRIVATE_OWNER / COLLABORATOR
  날짜·게스트 컨텍스트 내장 (여행 계획화)
```

## 7. FLOW-A06 인증 (에어락 다단계 챌린지)

```
로그인/가입: 소셜(네이버·구글·애플·위챗·왓츠앱) + 이메일/전화 + 패스키
  Identify{Email,Phone,RecentUser}StepInput → 챌린지
  챌린지: {Email,Sms,Voice,WhatsApp,Password,Passkey}ChallengeStepInput
  OTP: EmailOtpChallengeStepInput / SmsOtpChallengeStepInput / VoiceOtpChallengeStepInput
에어락(Airlock): 이상거래 시 AT_CHECKPOINT → AirlockAppealsReviewAndSubmitSaveMutation
```

## 8. 호스트 플로우 (개괄)

- **리스팅 관리** (123 오퍼레이션): `ActivityListingEditor{Title,Description,VanityCode,Cover,...}` — 필드별 편집
  등록: `AddListingsScreen`, M13 셋업 플로우
- **캘린더** (53 오퍼레이션): `CalendarScreen`, `BasePriceTuneupsCalendarPluginScreen` — **날짜별 요금**
- **예약 관리**: `ReservationDetailsScreen`, RTB 승인
- **정산**: `AddPayoutMethodReviewScreen`, Payout 17 오퍼레이션
- **공동호스팅**(Cohost, 34 오퍼레이션): 위임·그룹 스레드

---

## 9. 화면 인벤토리 규모 (dex)

| 영역 | 화면 클래스 수 (대략) |
|---|---|
| 전체 Fragment/Activity/Screen | **1,756** |
| Checkout* | 40+ |
| Listing*(호스트 편집) | 100+ |
| Calendar* | 30+ |
| Reservation*/Trip* | 40+ |
| Review* | 20+ |
| Wishlist* | 15+ |

> 전체 목록이 필요하면 `_shared/captures/airbnb.graphql-operations.txt`(오퍼레이션)와
> dex 재추출로 화면 클래스 전량 확보 가능. 여기서는 클론 판단에 필요한 핵심 플로우만 정리.

---

## 10. 웹 화면 (로그인 확인)

| 경로 | 오퍼레이션 |
|---|---|
| `/` | 검색 홈 (카테고리 탭 + 지역 캐러셀) |
| `/s/{loc}/homes` | `StaysSearch` |
| `/rooms/{id}` | `StaysPdpSections` |
| `/book/stays/{id}` | `stayCheckout` |
| `/trips/v1` | `TripListQuery` + `PastTripPinsQuery` |
| `/wishlists` | `WishlistIndexPageQuery` |
| `/account-settings` | `PersonalInfoQuery` · `IsScaRequiredQuery` · `CouponPromotionQuery` |
| `/messages`(앱: 메시지탭) | `GetMessagesQuery` · `InboxSyncProtocol*` |
