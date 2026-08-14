# 33m2 — 데이터 모델 (게스트 관점)

> RSC 페이로드 및 `/v1/use-auth/map/rooms` 응답에서 추출한 **실제 필드명·타입·enum**.
> 샘플: `rid=4684` (강남역 초역세권 역삼동)

## ENT-001 `Room` (매물) — 상세 응답

매물 상세 RSC 페이로드의 루트 객체. **56개 필드**.

### 식별/기본
| 필드 | 타입 | 예시 | 비고 |
|---|---|---|---|
| `rid` | int | `4684` | Room ID (PK). URL `/guest/room/{rid}` |
| `roomName` | string | `"강남역 초역세권 역삼동"` | 호스트 작성 제목 |
| `propertyType` | enum | `"STUDIO"` | 아래 enum 참조 |
| `cid` | int\|null | `null` | Contract ID — 조회자의 해당 매물 계약 참조 추정 |
| `roomUrl` | string | | 공유용 URL |
| `translationApplied` | bool | | 기계번역 적용 여부 |

### 주소/위치
| 필드 | 타입 | 예시 |
|---|---|---|
| `addrLot` | string | `"서울특별시 강남구 역삼동 817-37 주건축물제1동 3층"` (지번) |
| `addrStreet` | string | `"서울특별시 강남구 강남대로98길 22 3층"` (도로명) |
| `state` | string | `"서울특별시"` (시/도) |
| `province` | string | `"강남구"` (시/군/구) |
| `town` | string | `"역삼동"` (읍/면/동) |
| `lat` / `lng` | float | `37.50083` / `127.02822` |
| `subwayStations` | string[] | `["강남역", …]` (2개) |
| `transportation` | text | 교통 설명 (호스트 작성) |

> 주소가 **3단 행정구역으로 분해 저장** + 지번/도로명 이중 보관. 검색 필터링·표시명 생성에 사용.

### 구조/규모
| 필드 | 타입 | 예시 |
|---|---|---|
| `roomCnt` / `bathroomCnt` / `cookroomCnt` / `sittingroomCnt` | int | `1/1/1/0` (방/화장실/주방/거실) |
| `sharedRoom` / `sharedBathroom` / `sharedCookroom` | bool | 공유 여부 |
| `duplexStructure` | bool | 복층 여부 |
| `pyeongSize` | int | `5` (평) |
| `squareMeterSize` | number | (㎡) |
| `hasElevator` | bool | |
| `parkingType` | enum | `"NONE"` |
| `parkingNotice` | string | |
| `petAllowed` | bool | |

### 설명 (호스트 자유 입력)
`description`, `additionalDescription`, `usageGuide`, `managementFeeDescription`

### 옵션 (3분할이 핵심 설계)
| 필드 | 의미 |
|---|---|
| `basicOptions` | 기본 옵션 (보유) |
| `additionalOptions` | 추가 옵션 (보유) |
| `missingOptions` | **미보유 옵션 — 명시적으로 "없음"을 표기** |

> 💡 `missingOptions`를 별도 저장하는 게 특징. "있는 것"만 나열하는 Airbnb와 달리 **없는 것도 명시**해 분쟁을 줄이는 설계.

**관찰된 옵션 enum** (합집합, 29종)
```
REFRIGERATOR, WASHING_MACHINE, AIR_CONDITIONER, WIFI, SINK, INDUCTION, BED,
DOOR_LOCK, CCTV, MANAGEMENT_OFFICE, MICROWAVE, DESK, CLOSET, SHOE_RACK,
CURTAINS, AIR_PURIFIER, TV, GAS_STOVE, DINING_TABLE, RICE_COOKER,
WATER_PURIFIER, SOFA, VANITY, BATHTUB, BIDET, DRYER, BALCONY,
DRESSING_ROOM, CABLE_TV
```

### 요금 (핵심 도메인)
| 필드 | 타입 | 예시 | 의미 |
|---|---|---|---|
| `deposit` | int | `330000` | 보증금 — **플랫폼 에스크로 보관, 퇴실 후 반환** |
| `usingFee` | int | `340000` | 임대료 (**주 단위**) |
| `mgmtFee` | int | `50000` | 관리비 (주 단위) |
| `cleanFee` | int | `30000` | 청소비 (1회성 추정) |
| `includeElectricity` / `includeWater` / `includeGas` | bool | `true` | 관리비 포함 항목 |
| `minimumContractWeeks` | int | `1` | 최소 계약 주수 |

**`longTermDiscounts`** — 장기계약 할인 테이블
```jsonc
[ { "weeks": 2, "discountRate": 7,  "discountedUsingFee": 316200 },
  { "weeks": 4, "discountRate": 10, "discountedUsingFee": 306000 } ]
```
> 서버가 할인율과 **계산된 금액을 함께 내려줌** (클라이언트 계산 불일치 방지).

**`earlyCheckinDiscounts`** — 즉시입주 할인
```jsonc
[ { "days": 1, "discountAmount": 7 },   // 1일 내 입주 시 7만원
  { "days": 3, "discountAmount": 5 } ]
```
> `discountAmount` 단위는 **만원** (UI "즉시입주 ~7만 원 할인"과 일치).

### 환불 정책
| 필드 | 값 |
|---|---|
| `refundPolicy` | enum: `"MIDDLE"` (다른 값 미확인 — `FLEXIBLE`/`STRICT` 계열 추정) |
| `refundTerms` | 아래 |

```jsonc
[ { "beforeCheckinDays": 15, "cancelFeePercent": 10 },
  { "beforeCheckinDays": 8,  "cancelFeePercent": 30 },
  { "beforeCheckinDays": 1,  "cancelFeePercent": 50 },
  { "beforeCheckinDays": 0,  "cancelFeePercent": null } ]
```
> 정책명(enum)과 실제 구간 테이블을 **둘 다** 내려줌. 프리셋 선택 + 서버 전개 방식.

### 미디어
| 필드 | 타입 | 비고 |
|---|---|---|
| `pictures` | object[] | 129개 (RSC 참조 형태 `$`) — CDN 경로 + 순서/카테고리 포함 추정 |
| `picMain` | string | 목록 응답에서 대표 이미지 경로 (`room/{uuid}.jpg`) |

### 관계
| 필드 | 대상 |
|---|---|
| `hostUser` | → `Host` |
| `reviewList` | → `Review[]` |
| `simpleReviewCounts` | → `SimpleReviewTag[]` (집계) |
| `otherHostRooms` | → `Room[]` (같은 호스트의 다른 매물) |
| `reviewScore` | float `4.8824` — 매물 평균 평점 |
| `like` | bool — **조회자 기준** 찜 여부 (개인화 필드) |

---

## ENT-002 `Host` (임대인) — `hostUser`

```jsonc
{
  "uid": 21445,
  "picProfile": "profile/{uuid}.png",
  "name": "이윤지",
  "isSuperHost": true,          // UI 배지 "우수 임대인"
  "isCertificated": true,       // 본인/신원 인증
  "introduction": "강남역 초역세권에서 모든 인프라를 누려보세요^^",
  "reviewCount": 51,
  "avgScore": 4.9,
  "firstRoomRegisteredDate": "2022-09-20"   // 호스트 경력 표시용
}
```

> `uid`는 게스트/호스트 공통 User ID로 추정 (동일 계정 모드 전환 구조).

---

## ENT-003 `SimpleReviewTag` (태그형 리뷰) — 설계상 강점

```jsonc
{
  "simpleReviewTemplateId": 1,
  "simpleReviewTemplateCode": "FAST_RESPONSE",
  "content": "신속한 응답",
  "isForHost": true,     // 호스트 평가용 / 매물 평가용 구분
  "count": 2             // 해당 매물에서 이 태그가 선택된 횟수
}
```

**확인된 템플릿**
| id | code | content | isForHost |
|---|---|---|---|
| 1 | `FAST_RESPONSE` | 신속한 응답 | true |
| 2 | `KIND_HOST` | 친절한 임대인 | true |
| 3 | … | (추가 확인 필요) | |

> 💡 자유 텍스트 리뷰 + **정규화된 태그 리뷰**를 병행. 태그는 템플릿 테이블로 관리되고 호스트용/매물용이 분리됨.

---

## ENT-004 `RoomListItem` — 지도/목록 응답

`GET /v1/use-auth/map/rooms` 의 `data.content[]`

```jsonc
{
  "rid": 4684,
  "roomName": "강남역 초역세권 역삼동",
  "state": "서울특별시", "province": "강남구", "town": "역삼동",
  "picMain": "room/{uuid}.jpeg",
  "addrLot": "…", "addrStreet": "…",
  "propertyType": "원룸건물",        // ⚠️ 목록은 한글 표시명, 상세는 enum("STUDIO")
  "usingFee": 340000, "mgmtFee": 50000,
  "pyeongSize": 5,
  "roomCnt": 1, "bathroomCnt": 1, "cookroomCnt": 1, "sittingroomCnt": 0,
  "recoType1": false, "recoType2": false,   // 추천/노출 슬롯 플래그 (의미 미확정)
  "longtermDiscountPer": 10,                 // 최대 장기할인율
  "earlyDiscountAmount": 7,                  // 최대 즉시입주 할인(만원)
  "isNew": false,
  "isSuperHost": true,
  "lat": 37.50083, "lng": 127.02822,
  "like": false
}
```

> ⚠️ **불일치 주의**: 목록은 `propertyType`을 한글 표시명(`"원룸건물"`), 상세는 enum(`"STUDIO"`)으로 내려줌. 우리 서비스에서는 enum으로 통일하고 표시명은 클라이언트 i18n으로 처리할 것.

---

## 미확정 / 추가 확인 필요

- [ ] `propertyType` enum 전체 값 (`STUDIO` 외: 오피스텔/아파트/투룸/쓰리룸+ 확인됨 — 코드값 매핑 필요)
- [ ] `parkingType` enum 전체 값 (`NONE` 외)
- [ ] `refundPolicy` enum 전체 값 (`MIDDLE` 외)
- [ ] `pictures[]` 객체 구조 (카테고리/순서 필드)
- [ ] `recoType1`, `recoType2` 의미
- [ ] `Review` (자유 텍스트) 객체 구조
- [ ] `simpleReviewCounts` 템플릿 전체 목록
- [ ] Contract / Chat / Payment 엔티티 (계약·채팅 화면 미탐색)
