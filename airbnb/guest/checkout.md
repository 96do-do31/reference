# Airbnb 체크아웃(예약·결제) 모델 — `stayCheckout`

> 출처: `/book/stays/{listingId}` 페이지의 `data-deferred-state-0` → `niobeClientData` → `stayCheckout` (57KB).
> 33m2의 `/guest/contract/request` (계약 요청) 에 대응하는 화면·모델입니다.

---

## 1. 진입 URL

```
/book/stays/{listingId}
  ?checkin=YYYY-MM-DD &checkout=YYYY-MM-DD
  &numberOfAdults &numberOfChildren &numberOfInfants &numberOfPets
  &guestCurrency=KRW &productId={listingId}
  &isWorkTrip=false
  &code={code} &orderId={orderId}      ← 진입 시 서버가 발급
```

> ⚠️ **진입 시점에 주문이 선생성**됩니다 (`orderId`, `code`). 결제 전 이탈해도 과금 없음.

---

## 2. GraphQL 입력 (`stayCheckout.input`)

```jsonc
{
  "input": {
    "productId": "<base64: StayListing:{id}>",
    "checkinDate": "2026-10-20",
    "checkoutDate": "2026-11-02",
    "guestCounts": {
      "numberOfAdults": 1, "numberOfChildren": 0,
      "numberOfInfants": 0, "numberOfPets": 0
    },
    "guestCurrencyOverride": "KRW",
    "addOn": {
      "carbonOffsetParams":  { "isSelected": false },   // 탄소 상쇄 기부
      "guestDonationParams": { "isSelected": false }    // 게스트 기부
    },
    "businessTravel": {},        // 비즈니스 출장
    "lux": {},                   // Airbnb Luxe
    "org": {},                   // 조직/법인 예약
    "listingDetail": {},
    "metadata": { "internalFlags": ["LAUNCH_LOGIN_PHONE_AUTH"] },
    "quickPayData": null
  }
}
```

> 🆕 33m2에 없는 축: **기부 애드온(탄소상쇄·기부)**, **비즈니스 출장**, **조직 예약**, **다중 통화**.

---

## 3. 응답 구조

```
presentation.stayCheckout.sections
  ├─ metadata
  ├─ sectionConfiguration
  ├─ stateMutation
  ├─ checkoutServiceContext
  └─ temporaryQuickPayData
```

### 3.1 `metadata` — 식별자 4단 ★
| 필드 | 의미 |
|---|---|
| `orderId` | 주문 (진입 시 발급) |
| `bookingAttemptId` | **예약 시도** — 재시도 추적 |
| `bookingQuoteId` | **견적** — 가격 스냅샷 |
| `confirmationCode` | 확정 코드 (예약 완료 후) |
| `misaId`, `tierId` | 내부 식별자 |
| `pageTitle`, `windowTitle`, `animationTitle` | 화면 문구 |
| `toast`, `checkoutFlowMetadata` | |

> 💡 **주문 / 시도 / 견적 / 확정**을 분리한 4단 식별자 모델. 결제 재시도와 가격 스냅샷 무결성을 위한 설계.
> 33m2는 `contractId` 하나로 처리 — 새 서비스에서는 최소 **견적 ID**는 분리할 것을 권장(가격 변동 시 분쟁 방지).

### 3.2 `stateMutation` — 사용자가 변경 가능한 상태
```
checkin · checkout
numberOfAdults · numberOfChildren · numberOfInfants · numberOfPets
messageToHost              ← 33m2의 "임대인에게 인사 메시지"와 동일 역할
isWorkTrip · tripPurpose   ← 출장 여부·여행 목적
openHomesAffiliated        ← Open Homes(재난 무료 숙박) 연계
modals
```

### 3.3 `sectionConfiguration.data` — 화면 섹션 7종
| sectionId | 타입 |
|---|---|
| `PRODUCT_DETAILS` | `CheckoutProductDetailSection` |
| `PAYMENT_PLAN_SELECTION` | `PaymentPlanSelectionSection` |
| `PAYMENT_OPTIONS` | `PaymentOptionsSection` |
| `PRICE_DETAIL` | `PriceDetailSection` |
| `TERMS_AND_CONDITIONS` | `TermsAndConditionsSection` |
| `CONFIRM_AND_PAY` | `ConfirmAndPaySection` |
| `FOOTER_BANNER` | `CheckoutFooterBannerSection` |

동반: `effects`, `stepperPlacement`, `postConfirmAndPayClick`(결제 후 처리)

---

## 4. 결제 모델 — `temporaryQuickPayData` ★

Airbnb의 **QuickPay** 결제 플랫폼.

### 4.1 `billInfo`
```
billItemProductId · billItemProductType · isBusinessTravel · productInfos
```

### 4.2 `bootstrapPayments` — 19 필드
| 필드 | 의미 |
|---|---|
| `paymentOptions` | 저장된 결제수단 목록 |
| **`paymentPlans`** | **결제 플랜 옵션** (전액 / 분할 / 후불) |
| **`paymentPlanSchedule`** | 분할 결제 스케줄 |
| `productPriceBreakdown` | 상품 요금 분해 |
| `structuredDisplayPriceBreakdown` | 표시용 요금 분해 |
| `tendersPriceBreakdown` | 결제수단별 분해 |
| `couponList` | **쿠폰** |
| `airbnbCredit` · `travelCouponCredit` | **크레딧** |
| `brazilianInstallments` · `vendorInstallments` | **할부** (지역·벤더별) |
| `fxMessage` | **환율 안내** |
| `regionalCheckoutData` | 지역별 체크아웃 규칙 |
| `quickPayConfiguration` | |
| `visiblePaymentModuleTypes` | 노출 모듈 목록 |
| `checkoutTokens` · `status` · `billData` · `pricingDisclaimer` | |

**`visiblePaymentModuleTypes` 실측값**
```
COUPON · FX_MESSAGE · PAYMENT_OPTIONS · PAYMENT_PLANS · PRODUCT_PRICE_BREAKDOWN
```

### 4.3 결제 플랜 옵션 (`paymentPlanOptions[]`)
```jsonc
{
  "localizedAmount": "₩452,640",
  "paymentPlanOption": {
    "displayString": "Pay in full",
    "depositOption": null,
    "eligibleGibralt…": …
  },
  "amountSubtitle": null, "depositInfo": null,
  "disclaimer": null, "learnMoreLink": null
}
```
UI 표기: **"지금 ₩452,640 결제"** vs **"지금 ₩0 결제"**(체크인 D-9 자동청구, 추가 수수료 없음)

### 4.4 결제 수단 (관찰)
저장 카드(AMEX) · **네이버페이** · 기타 옵션 · VISA/MC/JCB
> CSS에 `kakaopay System Sans` 폰트 토큰 존재 → **카카오페이 연동**도 있음.
> 고지: "해외에서 결제가 처리되기 때문에 카드 발행사에서 추가 수수료를 부과할 수 있습니다."

---

## 5. 33m2 계약 요청과의 대조

| 축 | 33m2 `/guest/contract/request` | Airbnb `/book/stays/{id}` |
|---|---|---|
| 식별자 | `contractId` 단일 | **orderId / bookingAttemptId / bookingQuoteId / confirmationCode** |
| 게스트 수 | ❌ 없음 | 성인·어린이·유아·반려동물 |
| 호스트 메시지 | 인사 메시지 (500자) | `messageToHost` |
| 결제 시점 | **승인 후 결제** | 즉시 or **후불(수수료 0)** |
| 결제 플랜 | 단일 | 전액/분할/후불 + 지역별 할부 |
| 쿠폰·크레딧 | ❌ | 쿠폰 + Airbnb 크레딧 + 여행 쿠폰 |
| 통화 | KRW 고정 | 다중 통화 + 환율 안내 |
| 요금 표시 | 4항목 분해 + 보증금 | 올인 총액 (내부는 다층 분해 보유) |
| 약관 동의 | 별도 화면 | 버튼 클릭 = 동의 |
| 부가 | ❌ | 탄소상쇄·기부·출장·조직예약 |
| 여행 목적 | ❌ | `isWorkTrip`, `tripPurpose` |

> 🔵 **새 서비스 시사점**
> 1. **견적 ID(`bookingQuoteId`) 분리**는 도입할 가치가 큽니다. 요금이 조회 시점과 결제 시점에 달라지는 분쟁을 막습니다.
> 2. **결제 시도(`bookingAttemptId`) 분리**로 재시도·중복결제 방어.
> 3. 33m2의 "승인 후 결제"와 Airbnb의 "후불 결제(수수료 0)"는 목적이 유사(선점) — 새 서비스는 **승인 + 결제기한 홀드** 조합이 적합해 보입니다.
