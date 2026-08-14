# 33m2 데이터 모델 — 앱 DTO 전량 (APK 정적 분석) ★

> 출처: 안드로이드 앱 `network/model/` 의 Gson `@SerializedName` 모델 클래스.

> **179 클래스 / 1,045 필드** — 필드명·타입·(널러블 추정)이 코드 그대로.

> 웹 RSC/Zod 추출과 교차검증되며, 이쪽이 더 완전합니다. 원본: `_shared/captures/33m2.dto.json`

> 타입: Kotlin 원형 (`long`=금액/타임스탬프, `int`, `String`, `boolean`, `List X`). `Integer`/`Long`(박스형) = nullable 추정.


## User/Auth


### `CertNumResult` (1)

| field | type |
|---|---|
| `certNum` | String |

### `EmailVerifyCodeResult` (1)

| field | type |
|---|---|
| `expiresIn` | int |

### `FindMemberIdResult` (1)

| field | type |
|---|---|
| `username` | String |

### `JoinResult` (3)

| field | type |
|---|---|
| `airbridgeData` | NewAirBridgeEventData |
| `airbridgeUid` | String |
| `googleAnalyticsEventData` | GoogleAnalyticsEventData |

### `LoginResult` (11)

| field | type |
|---|---|
| `accessToken` | String |
| `airbridgeUid` | String |
| `blocked` | boolean |
| `certified` | boolean |
| `firebaseToken` | String |
| `name` | String |
| `profileImageUrl` | String |
| `refreshToken` | String |
| `uid` | int |
| `userType` | String |
| `verificationStatus` | String |

### `MobileCertNumResendResult` (2)

| field | type |
|---|---|
| `expiresIn` | int |
| `resendCount` | String |

### `MobileCertNumResult` (3)

| field | type |
|---|---|
| `expiresIn` | int |
| `resendCount` | String |
| `txKey` | String |

### `MobileCertTerm` (2)

| field | type |
|---|---|
| `required` | Boolean |
| `viewUrl` | String |

### `MobileCertTermsResult` (1)

| field | type |
|---|---|
| `terms` | List MobileCertTerm |

### `PassportOcrResult` (1)

| field | type |
|---|---|
| `ocrToken` | String |

### `RefreshTokenResult` (2)

| field | type |
|---|---|
| `accessToken` | String |
| `refreshToken` | String |

### `UserMe` (23)

| field | type |
|---|---|
| `bankAccount` | String |
| `bankHolder` | String |
| `bankName` | String |
| `certType` | String |
| `corpCeo` | String |
| `corpId` | String |
| `corpName` | String |
| `detailReason` | String |
| `emailCertified` | boolean |
| `holdReason` | String |
| `hostIntro` | String |
| `invoiceeEmail` | String |
| `isCertificated` | boolean |
| `isSuperHost` | boolean |
| `issuanceNumber` | String |
| `name` | String |
| `passportImageUrl` | String |
| `phoneNumber` | String |
| `profileImageUrl` | String |
| `receiptRequested` | Boolean |
| `taxReceiptType` | String |
| `userType` | String |
| `verificationStatus` | String |

## Room


### `HostRoomListData` (1)

| field | type |
|---|---|
| `content` | List HostRoomItem |

### `LocationMakerItem` (6)

| field | type |
|---|---|
| `fullName` | String |
| `lat` | double |
| `lng` | double |
| `name` | String |
| `nextZoomLevel` | Integer |
| `subwayLines` | List SubwayItem |

### `MapRoomSearchResult` (1)

| field | type |
|---|---|
| `content` | List RoomListItem |

### `OverViewAddressInfo` (12)

| field | type |
|---|---|
| `addrDetail` | String |
| `addrLot` | String |
| `addrStreet` | String |
| `addrStreetEn` | String |
| `floor` | String |
| `lat` | Double |
| `lng` | Double |
| `province` | String |
| `schools` | List String |
| `subwayStations` | List String |
| `town` | String |
| `zipCode` | String |

### `OverViewDiscountInfo` (2)

| field | type |
|---|---|
| `earlyCheckinDiscounts` | List EarlyCheckInDiscountItem |
| `longTermDiscounts` | List LongTermDiscountItem |

### `OverViewMaintenanceFeeInfo` (6)

| field | type |
|---|---|
| `cleanFee` | Integer |
| `includeElectricity` | Boolean |
| `includeGas` | Boolean |
| `includeWater` | Boolean |
| `managementFee` | Integer |
| `managementFeeDescription` | String |

### `OverViewRoomDescription` (3)

| field | type |
|---|---|
| `additionalDescription` | String |
| `transportation` | String |
| `usageGuide` | String |

### `OverViewSpaceAdditionalInfo` (3)

| field | type |
|---|---|
| `hasElevator` | Boolean |
| `parkingNotice` | String |
| `parkingType` | String |

### `OverViewSpaceStructure` (8)

| field | type |
|---|---|
| `bathroomCount` | Integer |
| `duplexStructure` | Boolean |
| `kitchenCount` | Integer |
| `livingRoomCount` | Integer |
| `roomCount` | Integer |
| `sharedBathroom` | Boolean |
| `sharedKitchen` | Boolean |
| `sharedRoom` | Boolean |

### `RoomBasicInfo` (1)

| field | type |
|---|---|
| `rid` | int |

### `RoomContractAvailableWeeks` (2)

| field | type |
|---|---|
| `maxAvailableWeeks` | int |
| `minAvailableWeeks` | int |

### `RoomDetailInfoResult` (57)

| field | type |
|---|---|
| `additionalDescription` | String |
| `additionalOptions` | List String |
| `addrLot` | String |
| `addrStreet` | String |
| `airbridgeEvent` | NewAirBridgeEventData |
| `basicOptions` | List String |
| `bathroomCnt` | int |
| `cid` | Integer |
| `cleanFee` | int |
| `cookroomCnt` | int |
| `deposit` | int |
| `duplexStructure` | boolean |
| `earlyCheckinDiscounts` | List EarlyCheckInDiscountItem |
| `hasElevator` | Boolean |
| `hostUser` | RoomHostInfo |
| `includeElectricity` | boolean |
| `includeGas` | boolean |
| `includeInternet` | Boolean |
| `includeWater` | boolean |
| `isOldRefundTerms` | Boolean |
| `isOldRoomOptions` | Boolean |
| `lat` | Double |
| `like` | boolean |
| `lng` | Double |
| `longTermDiscounts` | List LongTermDiscountItem |
| `managementFeeDescription` | String |
| `mgmtFee` | int |
| `minimumContractWeeks` | int |
| `missingOptions` | List String |
| `oldAdditionalOptions` | List String |
| `otherHostRooms` | List RoomBasicInfo |
| `parkingNotice` | String |
| `parkingType` | String |
| `petAllowed` | Boolean |
| `propertyType` | String |
| `province` | String |
| `pyeongSize` | int |
| `refundPolicy` | String |
| `refundTerms` | List RoomDetailRefundItem |
| `reviewList` | ArrayList RoomDetailReviewItem |
| `reviewScore` | Double |
| `rid` | int |
| `roomCnt` | int |
| `pictures` | ArrayList String |
| `roomName` | String |
| `roomUrl` | String |
| `sharedBathroom` | boolean |
| `sharedCookroom` | boolean |
| `sharedRoom` | boolean |
| `simpleReviewCounts` | List SimpleReviewData |
| `sittingroomCnt` | int |
| `squareMeterSize` | double |
| `subwayStations` | List String |
| `town` | String |
| `transportation` | String |
| `usageGuide` | String |
| `usingFee` | int |

### `RoomDetailRefundItem` (2)

| field | type |
|---|---|
| `beforeCheckinDays` | int |
| `cancelFeePercent` | Integer |

### `RoomDetailReviewItem` (8)

| field | type |
|---|---|
| `contractId` | int |
| `hostName` | String |
| `name` | String |
| `replyContents` | String |
| `replyCreatedDate` | String |
| `review` | String |
| `reviewTime` | String |
| `score` | int |

### `RoomHostInfo` (6)

| field | type |
|---|---|
| `avgScore` | Double |
| `firstRoomRegisteredDate` | String |
| `isSuperHost` | boolean |
| `name` | String |
| `reviewCount` | Long |
| `simpleReviewCounts` | List SimpleReviewCount |

### `RoomImage` (1)

| field | type |
|---|---|
| `objectKey` | String |

### `RoomInfoOverView` (17)

| field | type |
|---|---|
| `addressInfo` | OverViewAddressInfo |
| `allowCheckinDayContract` | Boolean |
| `allowCheckoutDayContract` | Boolean |
| `discountInfo` | OverViewDiscountInfo |
| `maintenanceFeeInfo` | OverViewMaintenanceFeeInfo |
| `minimumContractWeeks` | Integer |
| `propertyType` | String |
| `pyeongSize` | Integer |
| `refundPolicy` | String |
| `roomDescription` | OverViewRoomDescription |
| `roomImages` | List RoomImage |
| `roomName` | String |
| `roomOption` | HouseOptionInfo |
| `roomStatus` | String |
| `spaceAdditionalInfo` | OverViewSpaceAdditionalInfo |
| `spaceStructure` | OverViewSpaceStructure |
| `usingFee` | Integer |

### `RoomListData` (1)

| field | type |
|---|---|
| `content` | ArrayList RoomListItem |

### `RoomListItem` (22)

| field | type |
|---|---|
| `addrLot` | String |
| `addrStreet` | String |
| `bathroomCnt` | int |
| `cookroomCnt` | int |
| `earlyDiscountAmount` | int |
| `recoType2` | boolean |
| `isNew` | boolean |
| `recoType1` | boolean |
| `isSuperHost` | boolean |
| `like` | boolean |
| `longtermDiscountPer` | int |
| `mgmtFee` | long |
| `picMain` | String |
| `propertyType` | String |
| `province` | String |
| `pyeongSize` | int |
| `rid` | int |
| `roomCnt` | int |
| `roomName` | String |
| `sittingroomCnt` | int |
| `town` | String |
| `usingFee` | long |

### `RoomScheduleData` (2)

| field | type |
|---|---|
| `contracts` | List ContractScheduleItem |
| `schedules` | ArrayList RoomScheduleItem |

### `RoomScheduleItem` (2)

| field | type |
|---|---|
| `date` | String |
| `status` | String |

### `RoomSearchResult` (1)

| field | type |
|---|---|
| `rooms` | RoomListData |

### `SimpleHouseData` (3)

| field | type |
|---|---|
| `picMain` | String |
| `name` | String |
| `rid` | int |

### `SubwayItem` (3)

| field | type |
|---|---|
| `color` | String |
| `displayName` | String |
| `name` | String |

## HostRoom(등록)


### `ContractProgress` (1)

| field | type |
|---|---|
| `currentStep` | String |

### `ContractProgressItem` (3)

| field | type |
|---|---|
| `displayStatus` | String |
| `displayedAt` | String |
| `step` | String |

### `EarlyCheckInDiscountItem` (2)

| field | type |
|---|---|
| `days` | int |
| `discountAmount` | int |

### `EditRoomErrorData` (13)

| field | type |
|---|---|
| `addressInfo` | String |
| `maintenanceFeeInfo` | String |
| `minimumContractWeeks` | String |
| `propertyType` | String |
| `pyeongSize` | String |
| `refundPolicy` | String |
| `roomDescription` | String |
| `roomImages` | String |
| `roomName` | String |
| `roomOption` | String |
| `spaceAdditionalInfo` | String |
| `spaceStructure` | String |
| `usingFee` | String |

### `HostRoomItem` (11)

| field | type |
|---|---|
| `addrDetail` | String |
| `addrFloor` | String |
| `addrLot` | String |
| `mainImageUrl` | String |
| `isPublic` | boolean |
| `requiredFieldsCompleted` | boolean |
| `rid` | int |
| `roomName` | String |
| `status` | String |
| `stepCompletionStatus` | StepCompletionStatus |
| `usingFee` | Long |

### `HostRoomSummary` (4)

| field | type |
|---|---|
| `registeredRooms` | List SimpleHouseData |
| `rejectedRooms` | List SimpleHouseData |
| `reviewingRooms` | List SimpleHouseData |
| `savingRooms` | List SimpleHouseData |

### `HouseContractPolicyInfo` (3)

| field | type |
|---|---|
| `allowCheckinDayContract` | Boolean |
| `allowCheckoutDayContract` | Boolean |
| `minimumContractWeeks` | Integer |

### `HouseDescriptionInfo` (5)

| field | type |
|---|---|
| `additionalDescription` | String |
| `roomImages` | List RoomImage |
| `roomName` | String |
| `transportation` | String |
| `usageGuide` | String |

### `HouseOptionInfo` (3)

| field | type |
|---|---|
| `additionalOptions` | List String |
| `basicOptions` | List String |
| `petAllowed` | Boolean |

### `HousePriceInfo` (11)

| field | type |
|---|---|
| `cleanFee` | Integer |
| `earlyCheckinDiscounts` | List EarlyCheckInDiscountItem |
| `includeElectricity` | Boolean |
| `includeGas` | Boolean |
| `includeWater` | Boolean |
| `longTermDiscounts` | List LongTermDiscountItem |
| `managementFee` | Integer |
| `managementFeeDescription` | String |
| `propertyType` | String |
| `refundPolicy` | String |
| `usingFee` | Integer |

### `HouseSpaceInfo` (25)

| field | type |
|---|---|
| `addrDetail` | String |
| `addrLot` | String |
| `addrStreet` | String |
| `addrStreetEn` | String |
| `bathroomCount` | Integer |
| `duplexStructure` | Boolean |
| `floor` | String |
| `hasElevator` | Boolean |
| `kitchenCount` | Integer |
| `lat` | Double |
| `livingRoomCount` | Integer |
| `lng` | Double |
| `parkingNotice` | String |
| `parkingType` | String |
| `propertyType` | String |
| `province` | String |
| `pyeongSize` | Integer |
| `roomCount` | Integer |
| `schools` | List String |
| `sharedBathroom` | Boolean |
| `sharedKitchen` | Boolean |
| `sharedRoom` | Boolean |
| `subwayStations` | List String |
| `town` | String |
| `zipCode` | String |

### `LongTermDiscountItem` (3)

| field | type |
|---|---|
| `discountRate` | int |
| `discountedUsingFee` | Integer |
| `weeks` | int |

### `NewRoomRegistResult` (1)

| field | type |
|---|---|
| `rid` | int |

### `RefundTerm` (5)

| field | type |
|---|---|
| `cancelFeePercent` | Integer |
| `fromDate` | String |
| `fromDateDiffDays` | Integer |
| `toDate` | String |
| `toDateDiffDays` | Integer |

### `RoomCopyResult` (1)

| field | type |
|---|---|
| `rid` | int |

### `RoomInfoProgress` (3)

| field | type |
|---|---|
| `requiredFieldsCompleted` | boolean |
| `roomStatus` | String |
| `stepCompletionStatus` | StepCompletionStatus |

### `StepCompletionStatus` (4)

| field | type |
|---|---|
| `contractPolicy` | boolean |
| `feeInfo` | boolean |
| `options` | boolean |
| `spaceInfo` | boolean |

## Contract


### `CancelReason` (2)

| field | type |
|---|---|
| `code` | String |
| `label` | String |

### `ContractScheduleItem` (4)

| field | type |
|---|---|
| `checkoutDate` | String |
| `endDate` | String |
| `initialContractId` | String |
| `startDate` | String |

### `ContractScheduleResult` (12)

| field | type |
|---|---|
| `activeScheduleChange` | ScheduleChangeDetail |
| `canRequest` | boolean |
| `contractProgress` | ContractProgress |
| `currentEndDate` | String |
| `currentStartDate` | String |
| `hasHistory` | boolean |
| `initialContractId` | int |
| `latestScheduleChange` | ScheduleChangeDetail |
| `picMain` | String |
| `roomId` | int |
| `roomName` | String |
| `totalContractDays` | int |

### `GuestCheckInInfo` (4)

| field | type |
|---|---|
| `depositReturnAccountInfo` | DepositReturnAccount |
| `payType` | String |
| `receiptInfo` | ReceiptInfo |
| `roomName` | String |

### `GuestCheckOutCheckListResult` (8)

| field | type |
|---|---|
| `initialContractPayType` | String |
| `isInterimLeave` | boolean |
| `isReviewAvailable` | Boolean |
| `isScoreAvailable` | Boolean |
| `isSimpleReviewExists` | Boolean |
| `picMain` | String |
| `rid` | int |
| `roomName` | String |

### `GuestContractDetailResult` (65)

| field | type |
|---|---|
| `addrLot` | String |
| `addrStreet` | String |
| `approveTime` | String |
| `cancelFee` | long |
| `cancelFeePercent` | Integer |
| `cancelTime` | String |
| `checkFinishTime` | String |
| `checkinTime` | String |
| `cid` | int |
| `cleanFee` | long |
| `closedTime` | String |
| `contractCompleteTime` | String |
| `contractFee` | long |
| `contractGuideUrl` | String |
| `contractId` | int |
| `contractRequestTime` | String |
| `contractStatus` | String |
| `contractStatusDescription` | String |
| `deposit` | int |
| `earlyDiscount` | long |
| `endDate` | String |
| `finalContractFee` | Integer |
| `finalPayFee` | long |
| `guestName` | String |
| `guestPhoneNumber` | String |
| `guestUid` | int |
| `hasDepositReturnAccountInfo` | boolean |
| `hasReceiptInfo` | boolean |
| `hostName` | String |
| `hostPhoneNumber` | String |
| `hostUid` | int |
| `initialContractId` | int |
| `isCancelAvailable` | boolean |
| `isContractRefundAccountAvailable` | boolean |
| `isContractRefundCardAvailable` | boolean |
| `isContractTaxInfoAvailable` | boolean |
| `isDepositReturnAccountAvailable` | boolean |
| `isDepositReturnCardAvailable` | boolean |
| `isExtend` | boolean |
| `isOldRefundTerms` | boolean |
| `isPayAvailable` | boolean |
| `isRefundAvailable` | boolean |
| `kakaoPayTransferMobileUrl` | String |
| `leaveConfirmTime` | String |
| `longTermDiscount` | long |
| `mgmtFee` | long |
| `nowTime` | String |
| `payDeadlineTime` | String |
| `payType` | String |
| `paymentWebViewUrl` | String |
| `picMain` | String |
| `realUsingFee` | long |
| `refundAmount` | Integer |
| `refundTerms` | ArrayList RefundTerm |
| `refundType` | String |
| `rid` | int |
| `roomName` | String |
| `scheduleChangeInfo` | ScheduleChangeInfo |
| `startDate` | String |
| `statementUrl` | String |
| `usingFee` | long |
| `vaAccount` | String |
| `vaAccountHolder` | String |
| `vaBankName` | String |
| `week` | int |

### `GuestContractEstimateResult` (21)

| field | type |
|---|---|
| `addrLot` | String |
| `addrStreet` | String |
| `cleanFee` | long |
| `contractFee` | long |
| `deposit` | int |
| `earlyDiscount` | long |
| `endDate` | String |
| `finalPayFee` | long |
| `guestName` | String |
| `guestPhoneNumber` | String |
| `hostName` | String |
| `hostPhoneNumber` | String |
| `longTermDiscount` | long |
| `mgmtFee` | long |
| `picMain` | String |
| `realUsingFee` | long |
| `refundTerms` | ArrayList RefundTerm |
| `roomName` | String |
| `startDate` | String |
| `usingFee` | long |
| `week` | int |

### `GuestContractItem` (33)

| field | type |
|---|---|
| `addrLot` | String |
| `addrStreet` | String |
| `cid` | int |
| `contractList` | List GuestContractSubItem |
| `contractMasterStatus` | String |
| `contractMasterStatusDescription` | String |
| `deposit` | int |
| `endDate` | String |
| `extendContractStartDate` | String |
| `hostName` | String |
| `hostPhoneNumber` | String |
| `hostUid` | int |
| `initialContractApproveTime` | String |
| `initialContractCheckinTime` | String |
| `initialContractCompleteTime` | String |
| `initialContractId` | int |
| `initialContractRequestTime` | String |
| `isCallAvailable` | boolean |
| `isCheckinAvailable` | boolean |
| `isCheckoutAvailable` | boolean |
| `isContractReRequestAvailable` | boolean |
| `isExtendContractAvailable` | boolean |
| `isFindAnotherRoomAvailable` | boolean |
| `isReviewAvailable` | boolean |
| `isScoreAvailable` | boolean |
| `lastContractCheckFinishTime` | String |
| `lastContractClosedTime` | String |
| `lastContractLeaveConfirmTime` | String |
| `picMain` | String |
| `rid` | int |
| `roomName` | String |
| `startDate` | String |
| `tooltipMessage` | GuestTooltipMessageData |

### `GuestContractRequestResult` (2)

| field | type |
|---|---|
| `airbridgeEvent` | NewAirBridgeEventData |
| `contractId` | int |

### `GuestContractSubItem` (7)

| field | type |
|---|---|
| `contractId` | int |
| `contractStatus` | String |
| `contractStatusDescription` | String |
| `endDate` | String |
| `finalPayFee` | int |
| `startDate` | String |
| `week` | int |

### `HostContractCancelRefundInfo` (7)

| field | type |
|---|---|
| `calculatedCancelFee` | long |
| `calculatedCancelFeePercent` | int |
| `refundAccount` | String |
| `refundAccountBankName` | String |
| `refundAccountHolder` | String |
| `refundTerms` | ArrayList RefundTerm |
| `refundType` | String |

### `HostContractDetailResult` (49)

| field | type |
|---|---|
| `addrLot` | String |
| `addrStreet` | String |
| `approveTime` | String |
| `cancelFee` | long |
| `cancelFeePercent` | int |
| `cancelTime` | String |
| `checkFinishTime` | String |
| `checkinTime` | String |
| `cid` | int |
| `cleanFee` | long |
| `closedTime` | String |
| `contractCompleteTime` | String |
| `contractId` | int |
| `contractRequestTime` | String |
| `contractStatus` | String |
| `contractStatusDescription` | String |
| `earlyDiscount` | long |
| `endDate` | String |
| `guestName` | String |
| `guestPhoneNumber` | String |
| `guestUid` | int |
| `hostName` | String |
| `hostPayAmount` | long |
| `hostPayAmountBeforeOtherFee` | long |
| `hostPayDescription` | String |
| `hostPayTime` | String |
| `hostPhoneNumber` | String |
| `hostUid` | int |
| `isApproveRejectAvailable` | boolean |
| `isExtend` | boolean |
| `isRefundAvailable` | boolean |
| `leaveConfirmTime` | String |
| `longTermDiscount` | long |
| `mgmtFee` | long |
| `payDeadlineTime` | String |
| `picMain` | String |
| `refundAccount` | String |
| `refundAccountBankName` | String |
| `refundAmount` | long |
| `refundTerms` | ArrayList RefundTerm |
| `refundType` | String |
| `rid` | int |
| `roomName` | String |
| `scheduleChangeInfo` | ScheduleChangeInfo |
| `serviceFee` | long |
| `startDate` | String |
| `totalUsingFee` | long |
| `usingFee` | long |
| `week` | int |

### `HostContractItem` (23)

| field | type |
|---|---|
| `addrLot` | String |
| `addrStreet` | String |
| `cid` | int |
| `contractList` | List HostContractSubItem |
| `contractMasterStatus` | String |
| `contractMasterStatusDescription` | String |
| `deposit` | int |
| `endDate` | String |
| `guestName` | String |
| `guestPhoneNumber` | String |
| `guestUid` | int |
| `initialContractId` | int |
| `isCallAvailable` | boolean |
| `isCheckFinishAvailable` | boolean |
| `isDepositDeferAvailable` | boolean |
| `isDepositDeferReleaseAvailable` | boolean |
| `picMain` | String |
| `rid` | int |
| `roomName` | String |
| `samsamCareUrl` | String |
| `scheduleChangeAnswerAlert` | ScheduleChangeAnswerAlert |
| `startDate` | String |
| `tooltipMessage` | HostTooltipMessageData |

### `HostContractSubItem` (9)

| field | type |
|---|---|
| `contractId` | int |
| `contractStatus` | String |
| `contractStatusDescription` | String |
| `endDate` | String |
| `hostPayAmount` | Long |
| `hostPayTime` | String |
| `startDate` | String |
| `totalUsingFee` | long |
| `week` | int |

### `LastActiveContract` (6)

| field | type |
|---|---|
| `endDate` | String |
| `extendContractStartDate` | String |
| `initialContractId` | int |
| `isExtendContractAvailable` | boolean |
| `lastContractId` | int |
| `startDate` | String |

### `RefundCheckListResult` (10)

| field | type |
|---|---|
| `calculatedCancelFee` | int |
| `calculatedCancelFeePercent` | int |
| `calculatedContractFee` | int |
| `calculatedRefundAmount` | int |
| `cardName` | String |
| `cardNo` | String |
| `finalPayFee` | int |
| `payType` | String |
| `receiptInfo` | ReceiptInfo |
| `refundAccountInfo` | RefundAccountInfo |

## ScheduleChange


### `ChangeScheduleAvailableResult` (3)

| field | type |
|---|---|
| `available` | boolean |
| `requestedEndDate` | String |
| `requestedStartDate` | String |

### `ChangeScheduleRequestData` (13)

| field | type |
|---|---|
| `currentEndDate` | String |
| `currentStartDate` | String |
| `guestMessage` | String |
| `initialContractId` | int |
| `isAnswerable` | boolean |
| `requestedAt` | String |
| `requestedEndDate` | String |
| `requestedStartDate` | String |
| `roomId` | int |
| `roomName` | String |
| `scheduleId` | int |
| `status` | String |
| `unanswerableReason` | String |

### `ChangeScheduleRequestResult` (4)

| field | type |
|---|---|
| `requestedEndDate` | String |
| `requestedStartDate` | String |
| `scheduleId` | int |
| `status` | String |

### `ScheduleChangeAnswerAlert` (4)

| field | type |
|---|---|
| `isAnswerable` | boolean |
| `requestedEndDate` | String |
| `requestedStartDate` | String |
| `scheduleId` | int |

### `ScheduleChangeDetail` (14)

| field | type |
|---|---|
| `answerDeadlineDate` | String |
| `canAnswer` | Boolean |
| `canCancel` | Boolean |
| `completedAt` | String |
| `guestMessage` | String |
| `hostMessage` | String |
| `previousEndDate` | String |
| `previousStartDate` | String |
| `requestedAt` | String |
| `requestedEndDate` | String |
| `requestedStartDate` | String |
| `scheduleId` | int |
| `status` | String |
| `unanswerableReason` | String |

### `ScheduleChangeHistoryItem` (12)

| field | type |
|---|---|
| `completedAt` | String |
| `currentEndDate` | String |
| `currentStartDate` | String |
| `displaySteps` | List DisplayStepItem |
| `guestMessage` | String |
| `hostMessage` | String |
| `requestedAt` | String |
| `requestedEndDate` | String |
| `requestedStartDate` | String |
| `scheduleId` | int |
| `sequence` | int |
| `status` | String |

### `ScheduleChangeHistoryResult` (2)

| field | type |
|---|---|
| `history` | List ScheduleChangeHistoryItem |
| `initialContractId` | int |

### `ScheduleChangeInfo` (3)

| field | type |
|---|---|
| `hasChangedFromOriginal` | boolean |
| `originalEndDate` | String |
| `originalStartDate` | String |

### `ScheduleChangeResult` (9)

| field | type |
|---|---|
| `currentEndDate` | String |
| `currentStartDate` | String |
| `hostMessage` | String |
| `picMain` | String |
| `previousEndDate` | String |
| `previousStartDate` | String |
| `roomName` | String |
| `scheduleId` | int |
| `status` | String |

## Settlement/Payout


### `PayoutDetail` (27)

| field | type |
|---|---|
| `bankAccount` | String |
| `bankHolder` | String |
| `bankName` | String |
| `cancelFee` | Long |
| `cancelFeePercent` | Integer |
| `cleanFee` | long |
| `contractId` | int |
| `earlyDiscount` | long |
| `endDate` | String |
| `finalServiceFee` | long |
| `guestName` | String |
| `hostBankAccount` | String |
| `hostBankHolder` | String |
| `hostBankName` | String |
| `hostPayAmount` | long |
| `hostPayAmountBeforeOtherFee` | Long |
| `isCanceled` | boolean |
| `longTermDiscount` | long |
| `mgmtFee` | long |
| `refundAmount` | Long |
| `roomName` | String |
| `serviceFeeDiscount` | long |
| `settlementDate` | String |
| `settlementDueDate` | String |
| `startDate` | String |
| `totalUsingFee` | long |
| `usingFee` | long |

### `SettlementItem` (7)

| field | type |
|---|---|
| `contractEndDate` | String |
| `contractId` | int |
| `contractStartDate` | String |
| `guestName` | String |
| `isRefund` | Boolean |
| `roomName` | String |
| `settlementAmount` | long |

### `SettlementItemData` (1)

| field | type |
|---|---|
| `content` | List SettlementItem |

### `SettlementReadySearchInfoResult` (2)

| field | type |
|---|---|
| `currentTime` | String |
| `settlementSummary` | SettlementSummary |

### `SettlementSummary` (2)

| field | type |
|---|---|
| `totalAmount` | long |
| `totalCount` | int |

## Review


### `HostReply` (3)

| field | type |
|---|---|
| `contents` | String |
| `createdDate` | String |
| `hostName` | String |

### `LandLordReviewDetail` (13)

| field | type |
|---|---|
| `contractId` | int |
| `endDate` | String |
| `guestName` | String |
| `guestProfileImage` | String |
| `picMain` | String |
| `reply` | Reply |
| `review` | String |
| `reviewDate` | String |
| `rid` | int |
| `roomName` | String |
| `score` | Integer |
| `simpleReviews` | List SimpleReview |
| `startDate` | String |

### `LandLordReviewManageItem` (11)

| field | type |
|---|---|
| `contractId` | int |
| `endDate` | String |
| `guestName` | String |
| `guestProfileImage` | String |
| `isReplied` | boolean |
| `review` | String |
| `reviewDate` | String |
| `rid` | int |
| `roomName` | String |
| `score` | Integer |
| `startDate` | String |

### `LandLordReviewManageResult` (4)

| field | type |
|---|---|
| `currentPage` | Integer |
| `lastPage` | Integer |
| `content` | List LandLordReviewManageItem |
| `totalElements` | Integer |

### `LandlordReviewContentsResult` (4)

| field | type |
|---|---|
| `currentPage` | Integer |
| `lastPage` | Integer |
| `content` | List LandlordProfileReviewData |
| `totalElements` | Integer |

### `LandlordReviewSummary` (5)

| field | type |
|---|---|
| `avgScore` | Double |
| `firstReviewDate` | String |
| `scoreDistribution` | List ScoreCount |
| `simpleReviewCounts` | List SimpleReviewCount |
| `totalCount` | long |

### `RecentReviewItem` (7)

| field | type |
|---|---|
| `contractId` | int |
| `picMain` | String |
| `review` | String |
| `rid` | int |
| `roomAddress` | String |
| `roomName` | String |
| `score` | int |

### `Reply` (5)

| field | type |
|---|---|
| `alterMessage` | String |
| `contents` | String |
| `createdDate` | String |
| `isDeleted` | boolean |
| `replyId` | long |

### `ScoreCount` (2)

| field | type |
|---|---|
| `count` | long |
| `score` | int |

### `SimpleReview` (3)

| field | type |
|---|---|
| `code` | String |
| `content` | String |
| `templateId` | int |

### `SimpleReviewCount` (4)

| field | type |
|---|---|
| `code` | String |
| `content` | String |
| `count` | long |
| `templateId` | int |

### `SimpleReviewData` (3)

| field | type |
|---|---|
| `content` | String |
| `count` | Integer |
| `isForHost` | boolean |

### `TenantReviewManageItem` (12)

| field | type |
|---|---|
| `endDate` | String |
| `hostReply` | HostReply |
| `initialContractId` | int |
| `isDepositReturned` | Boolean |
| `picMain` | String |
| `review` | String |
| `reviewDate` | String |
| `rid` | int |
| `roomName` | String |
| `score` | Integer |
| `simpleReviews` | List SimpleReview |
| `startDate` | String |

### `TenantReviewManageResult` (4)

| field | type |
|---|---|
| `currentPage` | Integer |
| `lastPage` | Integer |
| `content` | List TenantReviewManageItem |
| `totalElements` | Integer |

## Chat


### `ChatScheduledItem` (6)

| field | type |
|---|---|
| `connectedRoomCount` | int |
| `content` | String |
| `dayOffset` | int |
| `id` | int |
| `sendTime` | String |
| `sendTrigger` | e |

### `ChatScheduledItemDetail` (6)

| field | type |
|---|---|
| `connectedRooms` | List ConnectedRoom |
| `content` | String |
| `dayOffset` | int |
| `id` | int |
| `sendTime` | String |
| `sendTrigger` | e |

### `ChatScheduledListResult` (1)

| field | type |
|---|---|
| `content` | List ChatScheduledItem |

### `ChatSendResult` (1)

| field | type |
|---|---|
| `chatRoomId` | int |

### `ChattingExtendContractItem` (4)

| field | type |
|---|---|
| `endDate` | String |
| `initialContractId` | Integer |
| `roomId` | Integer |
| `startDate` | String |

### `ChattingExtendContractListResult` (1)

| field | type |
|---|---|
| `contractMasters` | List ChattingExtendContractItem |

### `ChattingFloatingAction` (12)

| field | type |
|---|---|
| `changedEndDate` | String |
| `changedStartDate` | String |
| `contractId` | Integer |
| `currentEndDate` | String |
| `currentStartDate` | String |
| `endDate` | String |
| `initialContractId` | Integer |
| `paymentAmount` | Long |
| `roomId` | Integer |
| `scheduleChangeRequestId` | Integer |
| `startDate` | String |
| `type` | h |

### `ChattingHeaderAction` (2)

| field | type |
|---|---|
| `initialContractId` | Integer |
| `type` | i |

### `ChattingRoomActions` (2)

| field | type |
|---|---|
| `floatingAction` | ChattingFloatingAction |
| `headerActions` | List ChattingHeaderAction |

### `ChattingRoomInfo` (2)

| field | type |
|---|---|
| `picMain` | String |
| `roomName` | String |

### `ChattingSearchHintResult` (2)

| field | type |
|---|---|
| `earliestIdx` | Long |
| `matched` | boolean |

### `ChattingTranslationResult` (3)

| field | type |
|---|---|
| `sourceLanguage` | String |
| `targetLanguage` | String |
| `translatedText` | String |

### `ConnectedRoom` (8)

| field | type |
|---|---|
| `addrDetail` | String |
| `addrFloor` | String |
| `addrLot` | String |
| `isConnected` | Boolean |
| `isPublic` | boolean |
| `picMain` | String |
| `rid` | int |
| `roomName` | String |

## Payment/Account


### `BankInfoCheckResult` (2)

| field | type |
|---|---|
| `accountHolderName` | String |
| `verified` | boolean |

### `BankItem` (2)

| field | type |
|---|---|
| `code` | String |
| `name` | String |

### `DepositReturnAccount` (6)

| field | type |
|---|---|
| `depositReturnBankAccount` | String |
| `depositReturnBankHolder` | String |
| `depositReturnBankName` | String |
| `depositReturnedAt` | String |
| `isDepositReturned` | boolean |
| `isEditAvailable` | boolean |

### `DepositReturnCard` (5)

| field | type |
|---|---|
| `cardName` | String |
| `cardNo` | String |
| `cardReceiptUrl` | String |
| `depositReturnedAt` | String |
| `isDepositReturned` | boolean |

### `ReceiptInfo` (11)

| field | type |
|---|---|
| `billUrl` | String |
| `corpCeo` | String |
| `corpId` | String |
| `corpName` | String |
| `failedReason` | String |
| `invoiceeEmail` | String |
| `isEditAvailable` | boolean |
| `issuanceNumber` | String |
| `receiptRequested` | Boolean |
| `status` | String |
| `taxReceiptType` | String |

### `RefundAccountInfo` (5)

| field | type |
|---|---|
| `isRefunded` | boolean |
| `refundBankAccount` | String |
| `refundBankHolder` | String |
| `refundBankName` | String |
| `refundedAt` | String |

### `RefundCardInfo` (5)

| field | type |
|---|---|
| `cardName` | String |
| `cardNo` | String |
| `cardReceiptUrl` | String |
| `isRefunded` | boolean |
| `refundedAt` | String |

## Notification/Support


### `AlarmCategories` (3)

| field | type |
|---|---|
| `categoryCode` | String |
| `iconUrl` | String |
| `name` | String |

### `AlarmCategoriesResult` (1)

| field | type |
|---|---|
| `categories` | List AlarmCategories |

### `AlarmItem` (7)

| field | type |
|---|---|
| `categoryCode` | String |
| `content` | String |
| `createdAt` | String |
| `iconUrl` | String |
| `id` | String |
| `link` | AlarmLink |
| `read` | boolean |

### `AlarmItemListResult` (2)

| field | type |
|---|---|
| `currentPage` | int |
| `lastPage` | int |

### `AlarmLink` (1)

| field | type |
|---|---|
| `deepLink` | String |

### `Banner` (1)

| field | type |
|---|---|
| `link` | String |

### `DoNotDisturbSetting` (3)

| field | type |
|---|---|
| `enabled` | boolean |
| `endHour` | int |
| `startHour` | int |

### `FaqCategories` (1)

| field | type |
|---|---|
| `categoryCode` | String |

### `FaqCategoriesResult` (1)

| field | type |
|---|---|
| `categories` | List FaqCategories |

### `FaqItem` (3)

| field | type |
|---|---|
| `answer` | String |
| `id` | int |
| `question` | String |

### `FaqItemListResult` (1)

| field | type |
|---|---|
| `totalElements` | int |

### `GuestContractNotificationItem` (7)

| field | type |
|---|---|
| `actionDescription` | String |
| `actionType` | String |
| `content` | String |
| `contractId` | int |
| `deadlineDescription` | String |
| `deadlineTime` | String |
| `nowTime` | String |

### `InquiryContractInfo` (5)

| field | type |
|---|---|
| `contractId` | int |
| `endDate` | String |
| `picMain` | String |
| `roomName` | String |
| `startDate` | String |

### `MyInquiriesData` (1)

| field | type |
|---|---|
| `content` | List MyInquiriesItem |

### `MyInquiriesItem` (7)

| field | type |
|---|---|
| `answer` | String |
| `answeredAt` | String |
| `content` | String |
| `contract` | InquiryContractInfo |
| `createdAt` | String |
| `id` | int |
| `status` | String |

### `NoticeDetailItem` (5)

| field | type |
|---|---|
| `contents` | String |
| `id` | int |
| `next` | NoticeItem |
| `previous` | NoticeItem |
| `writeDate` | String |

### `NoticeItem` (2)

| field | type |
|---|---|
| `id` | int |
| `writeDate` | String |

### `NoticeListResult` (1)

| field | type |
|---|---|
| `content` | List NoticeItem |

### `NotificationCategoryItem` (1)

| field | type |
|---|---|
| `category` | String |

### `NotificationChannelItem` (2)

| field | type |
|---|---|
| `channel` | String |
| `enabled` | boolean |

### `NotificationSettingResult` (5)

| field | type |
|---|---|
| `chat` | NotificationCategoryItem |
| `doNotDisturb` | DoNotDisturbSetting |
| `marketing` | NotificationCategoryItem |
| `roomManagement` | NotificationCategoryItem |
| `settlement` | NotificationCategoryItem |

### `SurveyListData` (2)

| field | type |
|---|---|
| `questions` | List SurveyQuestion |
| `surveyType` | String |

### `SurveyOption` (2)

| field | type |
|---|---|
| `type` | SurveyOptionType |
| `value` | String |

### `SurveyQuestion` (6)

| field | type |
|---|---|
| `options` | List SurveyOption |
| `order` | int |
| `placeholder` | String |
| `question` | String |
| `required` | boolean |
| `type` | SurveyQuestionType |

## Campaign


### `ArticleCategory` (2)

| field | type |
|---|---|
| `id` | Integer |
| `name` | String |

### `ArticleContentItem` (3)

| field | type |
|---|---|
| `categoryId` | int |
| `id` | int |
| `link` | String |

### `ArticleData` (1)

| field | type |
|---|---|
| `content` | List ArticleContentItem |

### `ArticleResult` (2)

| field | type |
|---|---|
| `articleCategories` | List ArticleCategory |
| `articles` | ArticleData |

### `CampaignDetail` (4)

| field | type |
|---|---|
| `categoryId` | Integer |
| `id` | int |
| `link` | String |
| `type` | String |

### `EditorPick` (2)

| field | type |
|---|---|
| `id` | int |
| `link` | String |

### `EventItem` (4)

| field | type |
|---|---|
| `endAt` | String |
| `id` | int |
| `link` | String |
| `startAt` | String |

### `EventListResult` (2)

| field | type |
|---|---|
| `closedEvents` | List EventItem |
| `inProgressEvents` | List EventItem |

### `GoogleAnalyticsEventData` (2)

| field | type |
|---|---|
| `age` | Integer |
| `gender` | String |

### `NewAirBridgeEventData` (9)

| field | type |
|---|---|
| `label` | String |
| `level` | int |
| `price` | int |
| `productId` | int |
| `productName` | String |
| `quantity` | int |
| `score` | Integer |
| `transactionId` | int |
| `value` | int |

### `NewAirBridgeEventDataResult` (1)

| field | type |
|---|---|
| `airbridgeEvent` | NewAirBridgeEventData |

### `PartnershipItem` (2)

| field | type |
|---|---|
| `id` | int |
| `link` | String |

## Address


### `AddressDetail` (4)

| field | type |
|---|---|
| `lat` | Double |
| `lng` | Double |
| `schools` | List String |
| `subwayStations` | List String |

### `AddressInfo` (6)

| field | type |
|---|---|
| `addrLot` | String |
| `addrStreet` | String |
| `addrStreetEn` | String |
| `province` | String |
| `town` | String |
| `zipCode` | String |

### `AddressSearchResult` (1)

| field | type |
|---|---|
| `addresses` | List AddressInfo |

## 기타


### `AirBridgeDataObject` (5)
| field | type |
|---|---|
| `category` | String |
| `customAttributes` | JsonObject |
| `label` | String |
| `semanticAttributes` | JsonObject |
| `value` | Integer |

### `BaseResponseData` (3)
| field | type |
|---|---|
| `airbridgeObject` | AirBridgeDataObject |
| `data` | T |
| `code` | String |

### `ConfigResult` (8)
| field | type |
|---|---|
| `s3_access_key` | String |
| `aws_bucket_name` | String |
| `aws_cloudfront_url` | String |
| `aws_region` | String |
| `s3_secret_key` | String |
| `cs_email` | String |
| `error_code` | int |
| `min_version_android` | String |

### `DisplayPeriodItem` (3)
| field | type |
|---|---|
| `endDate` | String |
| `startDate` | String |
| `type` | String |

### `DisplayStepItem` (4)
| field | type |
|---|---|
| `displayStatus` | String |
| `displayedAt` | String |
| `periods` | List DisplayPeriodItem |
| `step` | String |

### `GuestContractListResult` (1)
| field | type |
|---|---|
| `content` | List GuestContractItem |

### `GuestEnterConfirmNeedContractInfo` (2)
| field | type |
|---|---|
| `contractId` | Integer |
| `hasPendingScheduleChangeResult` | Boolean |

### `GuestHomeDataResult` (7)
| field | type |
|---|---|
| `articleComponentDescription` | String |
| `articleComponentTitle` | String |
| `guestEvents` | ArrayList Banner |
| `popularPropertyType` | String |
| `popupInfos` | ArrayList Banner |
| `recommendedArticles` | List ArticleContentItem |
| `searchPlaceholders` | List String |

### `GuestTooltipMessageData` (3)
| field | type |
|---|---|
| `checkinMessage` | String |
| `checkoutMessage` | String |
| `extendMessage` | String |

### `HostActionContractInfoResult` (3)
| field | type |
|---|---|
| `currentTime` | String |
| `waitingApprovalCount` | Integer |
| `waitingCheckFinishCount` | Integer |

### `HostContractActionCountResult` (4)
| field | type |
|---|---|
| `waitingApprovalCount` | int |
| `waitingCheckFinishCount` | int |
| `waitingCheckinCount` | int |
| `waitingCheckoutCount` | int |

### `HostContractListResult` (2)
| field | type |
|---|---|
| `content` | List HostContractItem |
| `totalElements` | Integer |

### `HostContractMasterStatusCount` (8)
| field | type |
|---|---|
| `activeCount` | int |
| `canceledCount` | int |
| `closedCount` | int |
| `currentTime` | String |
| `paymentCanceledCount` | int |
| `readyCount` | int |
| `reviewingCount` | int |
| `terminatingCount` | int |

### `HostHomeDataResult` (6)
| field | type |
|---|---|
| `articleComponentDescription` | String |
| `articleComponentTitle` | String |
| `faqs` | List FaqItem |
| `hostRoomSummary` | HostRoomSummary |
| `popupInfos` | List Banner |
| `recommendedArticles` | List ArticleContentItem |

### `HostRoomListResult` (4)
| field | type |
|---|---|
| `currentPage` | Integer |
| `lastPage` | Integer |
| `content` | List RoomListItem |
| `totalElements` | Integer |

### `HostTooltipMessageData` (2)
| field | type |
|---|---|
| `checkFinishMessage` | String |
| `depositDeferReleaseMessage` | String |

### `LandlordProfileReviewData` (5)
| field | type |
|---|---|
| `guestName` | String |
| `hostReply` | HostReply |
| `review` | String |
| `reviewDate` | String |
| `score` | Integer |

### `MyRoomResult` (1)
| field | type |
|---|---|
| `content` | ArrayList RoomListItem |

### `RecommendSearchKeywords` (1)
| field | type |
|---|---|
| `keywords` | List String |

### `ResponseMessage` (2)
| field | type |
|---|---|
| `content` | String |
| `type` | ResponseMessageType |

### `RoomContractMoreInfo` (1)
| field | type |
|---|---|
| `lastActiveContract` | LastActiveContract |

### `RoomScheduleRequestData` (2)
| field | type |
|---|---|
| `endDate` | String |
| `startDate` | String |

### `SearchKeywordResult` (3)
| field | type |
|---|---|
| `landmarks` | List LocationMakerItem |
| `regions` | List LocationMakerItem |
| `subways` | List LocationMakerItem |