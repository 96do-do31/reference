# 모바일 앱 역설계 — 33m2 · Airbnb (Android)

> 실기기 관찰: Galaxy `SM-S948N`, Android 16, **1080×2340 / density 450 (= 360×780 dp)**
> 방법: `adb uiautomator dump` (뷰 트리 + resource-id + bounds) + `screencap`
> 원본: `_shared/captures/mobile/*.xml`, `*.png`

**2차 앱 런칭의 직접 참조 자료입니다.**

---

## 0. 두 앱의 성격

| | 33m2 (`com.samsamm2.mobileapp`) | Airbnb (`com.airbnb.android`) |
|---|---|---|
| 구현 | **네이티브 Android** (Android View 계층) | 하이브리드/선언형 (`View`/`Button` 래핑, 접근성 라벨 중심) |
| 액티비티 | 단일 `MainTabActivity` | `feat.homescreen.HomeActivity` |
| resource-id | ✅ 노출 (`hostHomeScrollView`, `usingCountTextView` …) | ❌ 거의 없음 |
| 지도 | **`WebView#mapWebView`** (지도만 웹뷰) | `TextureView` (네이티브 Google 지도) |
| 접근성 라벨 | 개별 요소 | **카드 전체를 한 문장으로** ("게스트 선호. 부산의 집. 10월 16일~18일. 총액 ₩698,000. 평점 5.0점(5점 만점).") |

> 💡 Airbnb의 접근성 라벨이 서버 생성 문자열(`avgRatingA11yLabel`)과 동일 — **웹·앱이 같은 프레젠테이션 API를 공유**합니다.
> 33m2는 앱이 별도 네이티브 구현이라 **웹/앱 각각 UI를 만들어야 하는 구조**입니다.

---

## 1. 정보구조(IA) — 하단 탭 ★

### 33m2 — 모드별로 탭이 바뀜
```
임차인 모드:  홈 │ 지도   │ 계약 │ 채팅 │ 마이
임대인 모드:  홈 │ 방 관리 │ 계약 │ 채팅 │ 마이
                  ↑ 2번 탭만 교체
```

### Airbnb — 고정 5탭
```
검색 │ 위시리스트 │ 여행 │ 메시지 │ 프로필
```

### 웹과의 대조
| | 33m2 웹 | 33m2 앱 | Airbnb 웹 | Airbnb 앱 |
|---|---|---|---|---|
| 내비 | 헤더 3개(지도/계약/채팅) + 계정 드롭다운 | **하단 5탭** | 카테고리 탭 + 햄버거 | **하단 5탭** |
| 홈 | 별도 라우트 | **탭으로 승격** | 검색 중심 | 검색 탭 |
| 마이 | 드롭다운 메뉴 | **탭으로 승격** | 햄버거 | 프로필 탭 |
| 위시리스트/찜 | 계정 메뉴 하위 | 헤더 아이콘 | 햄버거 | **탭으로 승격** |

> ⭐ **새 서비스 앱 설계 시**: 33m2식 "모드에 따라 탭 하나만 교체"는 임대인/임차인 겸업 사용자에게 자연스럽습니다.
> 다만 **모드 전환이 마이 탭 최하단**에 숨어 있어 발견성이 낮습니다(개선 여지).

---

## 2. 33m2 앱 화면 인벤토리

### 2.1 임대인 홈 (`hostHomeScrollView`)
웹 대시보드와 **동일 위젯 구성**:
```
[알림 벨]
할 일         — 승인대기(contractApproveReadyCountLayout) · 퇴실 점검(exitCheckCountLayout)
              + "23:44 기준" + 새로고침(todoRefreshLayout)
정산 예정 임대료 — 총 N건 / N원 (settlementTotalCountLayout)
계약 현황      — 계약대기 · 입주대기 · 거주중 · 퇴실중
              (contractReadyCount / enterReadyCount / usingCount / exitIngCount)
운영 팁 콘텐츠 — 이용 가이드 카드 리스트 + [전체 콘텐츠 보기]
```

### 2.2 방 관리 (`방 관리` 탭)
```
타이틀 "방 관리"
[전체보기 ▾ (typeLayout)]  [주소, 방 이름을 검색해 주세요 (roomSearchEditText)]
매물 카드:
  roomStateTextView "공개" · roomMoreImageView(⋮) · roomNameTextView · roomAddressTextView
  usingFeeTextView "360,000원" / "1주"
  [수정하기 (editTextView)]  [일정 관리하기 (manageScheduleLayout)]
[방 등록하기] ← Extended FAB (registRoomEFAB, 우하단)
```
> 웹은 헤더 버튼, **앱은 FAB**.

### 2.3 방 등록 위저드 ★ (웹에서 못 뽑았던 것)
```
헤더: [←] "방 등록하기"
스테퍼: ①공간 ②임대료 ③옵션 ④방 설명 ⑤일정   (수정 위저드와 동일 5단계)

1단계 "주소를 입력해 주세요 1/5"
  ⚠️ "주소는 수정이 불가능하니 정확히 입력해 주세요."
  주소      [주소를 검색해 주세요]          ← 검색형 입력
  층수      [층수를 선택해 주세요 ▾]
  상세 주소  "상세주소는 계약이 확정된 후 공개됩니다."
            placeholder: "예) 101동 302호, 2층 전체 사용"
  [다음으로 (blackButton)]

이탈 시 다이얼로그:
  "방 등록을 중단하고 나가시겠습니까? / 작성 중인 내용은 저장되지 않습니다."
  [나가기] [계속 작성하기]
```
> ✅ **신규 등록 = 수정 위저드 + 주소 입력**. 이후 2~5단계는 수정 위저드와 동일
> (`33m2/host/screens-and-model.md` §SCR-H03).

### 2.4 계약 탭 (임대인)
```
타이틀 "계약"
카운트 타일 4: 승인대기 · 입주예정 · 퇴실예정 · 퇴실점검
[검색 (searchButtonTextView)]
상태 탭 (HorizontalScrollView, 가로 스크롤):
  전체 │ 계약대기 │ 입주대기 │ 거주중 │ 퇴실중 │ 계약종료 │ …
정렬 [최신순 ▾ (sortLayout)]
계약 목록 (contractListRecyclerView):
  statusTextView(상태 배지) · roomNameTextView · buttonChatImageView · 주소 · 기간 · 금액
```
> 웹의 상태 칩 8종(+취소/결제취소)이 앱에서는 **가로 스크롤 탭**으로 압축.

### 2.5 마이 탭 (계정 IA)
```
프로필: 아바타 · 닉네임 · [임대인] 모드 배지(loginModeTextView) · 이메일 · [본인인증 완료] 배지
─ 관리      정산(payoutInfoLayout) · 후기 관리(landlordManageReviewLayout)
─ 설정      계정 정보 · 알림 설정 · **언어 설정(languageSettingLayout)**
─ 고객 지원  자주 묻는 질문 · 고객 센터
─ 소식·혜택  이벤트/제휴 · 삼삼엠투 단기임대 이야기 · 공지사항
[임차인 모드로 전환 (modeChangeTextView)]
[로그아웃 (logoutTextView)]
```
> 웹 계정 드롭다운과 항목이 거의 같되 **언어 설정**이 앱에만 별도 메뉴로 존재(웹은 헤더 `KR` 셀렉터).

### 2.6 임차인 홈 (`guestHomeScrollView`)
```
헤더: [찜(favoriteLayout)] [알림(alarmListLayout)]
"삼삼엠투에서 / 잠깐 살 집을 찾아보세요"
[검색바] ← ★ 동적 플레이스홀더: "제주도 단독주택을 찾으시나요?"
매물 유형 모자이크 그리드 (크기 불균등 매거진 레이아웃):
  원룸 / 투룸 / 오피스텔[인기 배지] / 쓰리룸+ / 아파트   각각 제목+2줄 설명
[원하는 지역의 집을 지도로 찾아보세요]
```
> 웹은 **가로 캐러셀**, 앱은 **모자이크 그리드**. 검색 플레이스홀더가 앱에서 동적으로 바뀜.

### 2.7 지도 탭 ★ 모바일 고유 패턴
```
상단: [지역, 지하철 검색 (keywordTextView)]  [일정 (chooseDateTextView)]
지도: WebView#mapWebView (전체 화면)
바텀시트 (bottomSheet + bottomSheetHandleLayout):
  [필터 아이콘] + 가로 스크롤 칩:
     방 개수 · 가격 · 건물 유형 · 평수 · 층수
  결과 목록 (searchResultRecyclerView):
     superHostBadge "우수 임대인"
     addressAndTypeTextView "용산구 한강로2가의 원룸건물"
     roomNameTextView
     방/화장실/주방 카운트
```
> 웹: 좌측 고정 패널 + 우측 지도 → 앱: **전체화면 지도 + 드래그 바텀시트**. 완전히 다른 레이아웃.

### 2.8 매물 상세
```
ViewPager#roomImagePager  (스와이프) + "1 / 20" 카운터
  └ 우수 임대인 배지 오버레이
roomNameTextView · roomAddressTextView
최소 계약 기간 [1주] · costPerWeekTextView "350,000원 / 1주"
detailPriceInfoTextView "임대료 300,000원  관리비 50,000원"
할인 헤더 (discountInfoHeaderLayout): 장기계약 ~10%
탭: 방 정보 │ 계약 정보 │ 후기 │ 임대인 정보   ← 웹과 동일
구조 섹션 …
```
> 웹의 **우측 스티키 예약 카드**가 앱에서는 인라인 + 하단 고정 CTA로 대체.
> 갤러리: 웹=그리드+썸네일, 앱=**ViewPager 스와이프**.

### 2.9 계약 탭 (임차인) — 빈 상태
`contractEmptyTextView` "아직 진행중인 계약이 없습니다" + "삼삼엠투에서 필요한 방을 찾아보세요" + [단기임대 찾아보기]

---

## 3. Airbnb 앱 화면 인벤토리

### 3.1 검색(홈)
```
"검색을 시작해 보세요" 검색바
카테고리 가로 탭: 전체 │ 숙소 │ 체험 │ 서비스     ← 웹과 동일
지역별 캐러셀: "광안리해수욕장의 인기 숙소", "다음 달에 예약 가능한 오사카시 숙소"
카드 = Button (접근성 라벨에 전체 정보 포함)
```

### 3.2 여행
```
Google 지도 (TextureView, 전체 화면)
바텀시트 ("Expand sheet")
빈 상태: "다음 여행을 계획해 보세요 / 숙소·체험·서비스를 예약한 후 여기로 돌아와
         세부 정보를 확인하고, 지도를 살펴보고, 가볼 만한 장소를 저장하세요."
```
> 웹 여행 탭의 **여행 플래너** 방향과 일치. 앱도 지도 + 바텀시트.

### 3.3 프로필
```
사용자 카드 "승연 게스트"
이전 여행 [NEW]  ·  인연 [NEW]      ← 🆕 "인연"(Connections) 소셜 기능
호스팅 하기 — "간단하게 호스팅을 시작하고 부수입을 올릴 수 있습니다."
알림 배지 "새로운 알림 0건"
```

---

## 4. 새 서비스 앱 설계 시사점

1. **하단 5탭이 표준** — 두 앱 모두. 웹의 헤더 내비를 그대로 옮기지 말 것
2. **모드 전환은 탭 교체로** (33m2식) — 단, 전환 진입점을 마이 탭 최하단보다 위로 올릴 것
3. **지도는 전체화면 + 바텀시트** — 웹의 사이드 패널 레이아웃은 모바일에서 성립하지 않음
4. **필터는 가로 스크롤 칩** + 상세 필터 모달
5. **갤러리는 ViewPager 스와이프** + N/M 카운터
6. **등록 위저드는 동일 5단계 유지**, 이탈 확인 다이얼로그 필수
7. **언어 설정을 앱 메뉴에 노출** (웹은 헤더 셀렉터로 충분)
8. 검색 플레이스홀더 **동적 순환**은 저비용 고효과 (33m2 앱 차용)
9. ⚠️ 33m2는 웹·앱을 **각각 구현**(네이티브)해 유지비가 큽니다.
   Airbnb처럼 **프레젠테이션 API를 공유**하면 웹/앱 일관성과 개발 효율이 올라갑니다 —
   웹 먼저, 앱 2차 런칭 계획이라면 **초기부터 섹션 기반 응답 설계**를 검토할 가치가 있습니다.

---

## 5. 한계

- 앱 **네트워크 트래픽 미캡처** (HTTPS 인터셉트에는 프록시 CA 설치 필요 — 사용자 기기 설정 변경이라 수행하지 않음)
- 따라서 **앱 전용 API**가 웹과 다른지는 미확인 (동일 `/v1/` REST 사용 추정 ❓)
- 알림 권한 다이얼로그는 **선택하지 않고 뒤로** 처리 (기기 설정 변경 회피)
- Airbnb 앱은 resource-id가 없어 33m2만큼 상세 추출 불가
