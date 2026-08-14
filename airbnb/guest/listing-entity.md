# Airbnb 숙소(Listing) 엔티티 — `node.pdpPresentation`

> 출처: `StaysPdpSections` GraphQL 응답의 `data.node`(타입 `DemandStayListing`).

> 33m2의 `ENT-001 Room` 에 대응하는 **Airbnb 핵심 엔티티**입니다.

> 원본: `_shared/captures/airbnb.pdp.sections.json`


## 최상위 필드 (27)

```
__typename
businessDetails
luxeBannerDescription
accessibilityFeatures
amenities
localizedLocation
availabilityCalendarDescriptionItems
bathroomsTour
descriptions
title
heroMedia
highlights
disclaimers
quality
location
addOnServices
hostInfo
sharingConfig
personCapacity
reportTermsDisclaimer
seoLinks
sleepingArrangements
overview
mediaTour
pdpEducation
pdpType
seoFeatures
```

### `accessibilityFeatures`

| path | type | sample |
|---|---|---|
| `accessibilityFeatures.name` | str | "접근성 편의" |
| `accessibilityFeatures.translationDisclaimer` | str | "한국어로 번역하기" |
| `accessibilityFeatures.stops` | array | len=0 |

### `amenities`

| path | type | sample |
|---|---|---|
| `amenities.title` | str | "숙소 편의시설" |
| `amenities.subtitle` | null | null |
| `amenities.overridePreviewTitle` | null | null |
| `amenities.prioritizeShowingAllPreviewAmenities` | bool | false |
| `amenities.previewAmenitiesGroups` | array | len=1 |
| `amenities.previewAmenitiesGroups[0].title` | null | null |
| `amenities.previewAmenitiesGroups[0].amenities` | array | len=10 |
| `amenities.previewAmenitiesGroups[0].amenities[0].available` | bool | true |
| `amenities.previewAmenitiesGroups[0].amenities[0].title` | str | "주방" |
| `amenities.previewAmenitiesGroups[0].amenities[0].icon` | str | "SYSTEM_COOKING_BASICS" |
| `amenities.seeAllAmenitiesGroups` | array | len=9 |
| `amenities.seeAllAmenitiesGroups[0].title` | str | "욕실" |
| `amenities.seeAllAmenitiesGroups[0].amenities` | array | len=4 |
| `amenities.seeAllAmenitiesGroups[0].amenities[0].id` | str | "pdp_v3_bathroom_45_1482267316113778051-0" |
| `amenities.seeAllAmenitiesGroups[0].amenities[0].available` | bool | true |
| `amenities.seeAllAmenitiesGroups[0].amenities[0].title` | str | "헤어드라이어" |
| `amenities.seeAllAmenitiesGroups[0].amenities[0].icon` | str | "SYSTEM_HAIRDRYER" |
| `amenities.seeAllAmenitiesGroups[0].amenities[0].subtitle` | object | {1} |
| `amenities.seeAllAmenitiesGroups[0].amenities[0].subtitle.text` | str | "" |

### `bathroomsTour`

| path | type | sample |
|---|---|---|
| `bathroomsTour.name` | str | "What’s the bathroom like" |
| `bathroomsTour.stops` | array | len=0 |

### `descriptions`

| path | type | sample |
|---|---|---|
| `descriptions.isVetted` | bool | false |
| `descriptions.longDescriptionHtml` | object | {3} |
| `descriptions.longDescriptionHtml.localizedStringWithTranslationPreference` | str | "º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다.<br />- 지하철역까지 도보 3분.<br />- 버스 정류장까지 |
| `descriptions.longDescriptionHtml.localizedString` | str | "º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다.<br />- 지하철역까지 도보 3분.<br />- 버스 정류장까지 |
| `descriptions.longDescriptionHtml.source` | str | "º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다.<br />- 지하철역까지 도보 3분.<br />- 버스 정류장까지 |
| `descriptions.modalTitle` | str | "숙소 설명" |
| `descriptions.shortDescriptionHtml` | object | {1} |
| `descriptions.shortDescriptionHtml.content` | object | {3} |
| `descriptions.shortDescriptionHtml.content.localizedStringWithTranslationPreference` | str | "º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다.<br />- 지하철역까지 도보 3분.<br />- 버스 정류장까지 |
| `descriptions.shortDescriptionHtml.content.localizedString` | str | "º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다.<br />- 지하철역까지 도보 3분.<br />- 버스 정류장까지 |
| `descriptions.shortDescriptionHtml.content.source` | str | "º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다.<br />- 지하철역까지 도보 3분.<br />- 버스 정류장까지 |
| `descriptions.title` | null | null |

### `title`

| path | type | sample |
|---|---|---|
| `title.content` | object | {3} |
| `title.content.localizedStringWithTranslationPreference` | str | "낙성대역3분거리 역세권숙소 207" |
| `title.content.localizedString` | str | "낙성대역3분거리 역세권숙소 207" |
| `title.content.source` | str | "낙성대역3분거리 역세권숙소 207" |

### `heroMedia`

| path | type | sample |
|---|---|---|
| `heroMedia.edges` | array | len=6 |
| `heroMedia.edges[0].node` | object | {1} |
| `heroMedia.edges[0].node.image` | object | {7} |
| `heroMedia.edges[0].node.image.altText` | null | null |
| `heroMedia.edges[0].node.image.id` | str | "SW1hZ2VFbnRpdHk6MjI4NTk4NDE5OQ==" |
| `heroMedia.edges[0].node.image.uri` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `heroMedia.edges[0].node.image.caption` | null | null |
| `heroMedia.edges[0].node.image.assetMetadata` | object | {4} |
| `heroMedia.edges[0].node.image.assetMetadata.aspectRatio` | float | 1.3333333333333333 |
| `heroMedia.edges[0].node.image.assetMetadata.orientation` | str | "LANDSCAPE" |
| `heroMedia.edges[0].node.image.assetMetadata.originalWidth` | int | 4000 |
| `heroMedia.edges[0].node.image.assetMetadata.originalHeight` | int | 3000 |
| `heroMedia.edges[0].node.image.tags` | array | len=3 |
| `heroMedia.edges[0].node.image.tags[0].name` | str | "Other" |
| `heroMedia.edges[0].node.image.moderatedUri` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |

### `disclaimers`

| path | type | sample |
|---|---|---|
| `disclaimers.highlights` | null | null |

### `quality`

| path | type | sample |
|---|---|---|
| `quality.isGuestFavorite` | bool | false |
| `quality.listingRatingStats` | object | {1} |
| `quality.listingRatingStats.overallRatingStats` | object | {2} |
| `quality.listingRatingStats.overallRatingStats.ratingAverage` | float | 4.75 |
| `quality.listingRatingStats.overallRatingStats.ratingCount` | str | "24" |
| `quality.isNewListing` | bool | false |
| `quality.allowsDisplayBottomQualityInformation` | bool | true |
| `quality.isViewedByHost` | bool | false |
| `quality.specialTreatmentCountry` | str | "NONE" |
| `quality.hasFewReviews` | bool | false |
| `quality.qualityScorePercentileBucket` | null | null |
| `quality.hostRatingCount` | str | "450" |
| `quality.supportsCategoryRatings` | bool | true |
| `quality.categoryRatings` | array | len=6 |
| `quality.categoryRatings[0].categoryType` | str | "CLEANLINESS" |
| `quality.categoryRatings[0].localizedRating` | str | "4.8" |
| `quality.categoryRatings[0].label` | str | "청결도" |
| `quality.categoryRatings[0].accessibilityLabel` | str | "청결도 항목에서 5점 만점 중 4.8점을 받았습니다." |
| `quality.categoryRatings[0].percentage` | float | 0.96 |
| `quality.ratingDistribution` | array | len=5 |
| `quality.ratingDistribution[0].label` | str | "5" |
| `quality.ratingDistribution[0].localizedRating` | str | "88%" |
| `quality.ratingDistribution[0].percentage` | float | 0.875 |
| `quality.ratingDistribution[0].accessibilityLabel` | str | "88%의 후기에서 5점의 별점을 받았습니다." |
| `quality.disclaimerLocation` | str | "UNDER_SUBTITLE" |
| `quality.reviewTags` | array | len=10 |
| `quality.reviewTags[0].name` | str | "GETTING_AROUND" |
| `quality.reviewTags[0].count` | int | 9 |
| `quality.reviewTags[0].localizedName` | str | "교통 편의성" |
| `quality.reviewTags[0].icon` | object | {1} |
| `quality.reviewTags[0].icon.baseUrl` | str | "https://a0.muscache.com/im/pictures/AirbnbPlatformAssets/AirbnbPlatfo |
| `quality.reviewSortSelectOptions` | array | len=4 |
| `quality.reviewSortSelectOptions[0].title` | str | "관련성 높은 순" |
| `quality.reviewSortSelectOptions[0].reviewsSortType` | str | "BEST_QUALITY" |
| `quality.guestFavoriteDescription` | str | "에어비앤비 게스트에게 가장 사랑받는 숙소" |
| `quality.reviewsCountUnit` | str | "개" |

### `location`

| path | type | sample |
|---|---|---|
| `location.subtitle` | str | "서울, 한국" |
| `location.homeIconIdentifier` | str | "COMPACT_HOUSE" |
| `location.latitude` | float | 37.4787 |
| `location.longitude` | float | 126.9618 |
| `location.isExactLocation` | bool | true |
| `location.defaultZoomLevel` | int | 14 |
| `location.categoryConfigs` | null | null |
| `location.exactAddress` | null | null |
| `location.verificationDetails` | object | {5} |
| `location.verificationDetails.isVerified` | bool | false |
| `location.verificationDetails.verifiedListingText` | null | null |
| `location.verificationDetails.verifiedHelpHtml` | null | null |
| `location.verificationDetails.verifiedHelpLinkText` | null | null |
| `location.verificationDetails.verifiedHelpModalContent` | null | null |
| `location.previewLocationDetails` | array | len=0 |
| `location.seeAllLocationDetails` | null | null |
| `location.nearbyPlacesData` | null | null |

### `hostInfo`

| path | type | sample |
|---|---|---|
| `hostInfo.passportData` | object | {13} |
| `hostInfo.passportData.name` | str | "필용" |
| `hostInfo.passportData.userId` | str | "RGVtYW5kVXNlcjo2Njg5OTYxNDc=" |
| `hostInfo.passportData.contextualUserId` | str | "Q29udGV4dHVhbFVzZXI6MTQ3MDY3ODAyNzM0MjA1NjE5OA==" |
| `hostInfo.passportData.titleText` | str | "호스트" |
| `hostInfo.passportData.profilePictureUrl` | str | "https://a0.muscache.com/im/pictures/user/User/original/84f81fce-4eb6- |
| `hostInfo.passportData.profileLoggingId` | null | null |
| `hostInfo.passportData.isSuperhost` | bool | false |
| `hostInfo.passportData.isVerified` | bool | true |
| `hostInfo.passportData.stats` | array | len=3 |
| `hostInfo.passportData.stats[0].label` | str | "후기" |
| `hostInfo.passportData.stats[0].value` | str | "450" |
| `hostInfo.passportData.stats[0].a11yValue` | str | "후기 450개" |
| `hostInfo.passportData.stats[0].type` | str | "REVIEW_COUNT" |
| `hostInfo.passportData.ratingCount` | int | 450 |
| `hostInfo.passportData.ratingAverage` | float | 4.67 |
| `hostInfo.passportData.timeAsHost` | object | {2} |
| `hostInfo.passportData.timeAsHost.years` | int | 1 |
| `hostInfo.passportData.timeAsHost.months` | int | 7 |
| `hostInfo.passportData.profileA11yLabel` | str | "호스트 필용님에 대해 자세히 알아보세요." |
| `hostInfo.highlights` | array | len=0 |
| `hostInfo.responseRateText` | str | "응답률: 99%" |
| `hostInfo.responseTimeText` | str | "1시간 이내에 응답" |
| `hostInfo.canBeMessaged` | bool | true |
| `hostInfo.isAirbnbManaged` | bool | false |
| `hostInfo.about` | null | null |
| `hostInfo.overview` | object | {2} |
| `hostInfo.overview.title` | object | {1} |
| `hostInfo.overview.title.text` | str | "호스트: 필용 님" |
| `hostInfo.overview.items` | array | len=1 |
| `hostInfo.overview.items[0].text` | str | "호스팅 경력 2년" |

### `sharingConfig`

| path | type | sample |
|---|---|---|
| `sharingConfig.imageUrl` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `sharingConfig.propertyType` | str | "임대 호실 전체" |
| `sharingConfig.ugcTitle` | object | {1} |
| `sharingConfig.ugcTitle.content` | object | {3} |
| `sharingConfig.ugcTitle.content.localizedStringWithTranslationPreference` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `sharingConfig.ugcTitle.content.localizedString` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `sharingConfig.ugcTitle.content.source` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `sharingConfig.shareUrl` | str | "https://www.airbnb.co.kr/rooms/1482267316113778051?unique_share_id=a0 |

### `seoLinks`

| path | type | sample |
|---|---|---|
| `seoLinks.title` | str | " 및 인근의 다른 옵션 살펴보기" |
| `seoLinks.breadcrumbs` | array | len=4 |
| `seoLinks.breadcrumbs[0].title` | str | "에어비앤비" |
| `seoLinks.breadcrumbs[0].path` | str | "/" |
| `seoLinks.nearbyCityLinks` | array | len=9 |
| `seoLinks.nearbyCityLinks[0].title` | str | "부산" |
| `seoLinks.nearbyCityLinks[0].subtitle` | str | "휴가지 숙소" |
| `seoLinks.nearbyCityLinks[0].path` | str | "/busan-south-korea/stays" |
| `seoLinks.otherStaysLinks` | array | len=5 |
| `seoLinks.otherStaysLinks[0].title` | str | "서울의 휴가지 숙소" |
| `seoLinks.otherStaysLinks[0].path` | str | "/seoul-south-korea/stays" |

### `overview`

| path | type | sample |
|---|---|---|
| `overview.title` | str | "한국의 임대 호실 전체" |
| `overview.items` | array | len=4 |
| `overview.items[]` |  | ["최대 인원 1명", "침실 1개", "침대 1개", "욕실 1개"] |
| `overview.reviewsInfoLayout` | str | "STANDARD" |

### `mediaTour`

| path | type | sample |
|---|---|---|
| `mediaTour.name` | null | null |
| `mediaTour.stops` | array | len=1 |
| `mediaTour.stops[0].id` | str | "1482267316113778051" |
| `mediaTour.stops[0].name` | null | null |
| `mediaTour.stops[0].items` | array | len=6 |
| `mediaTour.stops[0].items[0].image` | object | {7} |
| `mediaTour.stops[0].items[0].image.altText` | null | null |
| `mediaTour.stops[0].items[0].image.id` | str | "SW1hZ2VFbnRpdHk6MjE5MTQyMzc2NTIxMTM2NjQ5NQ==" |
| `mediaTour.stops[0].items[0].image.uri` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `mediaTour.stops[0].items[0].image.caption` | null | null |
| `mediaTour.stops[0].items[0].image.assetMetadata` | object | {4} |
| `mediaTour.stops[0].items[0].image.assetMetadata.aspectRatio` | float | 1.3333333333333333 |
| `mediaTour.stops[0].items[0].image.assetMetadata.orientation` | str | "LANDSCAPE" |
| `mediaTour.stops[0].items[0].image.assetMetadata.originalWidth` | int | 4000 |
| `mediaTour.stops[0].items[0].image.assetMetadata.originalHeight` | int | 3000 |
| `mediaTour.stops[0].items[0].image.tags` | null | null |
| `mediaTour.stops[0].items[0].image.imageId` | str | "2285984199" |
| `mediaTour.stops[0].description` | null | null |

### `seoFeatures`

| path | type | sample |
|---|---|---|
| `seoFeatures.title` | object | {1} |
| `seoFeatures.title.text` | str | "" |
| `seoFeatures.metaDescription` | object | {1} |
| `seoFeatures.metaDescription.content` | object | {3} |
| `seoFeatures.metaDescription.content.localizedStringWithTranslationPreference` | str | "2026년 8월 14일 · 임대 호실 전체 · º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다. - 지하철역까지 도 |
| `seoFeatures.metaDescription.content.localizedString` | str | "2026년 8월 14일 · 임대 호실 전체 · º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다. - 지하철역까지 도 |
| `seoFeatures.metaDescription.content.source` | str | "2026년 8월 14일 · 임대 호실 전체 · º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다. - 지하철역까지 도 |
| `seoFeatures.canonicalUrl` | str | "https://www.airbnb.co.kr/rooms/1482267316113778051" |
| `seoFeatures.indexInSearchEngines` | bool | true |
| `seoFeatures.relImageSrc` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `seoFeatures.androidAlternateUrl` | str | "android-app://com.airbnb.android/airbnb/rooms/1482267316113778051" |
| `seoFeatures.androidDeeplink` | str | "airbnb://rooms/1482267316113778051" |
| `seoFeatures.iphoneDeeplink` | str | "airbnb://rooms/1482267316113778051" |
| `seoFeatures.ogTags` | object | {5} |
| `seoFeatures.ogTags.ogTitle` | object | {1} |
| `seoFeatures.ogTags.ogTitle.content` | object | {3} |
| `seoFeatures.ogTags.ogTitle.content.localizedStringWithTranslationPreference` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `seoFeatures.ogTags.ogTitle.content.localizedString` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `seoFeatures.ogTags.ogTitle.content.source` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `seoFeatures.ogTags.ogDescription` | object | {1} |
| `seoFeatures.ogTags.ogDescription.content` | object | {3} |
| `seoFeatures.ogTags.ogDescription.content.localizedStringWithTranslationPreference` | str | "낙성대역3분거리 역세권숙소 207" |
| `seoFeatures.ogTags.ogDescription.content.localizedString` | str | "낙성대역3분거리 역세권숙소 207" |
| `seoFeatures.ogTags.ogDescription.content.source` | str | "낙성대역3분거리 역세권숙소 207" |
| `seoFeatures.ogTags.ogImage` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `seoFeatures.ogTags.ogType` | str | "airbedandbreakfast:listing" |
| `seoFeatures.ogTags.ogUrl` | str | "https://www.airbnb.co.kr/rooms/1482267316113778051" |
| `seoFeatures.twitterTags` | object | {3} |
| `seoFeatures.twitterTags.twitterCard` | str | "photo" |
| `seoFeatures.twitterTags.twitterImage` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `seoFeatures.twitterTags.twitterUrl` | str | "https://www.airbnb.co.kr/rooms/1482267316113778051" |

---

## `presentation…sections.metadata`

| path | type | sample |
|---|---|---|
| `pdpType` | str | "MARKETPLACE" |
| `pageTitle` | null | null |
| `isElvisListing` | bool | false |
| `errorData` | null | null |
| `sharingConfig` | object | {7} |
| `sharingConfig.title` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `sharingConfig.propertyType` | str | "임대 호실 전체" |
| `sharingConfig.personCapacity` | int | 1 |
| `sharingConfig.imageUrl` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `sharingConfig.shareUrl` | str | "https://www.airbnb.co.kr/rooms/1482267316113778051?unique_share_id=5b |
| `sharingConfig.reviewCount` | int | 24 |
| `sharingConfig.starRating` | float | 4.75 |
| `loggingContext` | object | {1} |
| `loggingContext.eventDataLogging` | object | {20} |
| `loggingContext.eventDataLogging.listingId` | str | "1482267316113778051" |
| `loggingContext.eventDataLogging.page` | str | "p3" |
| `loggingContext.eventDataLogging.pdpPageType` | int | 1 |
| `loggingContext.eventDataLogging.listingLat` | float | 37.4787 |
| `loggingContext.eventDataLogging.listingLng` | float | 126.9618 |
| `loggingContext.eventDataLogging.homeTier` | int | 1 |
| `loggingContext.eventDataLogging.roomType` | str | "Entire home/apt" |
| `loggingContext.eventDataLogging.personCapacity` | int | 1 |
| `loggingContext.eventDataLogging.descriptionLanguage` | str | "ko" |
| `loggingContext.eventDataLogging.isSuperhost` | bool | false |
| `loggingContext.eventDataLogging.amenities` | array | len=0 |
| `loggingContext.eventDataLogging.accuracyRating` | float | 4.92 |
| `loggingContext.eventDataLogging.checkinRating` | float | 4.96 |
| `loggingContext.eventDataLogging.cleanlinessRating` | float | 4.75 |
| `loggingContext.eventDataLogging.communicationRating` | float | 4.83 |
| `loggingContext.eventDataLogging.locationRating` | float | 4.88 |
| `loggingContext.eventDataLogging.valueRating` | float | 4.83 |
| `loggingContext.eventDataLogging.guestSatisfactionOverall` | float | 4.75 |
| `loggingContext.eventDataLogging.visibleReviewCount` | str | "24" |
| `loggingContext.eventDataLogging.propertyId` | null | null |
| `seoFeatures` | object | {12} |
| `seoFeatures.androidAlternateUrl` | str | "android-app://com.airbnb.android/airbnb/rooms/1482267316113778051" |
| `seoFeatures.androidDeeplink` | str | "airbnb://rooms/1482267316113778051" |
| `seoFeatures.canonicalUrl` | str | "https://www.airbnb.co.kr/rooms/1482267316113778051" |
| `seoFeatures.iphoneDeeplink` | str | "airbnb://rooms/1482267316113778051" |
| `seoFeatures.metaDescription` | str | "2026년 8월 14일 · 임대 호실 전체 · º 중심부에 위치하여 최고의 접근성을 자랑하는 숙소입니다. - 지하철역까지 도 |
| `seoFeatures.title` | str | "" |
| `seoFeatures.breadcrumbDetails` | array | len=0 |
| `seoFeatures.ogTags` | object | {10} |
| `seoFeatures.ogTags.ogDescription` | str | "낙성대역3분거리 역세권숙소 207" |
| `seoFeatures.ogTags.ogImage` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `seoFeatures.ogTags.ogTitle` | str | "임대 호실 · 서울 · ★4.75 · 침실 1개 · 침대 1개 · 욕실 1개" |
| `seoFeatures.ogTags.ogType` | str | "airbedandbreakfast:listing" |
| `seoFeatures.ogTags.ogUrl` | str | "https://www.airbnb.co.kr/rooms/1482267316113778051" |
| `seoFeatures.ogTags.ogImageHeight` | null | null |
| `seoFeatures.ogTags.ogImageWidth` | null | null |
| `seoFeatures.ogTags.ogVideoUrl` | null | null |
| `seoFeatures.ogTags.ogVideoHeight` | null | null |
| `seoFeatures.ogTags.ogVideoWidth` | null | null |
| `seoFeatures.propertySearchUrl` | null | null |
| `seoFeatures.relImageSrc` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `seoFeatures.twitterTags` | object | {5} |
| `seoFeatures.twitterTags.twitterCard` | str | "photo" |
| `seoFeatures.twitterTags.twitterDescription` | null | null |
| `seoFeatures.twitterTags.twitterImage` | str | "https://a0.muscache.com/im/pictures/hosting/Hosting-14822673161137780 |
| `seoFeatures.twitterTags.twitterTitle` | null | null |

---

## `screens` (13) — 모달/서브페이지 정의

- `DESCRIPTION` — ScreenContainer
- `PROFESSIONAL_HOST_DETAILS` — ScreenContainer
- `WHAT_COUNTS_AS_A_PET_MODAL` — ScreenContainer
- `ROOT` — ScreenContainer
- `PRICE_DETAIL_MODAL` — ScreenContainer
- `INDIVIDUAL_HOST_PROMPT` — ScreenContainer
- `TRANSLATION_PROMPT` — ScreenContainer
- `CANCELLATION_POLICY_PICKER` — ScreenContainer
- `PHOTO_TOUR_SCROLLABLE` — ScreenContainer
- `NON_EXPERIENCED_GUEST_LEARN_MORE_MODAL` — ScreenContainer
- `CALENDAR` — ScreenContainer
- `EDUCATION` — ScreenContainer
- `ACCESSIBILITY` — ScreenContainer