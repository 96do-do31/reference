# 33m2 클라이언트 Zod 스키마 (역추출)

> 출처: `web.33m2.co.kr` JS 번들 35개 청크(2.5MB)에서 `z.object({...})` 정의를 파싱.

> 클라이언트가 API 응답/요청을 Zod로 검증하므로, **이 스키마 = 서버 계약**으로 볼 수 있습니다.

> `z.enum` 은 `nativeEnum(...)` 을 치환한 표기이며, 실제 값은 `33m2/enums.md` 참조.

> ⚠️ 미니파이 코드 파싱이므로 일부 표현식이 잘릴 수 있습니다. 필드명·기본 타입은 신뢰 가능.


## S01 — 42 fields

| field | type |
|---|---|
| `roomName` | `z.string` |
| `propertyType` | `z.enum` |
| `hasElevator` | `z.boolean` |
| `parkingType` | `z.enum` |
| `parkingNotice` | `z.string` |
| `description` | `z.string` |
| `additionalDescription` | `z.string` |
| `usageGuide` | `z.string` |
| `basicOptions` | `z.array(z.enum` |
| `additionalOptions` | `z.array(z.enum` |
| `petAllowed` | `z.boolean` |
| `addrLot` | `z.string` |
| `addrStreet` | `z.string` |
| `addrDetail` | `z.string` |
| `floor` | `z.string` |
| `zipCode` | `z.string` |
| `state` | `z.string` |
| `province` | `z.string` |
| `town` | `z.string` |
| `subwayStations` | `z.array(z.string` |
| `schools` | `z.array(z.string` |
| `usingFee` | `z.number` |
| `mgmtFee` | `z.number` |
| `longTermDiscounts` | `z.array(l` |
| `earlyCheckinDiscounts` | `z.array(i` |
| `includeElectricity` | `z.boolean` |
| `includeWater` | `z.boolean` |
| `includeGas` | `z.boolean` |
| `managementFeeDescription` | `z.string` |
| `cleanFee` | `z.number` |
| `refundPolicy` | `z.enum` |
| `roomCnt` | `z.number` |
| `bathroomCnt` | `z.number` |
| `cookroomCnt` | `z.number` |
| `sittingroomCnt` | `z.number` |
| `sharedRoom` | `z.boolean` |
| `sharedBathroom` | `z.boolean` |
| `sharedCookroom` | `z.boolean` |
| `duplexStructure` | `z.boolean` |
| `pyeongSize` | `z.number` |
| `transportation` | `z.string` |
| `minimumContractWeeks` | `z.number` |

## S02 — 37 fields

| field | type |
|---|---|
| `contractId` | `d.z.number` |
| `contractStatusDescription` | `d.z.string` |
| `cid` | `d.z.number` |
| `week` | `d.z.number` |
| `startDate` | `d.z.string` |
| `endDate` | `d.z.string` |
| `isExtend` | `d.z.boolean` |
| `usingFee` | `d.z.number` |
| `longTermDiscount` | `d.z.number` |
| `earlyDiscount` | `d.z.number` |
| `mgmtFee` | `d.z.number` |
| `cleanFee` | `d.z.number` |
| `refundTerms` | `d.z.array(U` |
| `cancelFee` | `d.z.number().nullable` |
| `cancelFeePercent` | `d.z.number().nullable` |
| `refundAmount` | `d.z.number().nullable` |
| `contractRequestTime` | `d.z.string` |
| `approveTime` | `d.z.string().nullable` |
| `payDeadlineTime` | `d.z.string().nullable` |
| `contractCompleteTime` | `d.z.string().nullable` |
| `checkinTime` | `d.z.string().nullable` |
| `leaveConfirmTime` | `d.z.string().nullable` |
| `checkFinishTime` | `d.z.string().nullable` |
| `cancelTime` | `d.z.string().nullable` |
| `closedTime` | `d.z.string().nullable` |
| `rid` | `d.z.number` |
| `roomName` | `d.z.string` |
| `addrLot` | `d.z.string` |
| `addrStreet` | `d.z.string` |
| `picMain` | `d.z.string().nullable` |
| `hostUid` | `d.z.number` |
| `hostName` | `d.z.string` |
| `hostPhoneNumber` | `d.z.string` |
| `guestUid` | `d.z.number` |
| `guestName` | `d.z.string` |
| `guestPhoneNumber` | `d.z.string` |
| `isRefundAvailable` | `d.z.boolean` |

## S03 — 26 fields

| field | type |
|---|---|
| `propertyType` | `z.enum` |
| `zipCode` | `z.string` |
| `addrLot` | `z.string` |
| `addrStreet` | `z.string` |
| `addrStreetEn` | `z.string` |
| `addrDetail` | `z.string` |
| `floor` | `z.string` |
| `state` | `z.string` |
| `province` | `z.string` |
| `town` | `z.string` |
| `subwayStations` | `z.array(z.string` |
| `schools` | `z.array(z.string` |
| `lat` | `z.number` |
| `lng` | `z.number` |
| `pyeongSize` | `z.number().int` |
| `roomCount` | `z.number().int` |
| `bathroomCount` | `z.number().int` |
| `kitchenCount` | `z.number().int` |
| `livingRoomCount` | `z.number().int` |
| `duplexStructure` | `z.boolean` |
| `sharedRoom` | `z.boolean` |
| `sharedBathroom` | `z.boolean` |
| `sharedKitchen` | `z.boolean` |
| `hasElevator` | `z.boolean` |
| `parkingType` | `z.enum` |
| `parkingNotice` | `z.string` |

## S04 — 24 fields

| field | type |
|---|---|
| `roomName` | `z.string` |
| `state` | `z.string` |
| `province` | `z.string` |
| `town` | `z.string` |
| `picMain` | `z.string().nullable` |
| `addrLot` | `z.string` |
| `addrStreet` | `z.string` |
| `propertyType` | `z.string` |
| `usingFee` | `z.number` |
| `mgmtFee` | `z.number` |
| `pyeongSize` | `z.number` |
| `roomCnt` | `z.number` |
| `bathroomCnt` | `z.number` |
| `cookroomCnt` | `z.number` |
| `sittingroomCnt` | `z.number` |
| `recoType1` | `z.boolean` |
| `recoType2` | `z.boolean` |
| `longtermDiscountPer` | `z.number` |
| `earlyDiscountAmount` | `z.number` |
| `isNew` | `z.boolean` |
| `isSuperHost` | `z.boolean` |
| `lat` | `z.number` |
| `lng` | `z.number` |
| `like` | `z.boolean` |

## S05 — 22 fields

| field | type |
|---|---|
| `roomName` | `z.string` |
| `state` | `z.string` |
| `province` | `z.string` |
| `town` | `z.string` |
| `picMain` | `z.string().nullable` |
| `addrLot` | `z.string` |
| `addrStreet` | `z.string` |
| `propertyType` | `z.string` |
| `usingFee` | `z.number` |
| `mgmtFee` | `z.number` |
| `pyeongSize` | `z.number` |
| `roomCnt` | `z.number` |
| `bathroomCnt` | `z.number` |
| `cookroomCnt` | `z.number` |
| `sittingroomCnt` | `z.number` |
| `recoType1` | `z.boolean` |
| `recoType2` | `z.boolean` |
| `longtermDiscountPer` | `z.number` |
| `earlyDiscountAmount` | `z.number` |
| `isNew` | `z.boolean` |
| `isSuperHost` | `z.boolean` |
| `like` | `z.boolean` |

## S06 — 17 fields

| field | type |
|---|---|
| `email` | `z.string` |
| `name` | `z.string` |
| `profileImageUrl` | `z.string` |
| `phoneNumber` | `z.string` |
| `userType` | `z.enum` |
| `isCertificated` | `z.boolean` |
| `certType` | `z.enum.nullable` |
| `passportImageUrl` | `z.string().nullable` |
| `verificationStatus` | `z.enum` |
| `holdReason` | `z.string().nullable` |
| `detailReason` | `z.string().nullable` |
| `hostIntro` | `z.string` |
| `isSuperHost` | `z.boolean` |
| `bankName` | `z.string` |
| `bankAccount` | `z.string` |
| `bankHolder` | `z.string` |
| `emailCertified` | `z.boolean` |

## S07 — 15 fields

| field | type |
|---|---|
| `reviewingCount` | `d.z.number` |
| `canceledCount` | `d.z.number` |
| `readyCount` | `d.z.number` |
| `paymentCanceledCount` | `d.z.number` |
| `activeCount` | `d.z.number` |
| `terminatingCount` | `d.z.number` |
| `closedCount` | `d.z.number` |
| `reviewingContractRoomPics` | `d.z.array(d.z.string` |
| `canceledContractRoomPics` | `d.z.array(d.z.string` |
| `readyContractRoomPics` | `d.z.array(d.z.string` |
| `paymentCanceledContractRoomPics` | `d.z.array(d.z.string` |
| `activeContractRoomPics` | `d.z.array(d.z.string` |
| `terminatingContractRoomPics` | `d.z.array(d.z.string` |
| `closedContractRoomPics` | `d.z.array(d.z.string` |
| `currentTime` | `d.z.string` |

## S08 — 13 fields

| field | type |
|---|---|
| `initialContractId` | `d.z.number` |
| `rid` | `d.z.number` |
| `roomName` | `d.z.string` |
| `picMain` | `d.z.string().nullable` |
| `startDate` | `d.z.string` |
| `endDate` | `d.z.string` |
| `score` | `d.z.number().nullable` |
| `review` | `d.z.string().nullable` |
| `reviewDate` | `d.z.string().nullable` |
| `simpleReviews` | `d.z.array(d.z.object({templateId:d.z.number(),co` |
| `hostReply` | `d.z.object({hostName:d.z.string(),contents:d.z.s` |
| `isCheckoutConfirmed` | `d.z.boolean` |
| `isDepositReturned` | `d.z.boolean` |

## S09 — 13 fields

| field | type |
|---|---|
| `scheduleId` | `d.z.number` |
| `initialContractId` | `d.z.number` |
| `roomId` | `d.z.number` |
| `roomName` | `d.z.string` |
| `status` | `d.z.enum` |
| `isAnswerable` | `d.z.boolean` |
| `unanswerableReason` | `d.z.enum.nullable` |
| `guestMessage` | `d.z.string().nullable` |
| `currentStartDate` | `d.z.string` |
| `currentEndDate` | `d.z.string` |
| `requestedStartDate` | `d.z.string` |
| `requestedEndDate` | `d.z.string` |
| `requestedAt` | `d.z.string` |

## S10 — 12 fields

| field | type |
|---|---|
| `startDate` | `z.string().optional` |
| `endDate` | `z.string().optional` |
| `minUsingFee` | `z.coerce.number().nullable` |
| `maxUsingFee` | `z.coerce.number().nullable` |
| `roomCounts` | `z.z.array(z.enum` |
| `propertyTypes` | `z.z.array(z.enum` |
| `pyeongSizes` | `z.z.array(z.enum` |
| `floors` | `z.z.array(z.enum` |
| `popularOptions` | `z.z.array(z.enum` |
| `basicOptions` | `z.z.array(z.enum` |
| `additionalOptions` | `z.z.array(z.enum` |
| `roomDiscounts` | `z.z.array(z.enum` |

## S11 — 12 fields

| field | type |
|---|---|
| `email` | `u.z.string` |
| `password` | `u.z.string` |
| `name` | `u.z.string` |
| `certNum` | `u.z.string().optional` |
| `marketingAgree` | `u.z.boolean().optional` |
| `profileImageUrl` | `u.z.string().optional` |
| `passportImageUrl` | `u.z.string().optional` |
| `phoneNumber` | `u.z.string().optional` |
| `hostIntro` | `u.z.string().optional` |
| `recommenderPhoneNumber` | `u.z.string().optional` |
| `ocrToken` | `u.z.string().optional` |
| `emailCertToken` | `u.z.string().optional` |

## S12 — 12 fields

| field | type |
|---|---|
| `sequence` | `d.z.number` |
| `scheduleId` | `d.z.number` |
| `status` | `d.z.enum` |
| `currentStartDate` | `d.z.string` |
| `currentEndDate` | `d.z.string` |
| `requestedStartDate` | `d.z.string` |
| `requestedEndDate` | `d.z.string` |
| `guestMessage` | `d.z.string` |
| `hostMessage` | `d.z.string().nullable` |
| `requestedAt` | `d.z.string` |
| `completedAt` | `d.z.string().nullable` |
| `displaySteps` | `d.z.array(B` |

## S13 — 12 fields

| field | type |
|---|---|
| `initialContractId` | `d.z.number` |
| `contractMasterStatus` | `d.z.enum` |
| `deposit` | `d.z.number` |
| `cid` | `d.z.number` |
| `startDate` | `d.z.string` |
| `endDate` | `d.z.string` |
| `rid` | `d.z.number` |
| `roomName` | `d.z.string` |
| `addrLot` | `d.z.string` |
| `addrStreet` | `d.z.string` |
| `picMain` | `d.z.string().nullable` |
| `isCallAvailable` | `d.z.boolean` |

## S14 — 11 fields

| field | type |
|---|---|
| `usingFee` | `z.number().int` |
| `longTermDiscounts` | `z.array(f` |
| `earlyCheckinDiscounts` | `z.array(D` |
| `managementFee` | `z.number().int` |
| `includeElectricity` | `z.boolean` |
| `includeWater` | `z.boolean` |
| `includeGas` | `z.boolean` |
| `managementFeeDescription` | `z.string().nullable` |
| `cleanFee` | `z.number().int` |
| `refundPolicy` | `z.enum.nullable` |
| `propertyType` | `z.enum` |

## S15 — 11 fields

| field | type |
|---|---|
| `startDate` | `d.z.string` |
| `endDate` | `d.z.string` |
| `usingFee` | `d.z.number` |
| `longTermDiscount` | `d.z.number` |
| `earlyDiscount` | `d.z.number` |
| `mgmtFee` | `d.z.number` |
| `cleanFee` | `d.z.number` |
| `contractFee` | `d.z.number` |
| `realUsingFee` | `d.z.number` |
| `deposit` | `d.z.number` |
| `finalPayFee` | `d.z.number` |

## S16 — 10 fields

| field | type |
|---|---|
| `scheduleId` | `d.z.number` |
| `status` | `d.z.enum` |
| `previousStartDate` | `d.z.string` |
| `previousEndDate` | `d.z.string` |
| `requestedStartDate` | `d.z.string` |
| `requestedEndDate` | `d.z.string` |
| `guestMessage` | `d.z.string().nullable` |
| `hostMessage` | `d.z.string().nullable` |
| `requestedAt` | `d.z.string` |
| `completedAt` | `d.z.string().nullable` |

## S17 — 9 fields

| field | type |
|---|---|
| `currentTime` | `d.z.string` |
| `waitingApprovalCount` | `d.z.number` |
| `waitingCheckinCount` | `d.z.number` |
| `waitingCheckoutCount` | `d.z.number` |
| `waitingCheckFinishCount` | `d.z.number` |
| `waitingApprovalRoomPics` | `d.z.array(d.z.string` |
| `waitingCheckinRoomPics` | `d.z.array(d.z.string` |
| `waitingCheckoutRoomPics` | `d.z.array(d.z.string` |
| `waitingCheckFinishRoomPics` | `d.z.array(d.z.string` |

## S18 — 9 fields

| field | type |
|---|---|
| `initialContractId` | `d.z.number` |
| `roomId` | `d.z.number` |
| `roomName` | `d.z.string` |
| `picMain` | `d.z.string().nullable` |
| `currentStartDate` | `d.z.string` |
| `currentEndDate` | `d.z.string` |
| `totalContractDays` | `d.z.number` |
| `canRequest` | `d.z.boolean` |
| `hasHistory` | `d.z.boolean` |

## S19 — 9 fields

| field | type |
|---|---|
| `uid` | `z.number` |
| `picProfile` | `z.string` |
| `name` | `z.string` |
| `isSuperHost` | `z.boolean` |
| `isCertificated` | `z.boolean` |
| `introduction` | `z.string().nullable` |
| `reviewCount` | `z.number` |
| `avgScore` | `z.number().nullable` |
| `firstRoomRegisteredDate` | `z.string().nullable` |

## S20 — 9 fields

| field | type |
|---|---|
| `roomName` | `z.string` |
| `addrLot` | `z.string` |
| `addrFloor` | `z.string` |
| `addrDetail` | `z.string` |
| `usingFee` | `z.number` |
| `mainImageUrl` | `z.string` |
| `status` | `z.enum` |
| `isPublic` | `z.boolean` |
| `requiredFieldsCompleted` | `z.boolean` |

## S21 — 9 fields

| field | type |
|---|---|
| `scheduleId` | `d.z.number` |
| `status` | `d.z.enum` |
| `roomName` | `d.z.string` |
| `picMain` | `d.z.string` |
| `previousStartDate` | `d.z.string` |
| `previousEndDate` | `d.z.string` |
| `currentStartDate` | `d.z.string` |
| `currentEndDate` | `d.z.string` |
| `hostMessage` | `d.z.string().nullable` |

## S22 — 8 fields

| field | type |
|---|---|
| `contractId` | `z.number` |
| `name` | `z.string` |
| `score` | `z.number` |
| `review` | `z.string` |
| `reviewTime` | `z.string` |
| `replyContents` | `z.string().nullable` |
| `replyCreatedDate` | `z.string().nullable` |
| `hostName` | `z.string().nullable` |

## S23 — 7 fields

| field | type |
|---|---|
| `finalPayFee` | `d.z.number` |
| `cardNo` | `d.z.string().nullable` |
| `cardName` | `d.z.string().nullable` |
| `calculatedCancelFeePercent` | `d.z.number` |
| `calculatedCancelFee` | `d.z.number` |
| `calculatedContractFee` | `d.z.number` |
| `calculatedRefundAmount` | `d.z.number` |

## S24 — 7 fields

| field | type |
|---|---|
| `receiptRequested` | `z.boolean().nullable` |
| `taxReceiptType` | `z.enum.nullable` |
| `issuanceNumber` | `z.string().nullable` |
| `corpId` | `z.string().nullable` |
| `corpName` | `z.string().nullable` |
| `corpCeo` | `z.string().nullable` |
| `invoiceeEmail` | `z.string().nullable` |

## S25 — 7 fields

| field | type |
|---|---|
| `name` | `d.z.string` |
| `startDate` | `d.z.string` |
| `endDate` | `d.z.string` |
| `address` | `d.z.string` |
| `amount` | `d.z.number` |
| `method` | `d.z.string` |
| `paymentDate` | `d.z.string` |

## S26 — 7 fields

| field | type |
|---|---|
| `contractId` | `d.z.number` |
| `score` | `d.z.number` |
| `review` | `d.z.string` |
| `rid` | `d.z.number` |
| `roomName` | `d.z.string` |
| `roomAddress` | `d.z.string` |
| `picMain` | `d.z.string` |

## S27 — 6 fields

| field | type |
|---|---|
| `category` | `x.z.string` |
| `action` | `x.z.string().optional` |
| `label` | `x.z.string().optional` |
| `value` | `x.z.number().optional` |
| `semanticAttributes` | `x.z.record(x.z.string(),x.z.unknown()).optional` |
| `customAttributes` | `x.z.record(x.z.string(),x.z.unknown()).optional` |

## S28 — 6 fields

| field | type |
|---|---|
| `depositReturnBankName` | `d.z.string().nullable` |
| `depositReturnBankAccount` | `d.z.string().nullable` |
| `depositReturnBankHolder` | `d.z.string().nullable` |
| `isDepositReturned` | `d.z.boolean` |
| `depositReturnedAt` | `d.z.string().nullable` |
| `isEditAvailable` | `d.z.boolean` |

## S29 — 6 fields

| field | type |
|---|---|
| `calculatedCancelFeePercent` | `d.z.number` |
| `calculatedCancelFee` | `d.z.number` |
| `refundAccountBankName` | `d.z.string().nullable` |
| `refundAccount` | `d.z.string().nullable` |
| `refundAccountHolder` | `d.z.string().nullable` |
| `refundTerms` | `d.z.array(U` |

## S30 — 6 fields

| field | type |
|---|---|
| `roomName` | `z.string` |
| `roomImages` | `z.array(R` |
| `description` | `z.string().nullable` |
| `transportation` | `z.string().nullable` |
| `usageGuide` | `z.string().nullable` |
| `additionalDescription` | `z.string().nullable` |

## S31 — 6 fields

| field | type |
|---|---|
| `initialContractId` | `d.z.number` |
| `lastContractId` | `d.z.number` |
| `startDate` | `d.z.string` |
| `endDate` | `d.z.string` |
| `extendContractStartDate` | `d.z.string` |
| `isExtendContractAvailable` | `d.z.boolean` |

## S32 — 6 fields

| field | type |
|---|---|
| `eventType` | `i.z.enum(["click-keyword"]` |
| `keyword` | `i.z.string` |
| `type` | `i.z.enum` |
| `dataCount` | `i.z.number` |
| `markerName` | `i.z.string` |
| `selectedIndex` | `i.z.number` |

## S33 — 5 fields

| field | type |
|---|---|
| `fromDate` | `d.z.string().nullable` |
| `toDate` | `d.z.string().nullable` |
| `fromDateDiffDays` | `d.z.number().nullable` |
| `toDateDiffDays` | `d.z.number().nullable` |
| `cancelFeePercent` | `d.z.number().nullable` |

## S34 — 5 fields

| field | type |
|---|---|
| `refundBankName` | `d.z.string().nullable` |
| `refundBankAccount` | `d.z.string().nullable` |
| `refundBankHolder` | `d.z.string().nullable` |
| `isRefunded` | `d.z.boolean` |
| `refundedAt` | `d.z.string().nullable` |

## S35 — 5 fields

| field | type |
|---|---|
| `available` | `d.z.boolean` |
| `requestedStartDate` | `d.z.string` |
| `requestedEndDate` | `d.z.string` |
| `unavailableReason` | `d.z.enum.nullable` |
| `conflictPeriod` | `d.z.string().nullable` |

## S36 — 5 fields

| field | type |
|---|---|
| `cardName` | `d.z.string` |
| `cardNo` | `d.z.string` |
| `isDepositReturned` | `d.z.boolean` |
| `depositReturnedAt` | `d.z.string().nullable` |
| `cardReceiptUrl` | `d.z.string` |

## S37 — 5 fields

| field | type |
|---|---|
| `contractId` | `d.z.number` |
| `contractStatusDescription` | `d.z.string` |
| `week` | `d.z.number` |
| `startDate` | `d.z.string` |
| `endDate` | `d.z.string` |

## S38 — 5 fields

| field | type |
|---|---|
| `simpleReviewTemplateId` | `z.number` |
| `simpleReviewTemplateCode` | `z.string` |
| `content` | `z.string` |
| `isForHost` | `z.boolean` |
| `count` | `z.number` |

## S39 — 5 fields

| field | type |
|---|---|
| `cardName` | `d.z.string` |
| `cardNo` | `d.z.string` |
| `isRefunded` | `d.z.boolean` |
| `refundedAt` | `d.z.string().nullable` |
| `cardReceiptUrl` | `d.z.string` |

## S40 — 5 fields

| field | type |
|---|---|
| `companyName` | `d.z.string` |
| `ceoName` | `d.z.string` |
| `businessNumber` | `d.z.string` |
| `customerService` | `d.z.string` |
| `address` | `d.z.string` |

## S41 — 5 fields

| field | type |
|---|---|
| `spaceInfo` | `z.boolean` |
| `feeInfo` | `z.boolean` |
| `options` | `z.boolean` |
| `description` | `z.boolean` |
| `contractPolicy` | `z.boolean` |

## S42 — 4 fields

| field | type |
|---|---|
| `accessToken` | `u.z.string` |
| `refreshToken` | `u.z.string` |
| `firebaseToken` | `u.z.string` |
| `airbridgeUid` | `u.z.string` |

## S43 — 4 fields

| field | type |
|---|---|
| `status` | `d.z.enum.nullable` |
| `failedReason` | `d.z.string().nullable` |
| `billUrl` | `d.z.string().nullable` |
| `isEditAvailable` | `d.z.boolean().nullable` |

## S44 — 4 fields

| field | type |
|---|---|
| `step` | `d.z.enum` |
| `displayStatus` | `d.z.enum(["COMPLETED","CURRENT"]` |
| `displayedAt` | `d.z.string().nullable` |
| `periods` | `d.z.array(Y` |