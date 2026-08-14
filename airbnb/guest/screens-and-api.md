# Airbnb (airbnb.co.kr) — 게스트 화면·API 역설계

> 관찰: 2026-08-14, **비로그인 상태** 기준. 예약·메시지·여행·위시리스트는 로그인 후 추가 조사 필요.

## 1. 아키텍처

| 레이어 | 내용 |
|---|---|
| API | **GraphQL** — `POST/GET /api/v3/{OperationName}/{sha256hash}` |
| 초기 데이터 | `<script id="data-deferred-state-0" type="application/json">` 안에 `niobeClientData: [[ "Op:{vars}", {data:…} ]]` 형태로 GraphQL 응답 캐시 임베드 |
| 렌더링 | SSR + 하이드레이션. 필터 변경은 **전체 페이지 내비게이션** (URL이 곧 검색 상태) |
| 페이지 구성 | **섹션 기반 컴포저블 아키텍처** — 서버가 타입 지정된 섹션의 순서 배열을 반환, 클라이언트가 렌더 |
| 통화/로케일 | `KRW`, `ko` — 헤더에서 전환 |

### ★ 결정적 설계 차이: 프레젠테이션 지향 API

Airbnb의 GraphQL은 **도메인 엔티티가 아니라 UI 조립 완료 형태**를 반환합니다.

```jsonc
// 검색 결과 1건 (StaySearchResult)
{
  "avgRatingA11yLabel": "평점 4.75점(5점 만점), 후기 24개",  // 접근성 문구까지 서버 생성
  "avgRatingLocalized": "4.75 (24)",
  "title": "서울의 아파트",          // 타입+도시 조합 표시명
  "subtitle": "낙성대역3분거리 역세권숙소 207",
  "structuredDisplayPrice": { "primaryLine": {...}, "explanationData": {...} },
  "badges": [], "paymentMessages": [], "structuredContent": {...},
  "contextualPictures": [ … 6 ],
  "demandStayListing": { "id": "<base64: DemandStayListing:{listingId}>" }
}
```

> 33m2는 `{rid, roomName, usingFee, mgmtFee, …}` 도메인 필드를 주고 클라이언트가 조립.
> Airbnb는 `"13박 x ₩37,846"` 같은 **문자열까지 서버가 생성**.
> ⇒ Airbnb 방식은 A/B 테스트·다국어·플랫폼별 UI 변경을 서버 배포만으로 가능. 대신 클라이언트가 도메인을 모름.

---

## 2. 라우트

| 경로 | 화면 |
|---|---|
| `/` | 홈 — 탭(전체/숙소/체험/서비스) + 검색바 + 추천 캐러셀 |
| `/s/{location}/homes?checkin&checkout&adults&…` | 검색 결과 |
| `/rooms/{listingId}?check_in&check_out&adults` | 숙소 상세 (PDP) |
| `/book/stays/{listingId}` (추정) | 예약/결제 — 로그인 필요, 미확인 |
| `/wishlists`, `/trips`, `/messages`, `/account-settings` | 로그인 필요, 미확인 |
| `/hosting/*` | 호스팅 대시보드, 미확인 |

### 검색 URL 파라미터 (관찰)
```
checkin, checkout, adults, children, infants, pets
query, place_id, refinement_paths[]=/homes
room_types[]=Entire home/apt
price_filter_input_type, price_filter_num_nights
flexible_trip_lengths[]=one_week
monthly_start_date, monthly_length, monthly_end_date   ← 월 단위 체류 모드
search_mode=regular_search | flex_maybe_within_a_week
search_type=filter_change | autocomplete_click | pagination
channel=EXPLORE, tab_id=home_tab
```

### StaysSearch GraphQL 요청 형태
```jsonc
{
  "staysSearchRequest": {
    "requestedPageType": "STAYS_SEARCH",
    "metadataOnly": false,
    "maxMapItems": 9999,
    "rawParams": [                       // 제네릭 필터 백
      {"filterName":"adults","filterValues":["1"]},
      {"filterName":"checkin","filterValues":["2026-10-20"]},
      {"filterName":"checkout","filterValues":["2026-11-02"]},
      {"filterName":"query","filterValues":["Seoul, South Korea"]},
      {"filterName":"refinementPaths","filterValues":["/homes"]},
      {"filterName":"itemsPerGrid","filterValues":["18"]},
      {"filterName":"screenSize","filterValues":["large"]},
      {"filterName":"tabId","filterValues":["home_tab"]},
      {"filterName":"cdnCacheSafe","filterValues":["false"]},
      {"filterName":"version","filterValues":["1.8.8"]}
    ],
    "treatmentFlags": [ … 11 ]           // 실험 플래그
  },
  "staysMapSearchRequestV2": { … },      // 지도용 별도 요청
  "aiSearchEnabled": false,
  "isLeanTreatment": false
}
```

**응답**: `data.presentation.staysSearch.{results, mapResults}`
`results.{searchResults[18], paginationInfo, filters, searchInput, seo, pricingDisclaimer, pricingToggle, sectionConfiguration, staysSearchAnnouncements}`

**페이지네이션**: 커서 방식 — `pageCursors[]`, 각 커서는 base64 `{"section_offset":0,"items_offset":18,"version":1}`. 15페이지 관찰.

> 💡 `rawParams` 제네릭 필터 백 설계 — 새 필터를 스키마 변경 없이 추가 가능. 우리 서비스에서 차용할 만함.

---

## 3. SCR-A01 홈 `/`

- 헤더: 로고 / **탭 4종: 전체 · 숙소 · 체험 · 서비스** / 검색 / 호스팅 하기 / 언어·통화 / 메뉴
- 검색바: `여행지 | 날짜 | 여행자` + 검색 버튼
- 본문: 지역별 추천 캐러셀 ("부산의 인기 숙소", "다음 여행을 위한 훌륭한 호텔", "다음 달에 예약 가능한 오사카 숙소")
- 카드: 이미지 캐러셀 · 찜 하트 · `게스트 선호` 배지 · 제목 · 날짜 · **총액 ₩X** · ★평점
- 메뉴(비로그인): 도움말 센터 / 호스팅 하기 / 호스트 추천하기 / 공동 호스트 찾기 / **로그인 또는 회원 가입**

## 4. SCR-A02 검색 결과 `/s/…/homes`

**레이아웃**: 좌측 카드 리스트(2열 스크롤) + 우측 지도 (고정)

**퀵 필터 바**: `[필터]` · `지역·장소 선택 ▾` · 칩(집 전체, 세탁기, 에어컨, 와이파이, 게스트 선호, 주방, 한정 시간 무료 취소, 건조기, 셀프 체크인, TV)

**결과 헤더**: "숙소 1,000개 이상"

**카드 구성**
```
[이미지 캐러셀 · 도트] [♡]  [게스트 선호|슈퍼호스트|신규 배지]
서울의 아파트                                   ★ 4.75 (24)
낙성대역3분거리 역세권숙소 207
침실 1개 · 침대 1개 · 욕실 1개
[게스트 한마디 "호스트가 너무 친절하고"]         ← 리뷰 스니펫 (일부 카드)
총액 ~~₩1,219,467~~ ₩859,589   [요금 내역 표시]
[주간 할인] [오늘 ₩0 결제] [취소 수수료 없음]
```

**관찰된 배지 어휘**: `게스트 선호`, `상위 게스트 선호`, `슈퍼호스트`, `신규 숙소/신규`, `주간 할인`, `오늘 ₩0 결제`, `취소 수수료 없음`

**특수 섹션**: `비슷한 날짜에 예약 가능`(대체 날짜 캐러셀, 페이지 인디케이터), `선택하신 날짜에 예약 가능한 더 많은 숙소`

### 필터 패널 (전체 목록)

| 섹션 | 내용 |
|---|---|
| 선택된 필터 | 제거 가능 칩 |
| 추천 필터 | 세탁기 / 취소 수수료 없음 / 욕실 1개 이상 / 주방 |
| **숙소 유형** | 모든 유형 · 방 · 집 전체 |
| **가격 범위** | **분포 히스토그램** + 최저/최고 입력 — *"여행 요금, 모든 수수료 포함"* |
| **침실과 침대** | 침실 / 침대 / 욕실 스테퍼 (상관없음~) |
| **편의시설** | 와이파이 · 에어컨 · 건조기 · 헤어드라이어 · 난방 · TV + [더 표시] |
| **인기 지역** | 명동 · 강남구 · 종로구 · 마포구 + [더 표시] |
| **예약 옵션** | 즉시 예약 · 셀프 체크인 · 취소 수수료 없음 · 반려동물 동반 가능 |
| **돋보이는 숙소** | 게스트 선호 / Luxe |
| 건물 유형 | (접힘) |
| 접근성 편의 | (접힘) |
| 호스트 언어 | (접힘) |
| 푸터 | [전체 해제] · **[집 전체 숙소 1,000개 이상 표시]** ← 실시간 결과 수 |

> 💡 **가격 히스토그램**, **실시간 결과 수 반영 CTA**, **인기 지역(하위 지역) 필터** 는 33m2에 없는 강점.

---

## 5. SCR-A03 숙소 상세 (PDP) `/rooms/{id}` ★

### 서버가 내려주는 섹션 목록 (28종, 정확한 ID)

```
HERO_DEFAULT              TITLE_DEFAULT             OVERVIEW_DEFAULT_V2
GUEST_FAVORITE_BANNER     MESSAGE_BANNER            HIGHLIGHTS_COMPACT
HOST_OVERVIEW_DEFAULT     DESCRIPTION_DEFAULT       LOCATION_DEFAULT
AMENITIES_DEFAULT         AVAILABILITY_CALENDAR_INLINE
AVAILABILITY_CALENDAR_DEFAULT                       REVIEWS_DEFAULT
MEET_YOUR_HOST            POLICIES_DEFAULT          SIMILAR_LISTINGS_CAROUSEL
SEO_LINKS_DEFAULT         REPORT_TO_AIRBNB          NAV_DEFAULT / NAV_MOBILE
BOOK_IT_SIDEBAR           BOOK_IT_NAV               BOOK_IT_FLOATING_FOOTER
BOOK_IT_CALENDAR_SHEET    DESCRIPTION_MODAL         PHOTO_TOUR_SCROLLABLE_MODAL
CANCELLATION_POLICY_PICKER_MODAL                    WHAT_COUNTS_AS_A_PET_MODAL
```

> `CANCELLATION_POLICY_PICKER_MODAL` — **게스트가 취소 정책을 선택**(환불형 vs 비환불 할인가)할 수 있는 구조. 33m2는 호스트가 정한 정책 고정.

### 화면 구성

**상단**: 제목 · [공유하기] [저장] · 사진 그리드(1대형+4소형) · [사진 모두 보기]

**개요**: `한국의 임대 호실 전체` / `최대 인원 1명 · 침실 1개 · 침대 1개 · 욕실 1개` / ★4.75 · 후기 24개

**하이라이트(HIGHLIGHTS_COMPACT)**: 낙성대역 근처 · 셀프 체크인 · 무료 주차 공간 · 에어컨 · 세탁기 · 주방

**호스트 요약**: 호스트: 필용 님 / 호스팅 경력 2년

**설명** + [더 보기] → DESCRIPTION_MODAL

**위치**: 지도 + 지역명 (정확 주소 비공개)

**숙소 편의시설**: 2열 아이콘 목록, 미보유 항목은 **취소선**(예: ~~일산화탄소 경보기~~) + [편의시설 18개 모두 보기]
> 💡 33m2의 `missingOptions`와 같은 발상을 **취소선 UI**로 표현.

**예약 가능 여부(캘린더)**: "서울, 한국에서 13박" + 2개월 캘린더 + 선택 범위 하이라이트 + [날짜 지우기]

**후기 (REVIEWS_DEFAULT)** ★ 33m2 대비 강점
- ★4.75 · 후기 24개 + [후기 운영 방식]
- **전체 평점 분포 히스토그램** (5→1)
- **6개 카테고리 평점**: 청결도 4.8 · 정확도 4.9 · 체크인 5.0 · 의사소통 4.8 · 위치 4.9 · 가격 대비 만족도 4.8
- **리뷰 태그 칩 + 카운트** (가로 스크롤): 교통 편의성 9 · 나홀로 여행 2 · 인근 시설 6 · 가격 대비 만족 8 · 위치 6 · 욕실 4 · 편안함 4 · 청결 4 · 친절한 환대 6
- 리뷰 카드: 아바타 · 이름 · **에어비앤비 가입 기간**(1개월/5년/8개월) 또는 거주지 · 별점 · 상대 날짜("2주 전") 또는 연월 · 본문 + [더 보기]

**호스트 소개 (MEET_YOUR_HOST)**
- 카드: 아바타(인증 배지) · 이름 · "호스트" · **후기 450개 · 평점 4.67★ · 호스팅 경력 2년**
- **공동 호스트** 목록
- 호스트 상세 정보: **응답률 99% · 1시간 이내에 응답**
- [호스트에게 메시지 보내기]
- 경고문: "안전한 결제를 위해 항상 에어비앤비를 통해 송금하고 호스트와 소통하세요."

**알아두어야 할 사항 (POLICIES_DEFAULT)** — 3열
| 환불 정책 | 숙소 이용규칙 | 안전 및 공간 |
|---|---|---|
| "10월 19일 전까지 무료 취소가 가능합니다. 10월 20일 체크인 전에 취소하면 부분 환불을 받으실 수 있습니다." | 체크인 오후 3:00~10:00 / 체크아웃 오전 11:00 전까지 / 게스트 정원 1명 | 일산화탄소 경보기 정보 없음 / 부지 내 실외 보안 카메라 / 화재경보기 |

POLICIES_DEFAULT 데이터 필드: `cancellationPolicyForDisplay, houseRules, houseRulesSections, additionalHouseRules, listingExpectations, safetyExpectationsAndAmenities, safetyAndPropertiesSections, importantInformationContent, propertyLicenseTextList, businessDetails, cleaningModal`

**하단**: 비슷한 숙소 캐러셀 · 브레드크럼 · SEO 링크(인근 지역, 다른 유형 — **"서울의 장기 숙박 숙소"** 카테고리 존재)

### 예약 카드 (BOOK_IT_SIDEBAR)

```
🏠 흔치 않은 기회 이 숙소는 보통 예약이 가득 차 있습니다   ← 희소성 메시지
총액 ₩452,640
┌ 체크인 2026. 10. 20. ┬ 체크아웃 2026. 11. 2. ┐
└ 인원  게스트 1명                      ▾ ┘
오늘 ₩0 · 10월 19일 전까지 무료 취소 가능
        [ 예약하기 ]
예약 확정 전에는 요금이 청구되지 않습니다.
```

### 요금 계산 (검색 응답 `explanationData`)
```
13박 x ₩37,846        ₩492,000
주 단위 숙박 할인        -₩39,360      (-8%)
───────────────────────────────
총액                   ₩452,640
```
> 필터 패널에 *"여행 요금, 모든 수수료 포함"* 명시 → 표시 총액에 서비스 수수료 포함.
> 체크아웃 단계의 세부 항목(청소비·서비스 수수료·세금) 은 **로그인 후 확인 필요**.

---

## 6. 33m2와의 즉시 대비되는 차이 (예비 메모)

| 항목 | 33m2 | Airbnb |
|---|---|---|
| 기간 단위 | **주 단위** (1~12주) | **박 단위** (임의 범위) |
| 날짜 선택 | 입주일 → 기간(주) 2단계 | 체크인/체크아웃 범위 |
| **게스트 인원** | ❌ 개념 없음 | ✅ 성인/어린이/유아/반려동물 |
| 결제 시점 | 승인 후 결제 | 예약 시 결제 (오늘 ₩0 분할 옵션) |
| 즉시 예약 | ❌ 항상 승인 필요 | ✅ 즉시 예약 필터 |
| 취소 정책 | 호스트가 3택 프리셋 | 호스트 설정 + **게스트가 선택 가능** |
| 리뷰 | 총점 + 태그 | 총점 + **6카테고리** + 히스토그램 + 태그 |
| 호스트 지표 | 우수임대인, 평점, 후기수, 경력 | + **응답률·응답시간**, 공동호스트 |
| 보증금 | 33만원 고정 에스크로 | ❌ 없음 (손해배상은 AirCover) |
| 가격 필터 | 단순 범위 | **분포 히스토그램** |
| 지역 필터 | 지도 bbox | bbox + **인기 지역(행정동) 칩** |
| 다이나믹 프라이싱 | ❌ | ✅ 날짜별 요금 |

---

---

## 7. SCR-A04 확인 및 결제 (체크아웃) ★ — 로그인 확인

`/book/stays/{listingId}?checkin&checkout&numberOfAdults&numberOfChildren&numberOfInfants&numberOfPets&guestCurrency&productId&isWorkTrip&code={code}&orderId={orderId}`

> ⚠️ **체크아웃 진입 시점에 `orderId`가 발급**됨 (주문 선생성). 결제 전 이탈해도 과금 없음.
> 게스트 구성이 URL 파라미터로 분해됨: 성인/어린이/유아/**반려동물** 각각 별도 카운트.

### 좌측 — 결제

**결제 시기 선택** (핵심 차별 기능)
| 옵션 | 내용 |
|---|---|
| 지금 ₩452,640 결제 | 즉시 전액 |
| **지금 ₩0 결제** | "10월 11일에 ₩452,640의 금액이 청구됩니다. **추가 수수료는 없습니다.**" |

> 💡 체크인 약 9일 전 자동 청구. **수수료 없는 후불 예약** — 33m2의 "승인 후 결제"와 목적은 비슷하나(선점), Airbnb는 즉시 확정 + 결제만 연기.

**결제 수단**: 저장된 카드(AMEX ••4852) · **네이버페이** · [기타 옵션] · VISA/MC/JCB
- 고지: "해외에서 결제가 처리되기 때문에 카드 발행사에서 추가 수수료를 부과할 수 있습니다."

**약관 동의**: 별도 체크박스 없이 **버튼 클릭이 곧 동의** ("버튼을 선택하면 예약 약관 및 개정된 이용 약관에 동의하시는 것입니다")

**[확인 및 결제]** ← 최종 확정 버튼 (미실행)

### 우측 — 예약 요약

```
🏠 흔치 않은 기회! 이 숙소는 보통 예약이 가득 차 있습니다
[썸네일] 낙성대역3분거리 역세권숙소 207   ★4.75(후기 24개)

취소 수수료 없음
10월 19일까지 예약을 취소하면 요금 전액이 환불됩니다.  [환불 정책 전문]

날짜   2026년 10월 20일 ~ 11월 2일          [변경]
게스트  성인 1명                            [변경]

요금 세부 정보
  13박 x ₩37,846                    ₩492,000
  주 단위 숙박 할인                    -₩39,360
  ─────────────────────────────────────────
  총액 KRW                          ₩452,640
[요금 상세 내역]
```

### ★ 요금 구조: 올인(All-in) 가격

「요금 상세 내역」 모달을 열어도 **동일한 2줄뿐**입니다:
```
13박 · 10월 20일 ~ 11월 2일     ₩492,000
주 단위 숙박 할인                 -₩39,360
총액 KRW                        ₩452,640
```

**청소비·서비스 수수료·세금이 별도 항목으로 없습니다.**
→ Airbnb 한국은 게스트 서비스 수수료를 **1박 요금에 내재화한 올인 가격**(호스트 부담 수수료 모델)을 사용.
→ 검색 필터의 *"여행 요금, 모든 수수료 포함"* 문구와 일치.

> 🔀 **새 서비스 결정 지점**: 33m2식 **항목 분해**(임대료/관리비/청소비/수수료 — 투명하지만 복잡, 총액 체감 상승) vs Airbnb식 **올인 단일가**(단순하지만 불투명, 비교 용이).

---

## 8. SCR-A05 여행 `/trips` → `/trips/v1/{tripId}`

목록: 썸네일 · 지역명 · 날짜 범위 · 동행자 아바타(+N)

상세 (좌측 패널 + 우측 지도):
- 숙소 카드: 호스트명 · 날짜 · [리스팅 공유]
- **타임라인 항목**: `체크인 (일 27) 오후 3:00 이후` / `체크아웃 (월 28) 오전 11:00 이전`
- 목적지 스탬프 배지 (서울 KR)
- 우측: **Google 지도** + `대중교통` / `명소` 토글 + [지도에서 검색]

> 💡 여행 탭이 **여행 플래너**로 확장됨 — 공유 일정표, 저장한 장소를 지도에 표시, 동행자와 일정 공유.
> 33m2의 `/guest/contract`(순수 계약 목록)와 성격이 완전히 다름.

## 9. SCR-A06 메시지 `/guest/inbox` → `/guest/messages/{threadId}`

- 좌측: 검색 · 설정(⚙) · 필터 `전체 ▾` · `읽지 않음` 토글 · 스레드 목록 · **[이전 대화]** (아카이브)
- 우측: 스레드 헤더 · 날짜 구분선 · 시각 표시 말풍선
- **시스템 메시지에 액션 카드 임베드**:
  ```
  [에어비앤비 고객지원 팀]
  Jung-gu 숙소 체크인 과정이 원활하게 이뤄졌기를 바랍니다!
  숙박 기간 동안 도움이 필요하면 호스트 Stay G 님에게 연락하실 수 있지만…
    › Host G 님에게 메시지 보내기
    › 에어비앤비에 도움 요청
  ```
- 안내: 안전·고객지원·서비스 개선을 위해 **메시지를 분석**함을 고지

> 💡 **고객지원팀이 스레드 참여자**이고, 메시지에 CTA를 붙일 수 있는 구조.
> 33m2 채팅(게스트↔호스트 1:1, 계약 단위)보다 확장성 높음.

## 10. SCR-A07 위시리스트 `/wishlists`

- 그리드 카드(2×2 사진 모자이크) · 이름 · 갱신 시점
- **`최근 조회`가 자동 생성 위시리스트로 존재** — "둘러보신 숙소, 체험, 서비스는 나중에 다시 확인하실 수 있도록 자동으로 저장됩니다."

## 11. SCR-A08 계정 관리 `/account-settings`

**사이드바 (전체)**
```
개인 정보 · 로그인 및 보안 · 개인정보 보호 · 알림 · 세금
결제 및 대금 수령 · 언어 및 통화 · 예약 대행 권한 [NEW] · 출장
전문 호스팅 도구
```

**개인 정보 필드**: 실명 · 선호하는 이름 · 이메일 주소(+인증 배너) · 전화번호 · **본인 인증(인증됨)** · 거주지 주소 · 우편 주소

> `예약 대행 권한`(타인 대신 예약), `출장`(비즈니스 트래블), `세금`(호스트 세무) — 33m2에 없는 축.

---

## 12. Airbnb 호스트 모드 — 접근 상태

- `/hosting`, `/hosting/listings` 접근 가능. 상단 탭: **투데이 · 달력 · 리스팅 · 메시지**
- ⚠️ 이 계정에는 **등록 숙소 0건** → 투데이/달력/리스팅 모두 빈 상태
- ⚠️ 호스팅 진입 시 **「변경된 약관 및 정책 확인하기」 차단 모달** (동의 / 동의하지 않음) — 실계정 법적 동의라 대리 처리하지 않음
- ✅ **리스팅 등록 위저드는 모달 없이 진입 가능**: `/become-a-host` → `/become-a-host/address`
  - 1단계가 **주소 입력** (2025 개편판; 과거 "숙소 유형 먼저" 흐름과 다름)
  - 분기 링크: "숙소를 등록하지 않으시나요? **체험이나 서비스**를 호스팅하세요."

## 미확인 잔여

- [ ] 리스팅 등록 위저드 2단계 이후 (초안 생성 필요)
- [ ] 호스트 달력 — **날짜별 요금 설정**, 최소/최대 숙박일, 리드타임
- [ ] 호스트 예약 관리 · 수익/정산 · 호스트 수수료율
- [ ] 즉시 예약 vs 예약 요청 설정
- [ ] 리뷰 작성 플로우 (상호 리뷰, 14일 공개 규칙)
- [ ] AirCover 상세
- [ ] 체험·서비스 탭
