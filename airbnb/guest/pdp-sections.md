# Airbnb PDP 섹션 스키마 (역추출)

> 출처: `airbnb.co.kr/rooms/{id}` 의 `<script id="data-deferred-state-0">` → `niobeClientData` → `StaysPdpSections`.

> 원본 JSON: `_shared/captures/airbnb.pdp.sections.json` (177KB)

> 로깅/실험 관련 필드는 제거했습니다.


## 섹션 래퍼 공통 필드

```
id · sectionId · sectionComponentType · sectionContentStatus · errors
sectionDependencies · enableDependencies · disableDependencies
mutationMetadata · pluginPointId · section(실 데이터)
```
> `sectionContentStatus` 로 지연 로딩 여부를, `*Dependencies` 로 섹션 간 의존성을 표현합니다.


## `DESCRIPTION_MODAL` — `GeneralListContentSection` (31 paths)

| path | type | sample |
|---|---|---|
| `buttons` | null | null |
| `caption` | null | null |
| `ctaButton` | null | null |
| `flip` | null | null |
| `headingLevel` | null | null |
| `items` | array | len=2 |
| `items[0].action` | null | null |
| `items[0].anchor` | null | null |
| `items[0].accessibilityLabel` | null | null |
| `items[0].button` | null | null |
| `items[0].icon` | null | null |
| `items[0].html` | object | {5} |
| `items[0].html.htmlText` | str | "º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다.<br />- 지하철역까지 도보 3분.<br />- 버스 정류장까지 |
| `items[0].html.readMoreButton` | null | null |
| `items[0].html.textStyle` | null | null |
| `items[0].html.recommendedNumberOfLines` | null | null |
| `items[0].html.minimumNumberOfLinesForTruncation` | null | null |
| `items[0].image` | null | null |
| `items[0].kicker` | null | null |
| `items[0].media` | null | null |
| `items[0].subtitle` | null | null |
| `items[0].subtitleStyle` | null | null |
| `items[0].title` | null | null |
| `items[0].titleStyle` | null | null |
| `kickerString` | null | null |
| `logoData` | null | null |
| `mediaItems` | null | null |
| `subtitle` | null | null |
| `subtitleStyle` | null | null |
| `title` | str | "숙소 설명" |
| `titleStyle` | null | null |

## `WHAT_COUNTS_AS_A_PET_MODAL` — `GeneralContentSection` (26 paths)

| path | type | sample |
|---|---|---|
| `button` | null | null |
| `BasicButtonFragment` | null | null |
| `icon` | null | null |
| `mediaItem` | object | {10} |
| `mediaItem.id` | str | "SW1hZ2U6d2hhdF9jb3VudHNfYXNfYV9wZXQ=" |
| `mediaItem.aspectRatio` | null | null |
| `mediaItem.orientation` | null | null |
| `mediaItem.onPressAction` | null | null |
| `mediaItem.accessibilityLabel` | str | "도우미 반려동물을 동반한 게스트가 호스트의 환영을 받고 있습니다." |
| `mediaItem.baseUrl` | str | "https://a0.muscache.com/pictures/adafb11b-41e9-49d3-908e-049dfd6934b6 |
| `mediaItem.displayAspectRatio` | null | null |
| `mediaItem.imageMetadata` | null | null |
| `mediaItem.previewEncodedPng` | str | "https://a0.muscache.com/pictures/adafb11b-41e9-49d3-908e-049dfd6934b6 |
| `mediaItem.overlay` | null | null |
| `subtitle` | null | null |
| `subtitleStyle` | null | null |
| `title` | str | "보조동물" |
| `titleStyle` | null | null |
| `headingLevel` | null | null |
| `html` | object | {5} |
| `html.htmlText` | str | "보조동물은 반려동물이 아니므로 여기에 추가할 필요가 없습니다.<br><br>정서적 지원 동물과 함께 여행하시나요? 에어비앤비 |
| `html.readMoreButton` | null | null |
| `html.textStyle` | null | null |
| `html.recommendedNumberOfLines` | null | null |
| `html.minimumNumberOfLinesForTruncation` | null | null |
| `kickerBadge` | null | null |

## `LOCATION_DEFAULT` — `LocationSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `REVIEWS_DEFAULT` — `StayPdpReviewsSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `AMENITIES_DEFAULT` — `AmenitiesSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `AVAILABILITY_CALENDAR_INLINE` — `AvailabilityCalendarSection` (10 paths)

| path | type | sample |
|---|---|---|
| `title` | str | "날짜 선택" |
| `subtitle` | str | "여행 날짜를 입력하여 정확한 요금을 확인하세요." |
| `descriptionItems` | array | len=3 |
| `descriptionItems[0].title` | str | "임대 호실 전체" |
| `listingTitle` | str | "낙성대역3분거리 역세권숙소 207" |
| `discountCopy` | null | null |
| `localizedLocation` | str | "서울, 한국" |
| `thumbnail` | object | {1} |
| `thumbnail.baseUrl` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `maxGuestCapacity` | int | 1 |

## `MEET_YOUR_HOST` — `MeetYourHostSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `POLICIES_DEFAULT` — `PoliciesSection` (52 paths)

| path | type | sample |
|---|---|---|
| `title` | str | "알아두어야 할 사항" |
| `cancellationPolicyForDisplay` | null | null |
| `additionalHouseRules` | null | null |
| `additionalHouseRulesTitle` | null | null |
| `cancellationPolicyTitle` | str | "환불 정책" |
| `houseRulesTitle` | str | "숙소 이용규칙" |
| `listingExpectationsTitle` | null | null |
| `safetyAndPropertyTitle` | str | "안전 및 공간" |
| `houseRules` | array | len=3 |
| `houseRules[0].icon` | null | null |
| `houseRules[0].title` | str | "체크인 시간: 오후 3:00~오후 10:00" |
| `listingExpectations` | null | null |
| `previewSafetyAndProperties` | array | len=3 |
| `previewSafetyAndProperties[0].title` | str | "일산화탄소 경보기 설치 여부 정보 없음" |
| `previewSafetyAndProperties[0].icon` | null | null |
| `previewSafetyAndProperties[0].learnMoreButton` | null | null |
| `safetyExpectationsAndAmenities` | null | null |
| `seeAllSafetyAndPropertyButton` | object | {2} |
| `seeAllSafetyAndPropertyButton.accessibilityLabel` | str | "안전 및 숙소에 관한 자세한 정보" |
| `seeAllSafetyAndPropertyButton.title` | str | "더 보기" |
| `seeAllHouseRulesButton` | object | {2} |
| `seeAllHouseRulesButton.accessibilityLabel` | str | "숙소 이용규칙에 관한 자세한 정보" |
| `seeAllHouseRulesButton.title` | str | "더 보기" |
| `seeCancellationPolicyButton` | object | {2} |
| `seeCancellationPolicyButton.accessibilityLabel` | str | "환불 정책에 관한 자세한 정보" |
| `seeCancellationPolicyButton.title` | str | "더 보기" |
| `cleaningModal` | null | null |
| `houseRulesSubtitle` | str | "에어비앤비 숙소는 다른 사람이 실제로 거주하는 집인 경우가 많으니 숙소 시설을 소중히 다뤄주세요." |
| `houseRulesTranslationDisclaimer` | null | null |
| `houseRulesSections` | array | len=2 |
| `houseRulesSections[0].title` | str | "체크인 및 체크아웃" |
| `houseRulesSections[0].items` | array | len=3 |
| `houseRulesSections[0].items[0].title` | str | "체크인 시간: 오후 3:00~오후 10:00" |
| `houseRulesSections[0].items[0].subtitle` | null | null |
| `houseRulesSections[0].items[0].icon` | str | "SYSTEM_CLOCK" |
| `houseRulesSections[0].items[0].html` | null | null |
| `safetyAndPropertySubtitle` | str | "나중에 당황하는 일이 없도록 호스트 숙소에 대한 중요 정보를 미리 확인하세요." |
| `safetyAndPropertiesTranslationDisclaimer` | null | null |
| `safetyAndPropertiesSections` | array | len=1 |
| `safetyAndPropertiesSections[0].title` | str | "안전 장치" |
| `safetyAndPropertiesSections[0].items` | array | len=3 |
| `safetyAndPropertiesSections[0].items[0].title` | str | "부지 내 실외 보안 카메라" |
| `safetyAndPropertiesSections[0].items[0].subtitle` | str | "“주차장, 1층현관, 각층 복도”" |
| `safetyAndPropertiesSections[0].items[0].icon` | str | "SYSTEM_SURVEILLANCE" |
| `safetyAndPropertiesSections[0].items[0].html` | null | null |
| `importantInformationTitle` | null | null |
| `importantInformationSubtitles` | null | null |
| `importantInformationContent` | null | null |
| `propertyLicenseTextList` | null | null |
| `enableCombinedThingsToKnowLayout` | bool | true |
| `businessDetails` | null | null |
| `seeBusinessDetailsCtaCopy` | null | null |

## `SIMILAR_LISTINGS_CAROUSEL` — `SBUISentinelSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `SEO_LINKS_DEFAULT` — `SeoLinksSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `BOOK_IT_SIDEBAR` — `BookItSection` (47 paths)

| path | type | sample |
|---|---|---|
| `subpageIdToOpen` | null | null |
| `showPriceBreakdown` | bool | true |
| `calendarTitle` | str | "날짜 선택" |
| `calendarSubtitle` | str | "여행 날짜를 입력하여 정확한 요금을 확인하세요." |
| `descriptionItems` | null | null |
| `discountCopy` | null | null |
| `maxGuestCapacity` | int | 1 |
| `maxPlusValue` | int | 16 |
| `reviewItem` | null | null |
| `available` | null | null |
| `structuredDisplayPrice` | null | null |
| `discountData` | null | null |
| `bookItButtonByPlacement` | null | null |
| `cancellationPolicies` | null | null |
| `cancellationPolicyForDisplay` | null | null |
| `localizedUnavailabilityMessage` | null | null |
| `localizedUnavailabilityMessagePositionString` | null | null |
| `priceDisclaimer` | null | null |
| `selectedDatesLink` | null | null |
| `selectedNights` | null | null |
| `bookItButtonLayout` | null | null |
| `productItemDetail` | null | null |
| `ratePlanTitle` | null | null |
| `promotionBanner` | null | null |
| `guestDisclaimer` | null | null |
| `petsAllowed` | null | null |
| `petDetails` | null | null |
| `adultsPicker` | object | {2} |
| `adultsPicker.title` | str | "성인" |
| `adultsPicker.subtitle` | str | "13세 이상" |
| `childrenPicker` | object | {2} |
| `childrenPicker.title` | str | "어린이" |
| `childrenPicker.subtitle` | str | "2~12세" |
| `infantsPicker` | object | {2} |
| `infantsPicker.title` | str | "유아" |
| `infantsPicker.subtitle` | str | "2세 미만" |
| `canInstantBook` | null | null |
| `highlightBanner` | null | null |
| `integratedPillMessageType` | null | null |
| `integratedPill` | null | null |
| `initialPillMessageType` | null | null |
| `initialPill` | null | null |
| `priceDetailPills` | array | len=0 |
| `availabilityPriceDetailEntry` | null | null |
| `vPoint` | null | null |
| `bookItPlacement` | str | "SIDEBAR" |
| `priceMerchandisingMessage` | null | null |

## `REPORT_TO_AIRBNB` — `ReportToAirbnbSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `NAV_DEFAULT` — `NavSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `BOOK_IT_NAV` — `BookItSection` (46 paths)

| path | type | sample |
|---|---|---|
| `subpageIdToOpen` | null | null |
| `showPriceBreakdown` | bool | false |
| `calendarTitle` | null | null |
| `calendarSubtitle` | null | null |
| `descriptionItems` | null | null |
| `discountCopy` | null | null |
| `maxGuestCapacity` | null | null |
| `maxPlusValue` | null | null |
| `reviewItem` | object | {5} |
| `reviewItem.accessibilityLabel` | str | "후기 24개로부터 5점 만점에 4.75점을 받은 숙소입니다." |
| `reviewItem.action` | null | null |
| `reviewItem.icon` | str | "COMPACT_STAR" |
| `reviewItem.subtitle` | str | "후기 24개" |
| `reviewItem.title` | str | "4.75 ·" |
| `available` | null | null |
| `structuredDisplayPrice` | null | null |
| `discountData` | null | null |
| `bookItButtonByPlacement` | null | null |
| `cancellationPolicies` | null | null |
| `cancellationPolicyForDisplay` | null | null |
| `localizedUnavailabilityMessage` | null | null |
| `localizedUnavailabilityMessagePositionString` | null | null |
| `priceDisclaimer` | null | null |
| `selectedDatesLink` | null | null |
| `selectedNights` | null | null |
| `bookItButtonLayout` | null | null |
| `productItemDetail` | null | null |
| `ratePlanTitle` | null | null |
| `promotionBanner` | null | null |
| `guestDisclaimer` | null | null |
| `petsAllowed` | null | null |
| `petDetails` | null | null |
| `adultsPicker` | null | null |
| `childrenPicker` | null | null |
| `infantsPicker` | null | null |
| `canInstantBook` | null | null |
| `highlightBanner` | null | null |
| `integratedPillMessageType` | null | null |
| `integratedPill` | null | null |
| `initialPillMessageType` | null | null |
| `initialPill` | null | null |
| `priceDetailPills` | null | null |
| `availabilityPriceDetailEntry` | null | null |
| `vPoint` | null | null |
| `bookItPlacement` | str | "NAV" |
| `priceMerchandisingMessage` | null | null |

## `OVERVIEW_DEFAULT_V2` — `SBUISentinelSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `GUEST_FAVORITE_BANNER` — `SBUISentinelSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `MESSAGE_BANNER` — `?`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`SHOULD_HIDE`


## `HIGHLIGHTS_COMPACT` — `PdpHighlightsCompactSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `HOST_OVERVIEW_DEFAULT` — `SBUISentinelSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `DESCRIPTION_DEFAULT` — `PdpDescriptionSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `TITLE_DEFAULT` — `PdpTitleSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `HERO_DEFAULT` — `PdpHeroSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `BOOK_IT_FLOATING_FOOTER` — `BookItSection` (43 paths)

| path | type | sample |
|---|---|---|
| `subpageIdToOpen` | null | null |
| `showPriceBreakdown` | bool | false |
| `calendarTitle` | null | null |
| `calendarSubtitle` | null | null |
| `descriptionItems` | null | null |
| `discountCopy` | null | null |
| `maxGuestCapacity` | null | null |
| `maxPlusValue` | null | null |
| `reviewItem` | null | null |
| `available` | null | null |
| `structuredDisplayPrice` | null | null |
| `discountData` | null | null |
| `bookItButtonByPlacement` | null | null |
| `cancellationPolicies` | null | null |
| `cancellationPolicyForDisplay` | null | null |
| `localizedUnavailabilityMessage` | null | null |
| `localizedUnavailabilityMessagePositionString` | null | null |
| `priceDisclaimer` | null | null |
| `selectedDatesLink` | object | {2} |
| `selectedDatesLink.title` | str | "10월 20일 ~ 11월 2일" |
| `selectedDatesLink.action` | object | {0} |
| `selectedNights` | null | null |
| `bookItButtonLayout` | str | "RIGHT_ALIGNED" |
| `productItemDetail` | null | null |
| `ratePlanTitle` | null | null |
| `promotionBanner` | null | null |
| `guestDisclaimer` | null | null |
| `petsAllowed` | null | null |
| `petDetails` | null | null |
| `adultsPicker` | null | null |
| `childrenPicker` | null | null |
| `infantsPicker` | null | null |
| `canInstantBook` | null | null |
| `highlightBanner` | null | null |
| `integratedPillMessageType` | null | null |
| `integratedPill` | null | null |
| `initialPillMessageType` | null | null |
| `initialPill` | null | null |
| `priceDetailPills` | array | len=0 |
| `availabilityPriceDetailEntry` | null | null |
| `vPoint` | null | null |
| `bookItPlacement` | str | "FLOATING_FOOTER" |
| `priceMerchandisingMessage` | null | null |

## `NAV_MOBILE` — `NavMobileSection`

> 익명 요청에서는 비어 있음 (지연 로딩). status=`COMPLETE`


## `CANCELLATION_POLICY_PICKER_MODAL` — `CancellationPolicyPickerSection` (5 paths)

| path | type | sample |
|---|---|---|
| `title` | str | "환불 정책을 선택하세요" |
| `button` | object | {2} |
| `button.title` | str | "계속" |
| `button.action` | null | null |
| `optionalityPriceDetail` | null | null |

## `PHOTO_TOUR_SCROLLABLE_MODAL` — `PhotoTourModalSection` (65 paths)

| path | type | sample |
|---|---|---|
| `title` | null | null |
| `mediaItems` | array | len=6 |
| `mediaItems[0].id` | str | "2285984199" |
| `mediaItems[0].aspectRatio` | float | 1.3333333333333333 |
| `mediaItems[0].orientation` | str | "LANDSCAPE" |
| `mediaItems[0].onPressAction` | null | null |
| `mediaItems[0].accessibilityLabel` | str | "리스팅 이미지 1" |
| `mediaItems[0].baseUrl` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `mediaItems[0].displayAspectRatio` | null | null |
| `mediaItems[0].imageMetadata` | object | {5} |
| `mediaItems[0].imageMetadata.caption` | null | null |
| `mediaItems[0].imageMetadata.imageType` | null | null |
| `mediaItems[0].imageMetadata.isProfessional` | bool | false |
| `mediaItems[0].imageMetadata.isVerified` | null | null |
| `mediaItems[0].imageMetadata.localizedCaption` | null | null |
| `mediaItems[0].previewEncodedPng` | null | null |
| `mediaItems[0].overlay` | null | null |
| `shareSave` | object | {6} |
| `shareSave.entityType` | str | "STAY" |
| `shareSave.shareButton` | object | {2} |
| `shareSave.shareButton.title` | str | "공유하기" |
| `shareSave.shareButton.subtitle` | null | null |
| `shareSave.saveButton` | object | {2} |
| `shareSave.saveButton.title` | str | "저장" |
| `shareSave.saveButton.subtitle` | null | null |
| `shareSave.unsaveButton` | object | {2} |
| `shareSave.unsaveButton.title` | str | "저장 목록" |
| `shareSave.unsaveButton.subtitle` | null | null |
| `shareSave.embedData` | object | {8} |
| `shareSave.embedData.id` | str | "1482267316113778051" |
| `shareSave.embedData.name` | str | "낙성대역3분거리 역세권숙소 207" |
| `shareSave.embedData.personCapacity` | int | 1 |
| `shareSave.embedData.pictureUrl` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `shareSave.embedData.propertyType` | str | "임대 호실 전체" |
| `shareSave.embedData.url` | null | null |
| `shareSave.embedData.reviewCount` | int | 24 |
| `shareSave.embedData.starRating` | float | 4.75 |
| `shareSave.sharingConfig` | object | {1} |
| `shareSave.sharingConfig.title` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `closeButton` | object | {4} |
| `closeButton.title` | str | "닫기" |
| `closeButton.anchor` | null | null |
| `closeButton.icon` | null | null |
| `closeButton.action` | null | null |
| `recommendedNumberOfHighlights` | null | null |
| `roomTourLayoutInfos` | array | len=1 |
| `roomTourLayoutInfos[0].roomTourItems` | array | len=1 |
| `roomTourLayoutInfos[0].roomTourItems[0].title` | null | null |
| `roomTourLayoutInfos[0].roomTourItems[0].imageIds` | array | len=6 |
| `roomTourLayoutInfos[0].roomTourItems[0].imageIds[]` |  | ["2285984199", "2285984205", "2285984191", "2285984198", "2285984197"] |
| `roomTourLayoutInfos[0].roomTourItems[0].mediaBlocks` | array | len=4 |
| `roomTourLayoutInfos[0].roomTourItems[0].mediaBlocks[0].flip` | str | "DEFAULT" |
| `roomTourLayoutInfos[0].roomTourItems[0].mediaBlocks[0].format` | str | "ONE_LANDSCAPE" |
| `roomTourLayoutInfos[0].roomTourItems[0].mediaBlocks[0].mediaBlock` | object | {1} |
| `roomTourLayoutInfos[0].roomTourItems[0].mediaBlocks[0].mediaBlock.landscapeId` | str | "2285984199" |
| `roomTourLayoutInfos[0].roomTourItems[0].highlights` | array | len=0 |
| `translationDisclaimer` | object | {3} |
| `translationDisclaimer.title` | null | null |
| `translationDisclaimer.subtitle` | str | "한국어로 번역하기" |
| `translationDisclaimer.icon` | str | "COMPACT_NO_TRANSLATION" |
| `showOriginalDisclaimer` | object | {3} |
| `showOriginalDisclaimer.title` | str | "자동 번역된 내용입니다." |
| `showOriginalDisclaimer.subtitle` | str | "원문 보기" |
| `showOriginalDisclaimer.icon` | str | "COMPACT_TRANSLATE" |
| `isAutoTranslatedOn` | bool | true |

## `AVAILABILITY_CALENDAR_DEFAULT` — `AvailabilityCalendarSection` (10 paths)

| path | type | sample |
|---|---|---|
| `title` | str | "날짜 선택" |
| `subtitle` | str | "여행 날짜를 입력하여 정확한 요금을 확인하세요." |
| `descriptionItems` | array | len=3 |
| `descriptionItems[0].title` | str | "임대 호실 전체" |
| `listingTitle` | str | "낙성대역3분거리 역세권숙소 207" |
| `discountCopy` | null | null |
| `localizedLocation` | str | "서울, 한국" |
| `thumbnail` | object | {1} |
| `thumbnail.baseUrl` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `maxGuestCapacity` | int | 1 |

## `BOOK_IT_CALENDAR_SHEET` — `BookItSection` (46 paths)

| path | type | sample |
|---|---|---|
| `subpageIdToOpen` | null | null |
| `showPriceBreakdown` | bool | false |
| `calendarTitle` | null | null |
| `calendarSubtitle` | null | null |
| `descriptionItems` | null | null |
| `discountCopy` | null | null |
| `maxGuestCapacity` | null | null |
| `maxPlusValue` | null | null |
| `reviewItem` | object | {5} |
| `reviewItem.accessibilityLabel` | str | "후기 24개로부터 5점 만점에 4.75점을 받은 숙소입니다." |
| `reviewItem.action` | null | null |
| `reviewItem.icon` | str | "COMPACT_STAR" |
| `reviewItem.subtitle` | null | null |
| `reviewItem.title` | str | "4.75" |
| `available` | null | null |
| `structuredDisplayPrice` | null | null |
| `discountData` | null | null |
| `bookItButtonByPlacement` | null | null |
| `cancellationPolicies` | null | null |
| `cancellationPolicyForDisplay` | null | null |
| `localizedUnavailabilityMessage` | null | null |
| `localizedUnavailabilityMessagePositionString` | null | null |
| `priceDisclaimer` | null | null |
| `selectedDatesLink` | null | null |
| `selectedNights` | null | null |
| `bookItButtonLayout` | null | null |
| `productItemDetail` | null | null |
| `ratePlanTitle` | null | null |
| `promotionBanner` | null | null |
| `guestDisclaimer` | null | null |
| `petsAllowed` | null | null |
| `petDetails` | null | null |
| `adultsPicker` | null | null |
| `childrenPicker` | null | null |
| `infantsPicker` | null | null |
| `canInstantBook` | null | null |
| `highlightBanner` | null | null |
| `integratedPillMessageType` | null | null |
| `integratedPill` | null | null |
| `initialPillMessageType` | null | null |
| `initialPill` | null | null |
| `priceDetailPills` | null | null |
| `availabilityPriceDetailEntry` | null | null |
| `vPoint` | null | null |
| `bookItPlacement` | str | "CALENDAR_SHEET" |
| `priceMerchandisingMessage` | null | null |