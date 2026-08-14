# 관찰된 API 명세

실제 네트워크 호출과 서버 직렬화 페이로드에서 확인한 것만 기록합니다.
`✅` = 요청·응답 모두 확인 · `👁` = 요청만 확인 · `❓` = 추정

---

## A. 33m2 — REST

**Base**: `https://web.33m2.co.kr`
**인증**: Firebase Authentication (`identitytoolkit.googleapis.com`)
**네임스페이스**: `/v1/use-auth/…` (인증 컨텍스트 사용) · `/v1/no-auth/…` (비인증, 규약상 추정 ❓)

### 공통 응답 엔벨로프 ✅
```jsonc
{
  "code": "SCSS_001",     // 성공 코드. 에러 코드 체계 미확인
  "data": { /* 페이로드 */ }
}
```
페이지네이션 응답은 Spring `Page` 형태: `data.content[]` (+ page/size/totalElements 동반 추정 ❓)

---

### API-33-01 지도 매물 목록 ✅
```http
GET /v1/use-auth/map/rooms
      ?swLat={float}&swLng={float}&neLat={float}&neLng={float}
      &size={int}&page={int}
```
**응답** `data.content[]` → `ENT-004 RoomListItem`
```jsonc
{ "code":"SCSS_001", "data": { "content": [
  { "rid":4684, "roomName":"강남역 초역세권 역삼동",
    "state":"서울특별시","province":"강남구","town":"역삼동",
    "picMain":"room/{uuid}.jpeg",
    "addrLot":"…","addrStreet":"…",
    "propertyType":"원룸건물",          // ⚠️ 한글 표시명 (상세는 enum)
    "usingFee":340000, "mgmtFee":50000,
    "pyeongSize":5,
    "roomCnt":1,"bathroomCnt":1,"cookroomCnt":1,"sittingroomCnt":0,
    "recoType1":false,"recoType2":false,   // 의미 미확정
    "longtermDiscountPer":10, "earlyDiscountAmount":7,
    "isNew":false, "isSuperHost":true,
    "lat":37.50083, "lng":127.02822,
    "like":false }                          // 조회자 기준 개인화
]}}
```

### API-33-02 지도 마커 👁
```http
GET /v1/use-auth/map/markers
      ?zoomLevel={int}&swLat=&swLng=&neLat=&neLng=
```
마커와 리스트를 **별도 엔드포인트로 분리** (마커는 줌 레벨에 따른 클러스터링 추정 ❓)

### API-33-03 매물 예약 가능 일정 ✅ ★
```http
GET /v1/use-auth/rooms/{rid}/schedules?year={YYYY}&month={M}
```
```jsonc
{ "code":"SCSS_001", "data": { "schedules": [
  { "date":"2026-09-01", "status":"booking" },
  { "date":"2026-08-15", "status":"disable" }
]}}
```
| `status` | 의미 |
|---|---|
| `booking` | 기존 계약으로 점유 |
| `disable` | 임대인이 차단 |
| *(응답에 없음)* | **예약 가능** |

> ✅ 검증: `rid=4684`, 2026-09 → 미포함일 `[7,21,22,23,24,25]`가 캘린더 UI 선택 가능일과 정확히 일치.

### API-33-04 활성 계약 조회 ✅
```http
GET /v1/use-auth/guest/contracts/last-active?rid={rid}
→ { "code":"SCSS_001", "data": { "lastActiveContract": null } }
```
매물 상세 진입 시 호출 — 해당 매물에 대한 조회자의 진행 중 계약 확인용.

---

### ⚠️ 33m2 API 표면의 한계

페이지 데이터 대부분은 REST가 **아니라 Next.js RSC 플라이트 페이로드**로 전달됩니다.
`/guest/room/{rid}`, `/guest/contract`, `/host/*` 등은 서버 컴포넌트가 렌더링하므로 브라우저에서 관찰되는 REST 호출이 없습니다.

**따라서 아래는 엔드포인트가 아니라 "화면이 필요로 하는 데이터 계약"으로 문서화되어 있습니다:**
- 매물 상세 → `33m2/guest/entities.md` `ENT-001 Room` (56필드, RSC 페이로드에서 추출)
- 계약 목록/상세, 정산, 채팅 → `33m2/host/screens-and-model.md`

새 서비스 설계 시에는 이들을 명시적 REST 엔드포인트로 승격시켜야 합니다.

### 이미지 CDN 규약 ✅
```
https://d1pviohoskiraj.cloudfront.net/{scope}/{uuid}.{ext}?b=samsamm2&d={W}x{H}&v=wm
  scope : room | profile | campaign
  d     : 목표 크기 (높이 0 = 비율 유지, 예: 720x0)
  v=wm  : 워터마크
  관찰된 프리셋: 240x240, 360x240, 480x480, 720x0, 720x480
```

---

## B. Airbnb — GraphQL

**Base**: `https://www.airbnb.co.kr`
**엔드포인트**: `/api/v3/{OperationName}/{sha256PersistedQueryHash}`
**초기 데이터**: `<script id="data-deferred-state-0" type="application/json">` → `niobeClientData: [[ "{Op}:{varsJson}", { data } ]]`

### API-AB-01 StaysSearch ✅
```jsonc
// variables
{
  "staysSearchRequest": {
    "requestedPageType": "STAYS_SEARCH",
    "metadataOnly": false,
    "maxMapItems": 9999,
    "rawParams": [                                   // ★ 제네릭 필터 백
      {"filterName":"adults",          "filterValues":["1"]},
      {"filterName":"checkin",         "filterValues":["2026-10-20"]},
      {"filterName":"checkout",        "filterValues":["2026-11-02"]},
      {"filterName":"query",           "filterValues":["Seoul, South Korea"]},
      {"filterName":"refinementPaths", "filterValues":["/homes"]},
      {"filterName":"itemsPerGrid",    "filterValues":["18"]},
      {"filterName":"screenSize",      "filterValues":["large"]},
      {"filterName":"tabId",           "filterValues":["home_tab"]},
      {"filterName":"cdnCacheSafe",    "filterValues":["false"]},
      {"filterName":"version",         "filterValues":["1.8.8"]}
    ],
    "treatmentFlags": [ /* 실험 플래그 11개 */ ]
  },
  "staysMapSearchRequestV2": { /* 지도용 별도 요청 */ },
  "aiSearchEnabled": false,
  "isLeanTreatment": false
}
```
**응답**: `data.presentation.staysSearch.{ results, mapResults }`
`results.{ searchResults[18], paginationInfo, filters, searchInput, seo, pricingDisclaimer, pricingToggle, sectionConfiguration, staysSearchAnnouncements }`

**페이지네이션**: `paginationInfo.pageCursors[]`, 각 커서 = base64(`{"section_offset":0,"items_offset":18,"version":1}`)

**`searchResults[]` 요소 = `StaySearchResult`** (프레젠테이션 지향)
```
avgRatingA11yLabel · avgRatingLocalized · title · subtitle · nameLocalized
structuredDisplayPrice · structuredContent · badges · paymentMessages
contextualPictures[] · listingParamOverrides · demandStayListing.id(base64)
propertyId · passportData · priceBreakdownMessages
```
`structuredDisplayPrice.explanationData.priceDetails[].items[]` = `{description, priceString, originalPriceString}`
예: `{"description":"13박 x ₩37,846","priceString":"₩492,000"}`, `{"description":"주 단위 숙박 할인","priceString":"-₩39,360"}`

### API-AB-02 StaysPdpSections ✅
```
GET /rooms/{listingId}?check_in&check_out&adults
→ data.presentation.stayProductDetailPage.sections.sections[] (28개)
```
**섹션 ID 전체** — `airbnb/guest/screens-and-api.md` §5 참조
`POLICIES_DEFAULT` 필드: `cancellationPolicyForDisplay, houseRules, houseRulesSections, additionalHouseRules, listingExpectations, safetyExpectationsAndAmenities, safetyAndPropertiesSections, importantInformationContent, propertyLicenseTextList, businessDetails, cleaningModal`

### API-AB-03 체크아웃 👁
```
GET /book/stays/{listingId}
      ?checkin&checkout
      &numberOfAdults&numberOfChildren&numberOfInfants&numberOfPets
      &guestCurrency=KRW&productId&isWorkTrip=false
      &code={code}&orderId={orderId}
```
> **진입 시 `orderId` 선발급** (주문 선생성 후 결제). 이탈해도 과금 없음.

---

## C. 새 서비스 API 설계 권장

| 항목 | 권장 | 근거 |
|---|---|---|
| 스타일 | **REST + 도메인 엔티티** | 33m2식. 클라이언트가 도메인을 알아야 계산·검증 가능 |
| 금액 | **서버가 계산된 금액까지 반환** | 33m2 `longTermDiscounts[].discountedUsingFee` 선례 — 클라 계산 불일치 방지 |
| 필터 | **제네릭 `rawParams[{name, values[]}]`** | Airbnb식. 스키마 변경 없이 필터 추가 |
| 페이지네이션 | **커서** | Airbnb식. 목록 변동 중에도 안정 |
| 엔벨로프 | `{ code, data }` 유지 | 33m2식이 에러 코드 체계와 잘 맞음 |
| 가용 일정 | **점유일만 반환**(`booking`/`blocked`), 미포함 = 가용 | 33m2식. 페이로드 절약 |
| 이미지 | CDN 온더플라이 리사이즈 `?d={W}x{H}` | 33m2식 |
| 인증 | 비로그인 열람 허용, 쓰기만 게이트 | Airbnb식 (SEO) |
