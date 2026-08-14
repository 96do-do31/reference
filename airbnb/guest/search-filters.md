# Airbnb 검색 필터 카탈로그 (역추출)

> 출처: `StaysSearch` 응답의 `results.filters.filterPanel.filterPanelSections.sections`.

> 각 항목은 `searchParams.params[{key, value, valueType, inArray}]` 로 **URL 쿼리 파라미터에 직접 매핑**됩니다.

> 원본: `_shared/captures/airbnb.search.json`


## `PRICE_RANGE` — 1개

| 표시명 | param key | value | type |
|---|---|---|---|
| ₩180,000 - ₩4,600,000 | `price_min` | `None` | integer |
| ₩180,000 - ₩4,600,000 | `price_max` | `None` | integer |

## `ROOM_TYPE` — 1개

| 표시명 | param key | value | type |
|---|---|---|---|
| 숙소 유형 | — | — | — |

## `ROOMS_AND_BEDS_WITH_SUBCATEGORY` — 3개

| 표시명 | param key | value | type |
|---|---|---|---|
| 침실 | `min_bedrooms` | `0` | integer |
| 침대 | `min_beds` | `0` | integer |
| 욕실 | `min_bathrooms` | `0` | integer |

## `TOP_TIER_STAYS` — 1개

| 표시명 | param key | value | type |
|---|---|---|---|
| — | — | — | — |

## `BOOKING_OPTIONS` — 4개

| 표시명 | param key | value | type |
|---|---|---|---|
| 즉시 예약 | `ib` | `True` | boolean |
| 셀프 체크인 | `amenities` | `None` | array (array) |
| 취소 수수료 없음 | `flexible_cancellation` | `True` | boolean |
| 반려동물 동반 가능 | `pets` | `1` | integer |

## `ACCESSIBILITY` — 16개

| 표시명 | param key | value | type |
|---|---|---|---|
| 게스트 출입구 및 주차장 | — | — | — |
| 계단 없이 출입 가능 | `amenities` | `None` | array (array) |
| 장애인용 주차 공간 | `amenities` | `None` | array (array) |
| 너비 81cm 이상의 게스트 출입구 | `amenities` | `None` | array (array) |
| 침실 | — | — | — |
| 계단이나 문턱 없는 침실 | `amenities` | `None` | array (array) |
| 너비 81cm 이상의 침실 출입구 | `amenities` | `None` | array (array) |
| 욕실 | — | — | — |
| 계단이나 문턱 없는 욕실 | `amenities` | `None` | array (array) |
| 너비 81cm 이상의 욕실 출입구 | `amenities` | `None` | array (array) |
| 변기 옆 고정 손잡이 | `amenities` | `None` | array (array) |
| 샤워실 고정 손잡이 | `amenities` | `None` | array (array) |
| 계단이나 문턱 없는 샤워실 | `amenities` | `None` | array (array) |
| 샤워/목욕 의자 | `amenities` | `None` | array (array) |
| 장애인용 보조 장치 | — | — | — |
| 천장형 또는 이동식 리프트 | `amenities` | `None` | array (array) |

## `MORE_FILTERS_AMENITIES_WITH_SUBCATEGORIES` — 30개

| 표시명 | param key | value | type |
|---|---|---|---|
| 인기 | — | — | — |
| 와이파이 | `amenities` | `None` | array (array) |
| 에어컨 | `amenities` | `None` | array (array) |
| 침실에 딸린 개인 욕실 | `bathroom_privacy` | `ENSUITE` | array (array) |
| 건조기 | `amenities` | `None` | array (array) |
| 헤어드라이어 | `amenities` | `None` | array (array) |
| 난방 | `amenities` | `None` | array (array) |
| TV | `amenities` | `None` | array (array) |
| 필수 | — | — | — |
| 주방 | `amenities` | `None` | array (array) |
| 세탁기 | `amenities` | `None` | array (array) |
| 업무 전용 공간 | `amenities` | `None` | array (array) |
| 다리미 | `amenities` | `None` | array (array) |
| 특징 | — | — | — |
| 수영장 | `amenities` | `None` | array (array) |
| 대형 욕조 | `amenities` | `None` | array (array) |
| 무료 주차 공간 | `amenities` | `None` | array (array) |
| 전기차 충전시설 | `amenities` | `None` | array (array) |
| 아기 침대 | `amenities` | `None` | array (array) |
| 킹사이즈 침대 | `amenities` | `None` | array (array) |
| 헬스장 | `amenities` | `None` | array (array) |
| 바비큐 그릴 | `amenities` | `None` | array (array) |
| 조식 | `amenities` | `None` | array (array) |
| 실내 벽난로 | `amenities` | `None` | array (array) |
| 흡연 가능 | `amenities` | `None` | array (array) |
| 위치 | — | — | — |
| 수변 | `kg_and_tags` | `Tag:686` | array (array) |
| 안전 | — | — | — |
| 화재경보기 | `amenities` | `None` | array (array) |
| 일산화탄소 경보기 | `amenities` | `None` | array (array) |

## `PROPERTY_TYPES_WITH_SUBCATEGORY` — 4개

| 표시명 | param key | value | type |
|---|---|---|---|
| 단독 또는 다세대 주택 | `l2_property_type_ids` | `None` | array (array) |
| 아파트 | `l2_property_type_ids` | `None` | array (array) |
| 게스트용 별채 | `l2_property_type_ids` | `None` | array (array) |
| 호텔 | `l2_property_type_ids` | `None` | array (array) |

## `HOST_LANGUAGE` — 62개

| 표시명 | param key | value | type |
|---|---|---|---|
| 중국어(간체) | `host_languages` | `zh` | array (array) |
| 중국어(번체) | `host_languages` | `zh-TW` | array (array) |
| 영어 | `host_languages` | `en` | array (array) |
| 프랑스어 | `host_languages` | `fr` | array (array) |
| 독일어 | `host_languages` | `de` | array (array) |
| 이탈리아어 | `host_languages` | `it` | array (array) |
| 일본어 | `host_languages` | `ja` | array (array) |
| 한국어 | `host_languages` | `ko` | array (array) |
| 포르투갈어 | `host_languages` | `pt` | array (array) |
| 러시아어 | `host_languages` | `ru` | array (array) |
| 스페인어 | `host_languages` | `es` | array (array) |
| 아랍어 | `host_languages` | `ar` | array (array) |
| 크로아티아어 | `host_languages` | `hr` | array (array) |
| 체코어 | `host_languages` | `cs` | array (array) |
| 덴마크어 | `host_languages` | `da` | array (array) |
| 네덜란드어 | `host_languages` | `nl` | array (array) |
| 핀란드어 | `host_languages` | `fi` | array (array) |
| 그리스어 | `host_languages` | `el` | array (array) |
| 힌디어 | `host_languages` | `hi` | array (array) |
| 헝가리어 | `host_languages` | `hu` | array (array) |
| 아이슬란드어 | `host_languages` | `is` | array (array) |
| 인도네시아어 | `host_languages` | `id` | array (array) |
| 말레이시아어 | `host_languages` | `ms` | array (array) |
| 노르웨이어 | `host_languages` | `no` | array (array) |
| 폴란드어 | `host_languages` | `pl` | array (array) |
| 스웨덴어 | `host_languages` | `sv` | array (array) |
| 태국어 | `host_languages` | `th` | array (array) |
| 튀르키예어 | `host_languages` | `tr` | array (array) |
| 아프리칸스어 | `host_languages` | `af` | array (array) |
| 알바니아어 | `host_languages` | `sq` | array (array) |
| 아르메니아어 | `host_languages` | `hy` | array (array) |
| 아제르바이잔어 | `host_languages` | `az` | array (array) |
| 바스크어 | `host_languages` | `eu` | array (array) |
| 벨라루스어 | `host_languages` | `be` | array (array) |
| 벵골어 | `host_languages` | `bn` | array (array) |
| 보스니아어 | `host_languages` | `bs` | array (array) |
| 불가리아어 | `host_languages` | `bg` | array (array) |
| 미얀마어(버마어) | `host_languages` | `my` | array (array) |
| 에스토니아어 | `host_languages` | `et` | array (array) |
| 필리핀어 | `host_languages` | `fil` | array (array) |
| 갈리시아어 | `host_languages` | `gl` | array (array) |
| 조지아어 | `host_languages` | `ka` | array (array) |
| 구자라트어 | `host_languages` | `gu` | array (array) |
| 아이티 크리올어 | `host_languages` | `ht` | array (array) |
| 아일랜드어 | `host_languages` | `ga` | array (array) |
| 키르기스어 | `host_languages` | `ky` | array (array) |
| 라오스어 | `host_languages` | `lo` | array (array) |
| 라트비아어 | `host_languages` | `lv` | array (array) |
| 리투아니아어 | `host_languages` | `lt` | array (array) |
| 마케도니아어 | `host_languages` | `mk` | array (array) |
| 몰타어 | `host_languages` | `mt` | array (array) |
| 펀자브어 | `host_languages` | `pa` | array (array) |
| 루마니아어 | `host_languages` | `ro` | array (array) |
| 세르비아어 | `host_languages` | `sr` | array (array) |
| 슬로바키아어 | `host_languages` | `sk` | array (array) |
| 슬로베니아어 | `host_languages` | `sl` | array (array) |
| 스와힐리어 | `host_languages` | `sw` | array (array) |
| 타갈로그어 | `host_languages` | `tl` | array (array) |
| 우크라이나어 | `host_languages` | `uk` | array (array) |
| 우르두어 | `host_languages` | `ur` | array (array) |
| 베트남어 | `host_languages` | `vi` | array (array) |
| 수화 | `host_languages` | `sgn` | array (array) |

## `RECOMMENDED_FILTERS` — 1개

| 표시명 | param key | value | type |
|---|---|---|---|
| — | — | — | — |

---

**총 필터 파라미터 매핑: 112개**


## 요금 표시 토글 (`pricingToggle`)

```json
null
```