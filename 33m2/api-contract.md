# 33m2 API 계약 — 완전판 (Retrofit 인터페이스 역추출) ★★

> 출처: 앱 APK의 **Retrofit 서비스 인터페이스**(`k7/f.java`) 디컴파일. 메서드·경로·파라미터·요청/응답 타입이 코드 그대로.
> **180 메서드 확정** (GET 103 · POST 56 · PUT 17 · DELETE 4). R8 축약 애노테이션 복원: `@ra.f`=GET `@ra.o`=POST `@ra.p`=PUT `@ra.b`=DELETE `@s`=@Path `@t`=@Query `@ra.a`=@Body.
> 요청/응답 DTO 필드는 `33m2/data-model.md`(응답) · 아래 부록(요청) 참조. 원본: `_shared/captures/33m2.api-full.json`, `33m2.req-dto.json`
> 이 문서가 **API 단일 진실**입니다. `api-endpoints.md`(경로만)·`api.md`(규약·의미)는 보조.
> **기계 판독용**: `33m2/openapi.yaml` (OpenAPI 3.1, 이 계약에서 자동생성 — 코드젠/목서버/검증에 사용). 재생성: `python3 _shared/captures/33m2.openapi.gen.py <out.yaml>`.

## 공통
- 성공 `{code:"SCSS_001", data:T}` · 에러 `{code, message:{type,content}, data?}` (HTTP 400)
- 응답은 항상 `BaseResponseData<T>` 로 래핑. 아래 표의 "응답"은 `T`.
- `v` = Unit/void (본문 없음). `{path}` = @Path, `?x` = @Query, `BODY` = @Body 요청 DTO.


## 1. 인증·계정·인증서 (33)

| M | path | query | body | → resp |
|---|---|---|---|---|
| GET | `/v1/accounts/bank-codes` | · | `·` | `List<BankItem>` |
| POST | `/v1/accounts/verification` | · | `BankInfoCheckRequest` | `BankInfoCheckResult` |
| POST | `/v1/cert/email/send` | · | `EmailVerifyCodeRequest` | `EmailVerifyCodeResult` |
| POST | `/v1/cert/email/verify` | · | `EmailVerifyRequest` | `EmailVerifyResult` |
| POST | `/v1/cert/mok/resend` | · | `MobileCertNumResendRequest` | `MobileCertNumResendResult` |
| POST | `/v1/cert/mok/send` | · | `MobileCertNumRequest` | `MobileCertNumResult` |
| GET | `/v1/cert/mok/terms` | · | `·` | `MobileCertTermsResult` |
| POST | `/v1/cert/mok/verify` | · | `MobileCertNumVerifyRequest` | `CertNumResult` |
| POST | `/v1/cert/passport/ocr` | · | `PassportOcrRequest` | `PassportOcrResult` |
| GET | `/v1/cert/phone-number` | certNum:String | `·` | `SimpleStringResult` |
| POST | `/v1/user/email/validation` | · | `CheckEmailValidationRequest` | `·` |
| POST | `/v1/user/find-id` | · | `FindUserIdRequest` | `FindMemberIdResult` |
| POST | `/v1/user/host-conversion` | · | `ChangeToHostRequest` | `RefreshTokenResult` |
| GET | `/v1/user/host-conversion/validation` | · | `·` | `·` |
| POST | `/v1/user/join/{joinType}` | · | `JoinRequest` | `JoinResult` |
| POST | `/v1/user/login` | · | `LoginRequest` | `LoginResult` |
| POST | `/v1/user/logout` | · | `·` | `·` |
| GET | `/v1/user/me` | · | `·` | `UserMe` |
| DELETE | `/v1/user/me` | · | `·` | `·` |
| PUT | `/v1/user/me/cert` | · | `CertNumUpdateRequest` | `·` |
| PUT | `/v1/user/me/cert/passport` | · | `PassPortUpdateRequest` | `·` |
| POST | `/v1/user/me/email/send` | · | `EmailVerifyCodeRequest` | `EmailVerifyCodeResult` |
| POST | `/v1/user/me/email/verify` | · | `EmailVerifyRequest` | `RefreshTokenResult` |
| POST | `/v1/user/me/firebase-token` | · | `·` | `SimpleStringResult` |
| PUT | `/v1/user/me/guest-profile` | · | `GuestProfileUpdateRequest` | `RefreshTokenResult` |
| PUT | `/v1/user/me/host-profile` | · | `HostProfileUpdateRequest` | `RefreshTokenResult` |
| POST | `/v1/user/password-reset` | · | `PasswordResetRequest` | `·` |
| POST | `/v1/user/password-reset/email` | · | `PasswordResetEmailRequest` | `·` |
| POST | `/v1/user/password-reset/email/send` | · | `EmailVerifyCodeRequest` | `EmailVerifyCodeResult` |
| POST | `/v1/user/password-reset/email/verify` | · | `EmailVerifyRequest` | `EmailVerifyResult` |
| POST | `/v1/user/password-reset/validation` | · | `PasswordResetValidationRequest` | `·` |
| POST | `/v1/user/phone-number/validation` | · | `ValidatePhoneNumberRequest` | `·` |
| POST | `/v1/user/refresh` | · | `RefreshTokenRequest` | `?` |

## 3. 매물조회·검색 (19)

| M | path | query | body | → resp |
|---|---|---|---|---|
| GET | `/v1/address/details` | address:String | `·` | `AddressDetail` |
| GET | `/v1/address/search` | keyword:String | `·` | `AddressSearchResult` |
| GET | `/v1/map/rooms` | swLat:Double, swLng:Double, neLat:Double, neLng:Double, roomMarkerLat:Double, roomMarkerLng:Double, zoomLevel:Integer, startDate:String, endDate:String, page:int | `·` | `MapRoomSearchResult` |
| GET | `/v1/map/search-keywords` | keyword:String, maxSize:int | `·` | `SearchKeywordResult` |
| GET | `/v1/rooms` | keyword:String, startDate:String, endDate:String, sortBy:String, page:int | `·` | `RoomSearchResult` |
| GET | `/v1/rooms/favorites` | page:int | `·` | `MyRoomResult` |
| GET | `/v1/rooms/hosts/{hostUid}` | page:int | `·` | `HostRoomListResult` |
| GET | `/v1/rooms/recent-views` | uuid:String, page:int | `·` | `MyRoomResult` |
| DELETE | `/v1/rooms/recent-views` | uuid:String, rid:int | `·` | `·` |
| GET | `/v1/rooms/recent/view` | uuid:String | `·` | `List<RoomListItem>` |
| GET | `/v1/rooms/recommend/search-keywords` | · | `·` | `RecommendSearchKeywords` |
| GET | `/v1/rooms/{rid}` | uuid:String | `·` | `RoomDetailInfoResult` |
| GET | `/v1/rooms/{rid}/available-weeks` | startDate:String, isExtend:boolean | `·` | `RoomContractAvailableWeeks` |
| GET | `/v1/rooms/{rid}/contract-availability` | startDate:String, endDate:String | `·` | `SimpleBooleanResult` |
| GET | `/v1/rooms/{rid}/contract/{contractId}` | · | `·` | `RoomDetailInfoResult` |
| DELETE | `/v1/rooms/{rid}/favorites` | · | `·` | `NewAirBridgeEventDataResult` |
| POST | `/v1/rooms/{rid}/favorites` | · | `·` | `NewAirBridgeEventDataResult` |
| GET | `/v1/rooms/{rid}/schedules` | year:int, month:int, currentInitialContractId:Integer | `·` | `RoomScheduleData` |
| GET | `/v1/settlements/rooms` | · | `·` | `List<RoomBasicInfo>` |

## 4. 매물관리(호스트) (24)

| M | path | query | body | → resp |
|---|---|---|---|---|
| GET | `/v1/host/rooms` | keyword:String, statusFilter:String, page:int | `·` | `HostRoomListData` |
| POST | `/v1/host/rooms` | · | `HouseSpaceInfo` | `NewRoomRegistResult` |
| GET | `/v1/host/rooms/address/validation` | addrStreet:String | `·` | `·` |
| GET | `/v1/host/rooms/survey-requirements` | · | `·` | `SimpleBooleanResult` |
| PUT | `/v1/host/rooms/{rid}` | · | `RoomInfoOverView` | `·` |
| GET | `/v1/host/rooms/{rid}` | · | `·` | `RoomInfoOverView` |
| GET | `/v1/host/rooms/{rid}/contract-policy` | · | `·` | `HouseContractPolicyInfo` |
| PUT | `/v1/host/rooms/{rid}/contract-policy` | · | `HouseContractPolicyInfo` | `·` |
| POST | `/v1/host/rooms/{rid}/deletion` | · | `ReasonRequest` | `·` |
| PUT | `/v1/host/rooms/{rid}/description` | · | `HouseDescriptionInfo` | `·` |
| GET | `/v1/host/rooms/{rid}/description` | · | `·` | `HouseDescriptionInfo` |
| PUT | `/v1/host/rooms/{rid}/fee-info` | · | `HousePriceInfo` | `·` |
| GET | `/v1/host/rooms/{rid}/fee-info` | · | `·` | `HousePriceInfo` |
| PUT | `/v1/host/rooms/{rid}/options` | · | `HouseOptionInfo` | `·` |
| GET | `/v1/host/rooms/{rid}/options` | · | `·` | `HouseOptionInfo` |
| GET | `/v1/host/rooms/{rid}/preview` | · | `·` | `RoomDetailInfoResult` |
| GET | `/v1/host/rooms/{rid}/progress` | · | `·` | `RoomInfoProgress` |
| POST | `/v1/host/rooms/{rid}/review-request` | · | `·` | `·` |
| GET | `/v1/host/rooms/{rid}/schedules` | · | `·` | `RoomScheduleData` |
| POST | `/v1/host/rooms/{rid}/schedules/unavailable` | · | `RoomScheduleRequestData` | `·` |
| GET | `/v1/host/rooms/{rid}/space-info` | · | `·` | `HouseSpaceInfo` |
| PUT | `/v1/host/rooms/{rid}/space-info` | · | `HouseSpaceInfo` | `·` |
| PUT | `/v1/host/rooms/{rid}/visibility` | · | `ChangeRoomPublishRequest` | `·` |
| POST | `/v1/host/rooms/{sourceRid}/clone` | · | `·` | `RoomCopyResult` |

## 5. 계약(게스트) (54)

| M | path | query | body | → resp |
|---|---|---|---|---|
| GET | `/v1/contracts/recent-reviews` | · | `·` | `List<RecentReviewItem>` |
| GET | `/v1/contracts/simple-review-templates` | · | `·` | `List<SimpleReviewData>` |
| GET | `/v1/guest/contracts/estimate` | rid:int, isExtend:boolean, startDate:String, endDate:String, initialContractId:Integer | `·` | `GuestContractEstimateResult` |
| GET | `/v1/guest/contracts/last-active` | rid:int | `·` | `RoomContractMoreInfo` |
| GET | `/v1/guest/contracts/masters` | contractMasterStatus:String, sortBy:String, roomNameOrAddress:String, page:int | `·` | `GuestContractListResult` |
| GET | `/v1/guest/contracts/masters/{initialContractId}` | · | `·` | `GuestContractItem` |
| POST | `/v1/guest/contracts/masters/{initialContractId}/schedule-changes` | · | `ChangeScheduleRequest` | `ChangeScheduleRequestResult` |
| GET | `/v1/guest/contracts/masters/{initialContractId}/schedule-changes/availability` | requestedStartDate:String | `·` | `ChangeScheduleAvailableResult` |
| GET | `/v1/guest/contracts/need-checkin` | · | `·` | `GuestEnterConfirmNeedContractInfo` |
| GET | `/v1/guest/contracts/need-review` | · | `·` | `TenantReviewManageItem` |
| GET | `/v1/guest/contracts/notifications` | · | `·` | `ArrayList<GuestContractNotificationItem>` |
| POST | `/v1/guest/contracts/request` | · | `GuestContractRequest` | `GuestContractRequestResult` |
| GET | `/v1/guest/contracts/reviews` | filter:String, page:int | `·` | `TenantReviewManageResult` |
| POST | `/v1/guest/contracts/reviews/{contractId}/popup/read` | · | `·` | `·` |
| POST | `/v1/guest/contracts/reviews/{initialContractId}` | · | `ScoreReviewUpdateRequest` | `·` |
| GET | `/v1/guest/contracts/reviews/{initialContractId}` | · | `·` | `TenantReviewManageItem` |
| GET | `/v1/guest/contracts/schedule-changes/result` | · | `·` | `ScheduleChangeResult` |
| POST | `/v1/guest/contracts/schedule-changes/{scheduleId}/cancel` | · | `·` | `·` |
| POST | `/v1/guest/contracts/schedule-changes/{scheduleId}/result/read` | · | `·` | `·` |
| GET | `/v1/guest/contracts/{contractId}` | · | `·` | `GuestContractDetailResult` |
| POST | `/v1/guest/contracts/{contractId}/cancel` | · | `·` | `·` |
| GET | `/v1/guest/contracts/{contractId}/check-in/checklist` | · | `·` | `GuestCheckInInfo` |
| PUT | `/v1/guest/contracts/{contractId}/deposit-return-account` | · | `DepositReturnAccountRequest` | `·` |
| GET | `/v1/guest/contracts/{contractId}/deposit-return-account` | · | `·` | `DepositReturnAccount` |
| GET | `/v1/guest/contracts/{contractId}/deposit-return-card` | · | `·` | `DepositReturnCard` |
| PUT | `/v1/guest/contracts/{contractId}/receipt-info` | · | `ReceiptInfoRequest` | `·` |
| GET | `/v1/guest/contracts/{contractId}/receipt-info` | · | `·` | `ReceiptInfo` |
| GET | `/v1/guest/contracts/{contractId}/receipt-info/bill-url` | · | `·` | `SimpleStringResult` |
| POST | `/v1/guest/contracts/{contractId}/refund` | · | `ContractRefundRequest` | `·` |
| GET | `/v1/guest/contracts/{contractId}/refund-account` | · | `·` | `RefundAccountInfo` |
| GET | `/v1/guest/contracts/{contractId}/refund-card` | · | `·` | `RefundCardInfo` |
| GET | `/v1/guest/contracts/{contractId}/refund-reasons` | · | `·` | `List<CancelReason>` |
| GET | `/v1/guest/contracts/{contractId}/refund/checklist` | · | `·` | `RefundCheckListResult` |
| POST | `/v1/guest/contracts/{initialContractId}/check-in` | · | `GuestCheckInRequest` | `GuestContractItem` |
| POST | `/v1/guest/contracts/{initialContractId}/check-out` | · | `GuestCheckOutRequest` | `GuestContractItem` |
| GET | `/v1/guest/contracts/{initialContractId}/check-out/checklist` | · | `·` | `GuestCheckOutCheckListResult` |
| POST | `/v1/guest/contracts/{initialContractId}/simple-review` | · | `SimpleReviewAddRequest` | `·` |
| GET | `/v1/host/contracts/masters/actions/count` | · | `·` | `HostContractActionCountResult` |
| GET | `/v1/host/contracts/masters/actions/count` | · | `·` | `HostActionContractInfoResult` |
| GET | `/v1/host/contracts/masters/status/count` | · | `·` | `HostContractMasterStatusCount` |
| GET | `/v1/host/contracts/masters/{initialContractId}` | · | `·` | `HostContractItem` |
| GET | `/v1/host/contracts/masters/{initialContractId}/care-link` | · | `·` | `SimpleStringResult` |
| GET | `/v1/host/contracts/schedule-changes/{scheduleId}` | · | `·` | `ChangeScheduleRequestData` |
| POST | `/v1/host/contracts/schedule-changes/{scheduleId}/approval` | · | `·` | `·` |
| POST | `/v1/host/contracts/schedule-changes/{scheduleId}/rejection` | · | `RejectionScheduleChangeRequest` | `·` |
| GET | `/v1/host/contracts/{contractId}` | · | `·` | `HostContractDetailResult` |
| POST | `/v1/host/contracts/{contractId}/approval` | · | `·` | `NewAirBridgeEventDataResult` |
| GET | `/v1/host/contracts/{contractId}/calculated-refund-info` | · | `·` | `HostContractCancelRefundInfo` |
| POST | `/v1/host/contracts/{contractId}/rejection` | · | `ReasonRequest` | `NewAirBridgeEventDataResult` |
| POST | `/v1/host/contracts/{initialContractId}/confirm-checkout` | · | `·` | `HostContractItem` |
| POST | `/v1/host/contracts/{initialContractId}/hold-checkout` | · | `ArrayReasonRequest` | `HostContractItem` |
| GET | `/v1/{mode}/contracts/masters/{initialContractId}/schedule-change` | · | `·` | `ContractScheduleResult` |
| GET | `/v1/{mode}/contracts/masters/{initialContractId}/schedule-change/history` | · | `·` | `ScheduleChangeHistoryResult` |
| GET | `/v2/host/contracts/masters` | contractMasterStatus:String, fromStartDate:String, toStartDate:String, fromEndDate:String, toEndDate:String, roomNameOrAddress:String, hostContractActionType:String, sortBy:String, page:int | `·` | `HostContractListResult` |

## 6. 계약(호스트) (4)

| M | path | query | body | → resp |
|---|---|---|---|---|
| GET | `/v1/host/contract/reviews` | rid:Integer, replyStatus:String, fromDate:String, toDate:String, sortBy:String, page:int | `·` | `LandLordReviewManageResult` |
| GET | `/v1/host/contract/reviews/summary` | rid:Integer | `·` | `LandlordReviewSummary` |
| GET | `/v1/host/contract/reviews/{contractId}` | · | `·` | `LandLordReviewDetail` |
| POST | `/v1/host/contract/reviews/{contractId}/replies` | · | `SimpleStringRequest` | `·` |

## 7. 정산 (4)

| M | path | query | body | → resp |
|---|---|---|---|---|
| GET | `/v1/settlements/complete` | onlySummary:boolean, rid:Integer, fromSettlementDate:String, toSettlementDate:String, page:int | `·` | `SettlementReadySearchInfoResult` |
| GET | `/v1/settlements/ready` | onlySummary:boolean | `·` | `SettlementReadySearchInfoResult` |
| GET | `/v1/settlements/ready` | onlySummary:boolean, rid:Integer, page:int | `·` | `SettlementReadySearchInfoResult` |
| GET | `/v1/settlements/{contractId}` | · | `·` | `PayoutDetail` |

## 8. 채팅 (14)

| M | path | query | body | → resp |
|---|---|---|---|---|
| POST | `/v1/chat/messages` | · | `ChatMessageSendRequest` | `ChatSendResult` |
| POST | `/v1/chat/scheduled` | · | `SetScheduledChatMessageRequest` | `·` |
| GET | `/v1/chat/scheduled` | page:int | `·` | `ChatScheduledListResult` |
| GET | `/v1/chat/scheduled/connectable-rooms` | keyword:String, id:Integer | `·` | `List<ConnectedRoom>` |
| DELETE | `/v1/chat/scheduled/{id}` | · | `·` | `·` |
| PUT | `/v1/chat/scheduled/{id}` | · | `SetScheduledChatMessageRequest` | `·` |
| GET | `/v1/chat/scheduled/{id}` | · | `·` | `ChatScheduledItemDetail` |
| GET | `/v1/chat/{cid}` | · | `·` | `ChattingRoomInfo` |
| GET | `/v1/chat/{cid}/actions` | · | `·` | `ChattingRoomActions` |
| GET | `/v1/chat/{cid}/contract-masters` | · | `·` | `ChattingExtendContractListResult` |
| PUT | `/v1/chat/{cid}/contract-period` | · | `StartEndDateRequest` | `·` |
| GET | `/v1/chat/{cid}/messages/search/hint` | keyword:String | `·` | `ChattingSearchHintResult` |
| POST | `/v1/chat/{cid}/messages/{msg_idx}/translation` | · | `ChatTranslateRequest` | `ChattingTranslationResult` |
| POST | `/v1/chat/{cid}/read` | · | `·` | `·` |

## 9. 공통·지원·콘텐츠 (28)

| M | path | query | body | → resp |
|---|---|---|---|---|
| GET | `/v1/campaigns/articles` | categoryId:Integer, onlyGuestArticle:boolean, onlyHostArticle:boolean, page:int | `·` | `ArticleResult` |
| GET | `/v1/campaigns/articles/editor-pick/{loginType}` | · | `·` | `List<EditorPick>` |
| GET | `/v1/campaigns/events` | onlyGuestEvent:boolean, onlyHostEvent:boolean | `·` | `EventListResult` |
| GET | `/v1/campaigns/partnerships` | · | `·` | `ArrayList<PartnershipItem>` |
| GET | `/v1/campaigns/{id}` | · | `·` | `CampaignDetail` |
| GET | `/v1/contents/guest/home` | · | `·` | `GuestHomeDataResult` |
| GET | `/v1/contents/host/home` | · | `·` | `HostHomeDataResult` |
| POST | `/v1/devices/app-installations` | · | `·` | `·` |
| GET | `/v1/hosts/{hostUid}/profile` | · | `·` | `RoomHostInfo` |
| GET | `/v1/hosts/{hostUid}/reviews` | page:int | `·` | `LandlordReviewContentsResult` |
| GET | `/v1/support/inquiries` | page:int | `·` | `MyInquiriesData` |
| POST | `/v1/support/inquiries` | · | `InquiriesRequest` | `·` |
| GET | `/v1/support/{loginType}/top-faqs` | · | `·` | `FaqItemListResult` |
| GET | `/v1/support/{type}/faq-categories` | · | `·` | `FaqCategoriesResult` |
| GET | `/v1/support/{type}/faqs` | category:String, keyword:String, page:int | `·` | `FaqItemListResult` |
| GET | `/v1/support/{type}/notices` | page:int | `·` | `NoticeListResult` |
| GET | `/v1/support/{type}/notices/{id}` | · | `·` | `NoticeDetailItem` |
| GET | `/v1/surveys/{type}` | · | `·` | `SurveyListData` |
| POST | `/v1/surveys/{type}/submit` | · | `SurveyRequest` | `·` |
| GET | `/v1/{type}/inbox` | categoryCode:String, unreadOnly:boolean, page:int | `·` | `AlarmItemListResult` |
| GET | `/v1/{type}/inbox/categories` | · | `·` | `AlarmCategoriesResult` |
| POST | `/v1/{type}/inbox/{id}/read` | · | `·` | `·` |
| GET | `/v1/{type}/notification-settings` | · | `·` | `NotificationSettingResult` |
| PUT | `/v1/{type}/notification-settings/channels` | · | `NotificationUpdateRequest` | `·` |
| PUT | `/v1/{type}/notification-settings/do-not-disturb` | · | `DoNotDisturbUpdateRequest` | `·` |
| GET | `app/config` | · | `·` | `?` |
| POST | `test/auth` | · | `·` | `·` |
| GET | `test/token/expire` | · | `·` | `String` |

---

## 부록: 요청 DTO (49)


### `AccountChangeRequest`
| field | type |
|---|---|
| `accountHolder` | String |
| `bankAccount` | String |
| `bankName` | String |

### `AccountData`
| field | type |
|---|---|
| `bankAccount` | String |
| `bankHolder` | String |
| `bankName` | String |

### `ArrayReasonRequest`
| field | type |
|---|---|
| `reasons` | List<String> |

### `BankInfoCheckRequest`
| field | type |
|---|---|
| `accountNumber` | String |
| `bankName` | String |

### `CertNumUpdateRequest`
| field | type |
|---|---|
| `certNum` | String |

### `ChangeRoomPublishRequest`
| field | type |
|---|---|
| `detailReason` | String |
| `isPublic` | boolean |
| `reason` | String |

### `ChangeScheduleRequest`
| field | type |
|---|---|
| `guestMessage` | String |
| `requestedStartDate` | String |

### `ChangeToHostRequest`
| field | type |
|---|---|
| `bankAccount` | String |
| `bankHolder` | String |
| `bankName` | String |
| `corpCeo` | String |
| `corpId` | String |
| `corpName` | String |
| `hostIntro` | String |
| `invoiceeEmail` | String |
| `issuanceNumber` | String |
| `receiptRequested` | boolean |
| `recommenderPhoneNumber` | String |
| `taxReceiptType` | String |

### `ChatMessageSendRequest`
| field | type |
|---|---|
| `cid` | Integer |
| `contractEndDate` | String |
| `contractStartDate` | String |
| `imageUrl` | String |
| `picidx` | Integer |
| `rid` | Integer |
| `type` | String |

### `ChatTranslateRequest`
| field | type |
|---|---|
| `sourceLanguage` | String |
| `targetLanguage` | String |

### `ContractRefundRequest`
| field | type |
|---|---|
| `receiptInfo` | ReceiptInfoChangeRequest |
| `refundBankInfo` | AccountChangeRequest |
| `refundReasonCode` | String |

### `DepositReturnAccountChangeRequest`
| field | type |
|---|---|
| `depositReturnBankAccount` | String |
| `depositReturnBankHolder` | String |
| `depositReturnBankName` | String |

### `DepositReturnAccountRequest`
| field | type |
|---|---|
| `depositReturnAccount` | DepositReturnAccountChangeRequest |

### `DoNotDisturbUpdateRequest`
| field | type |
|---|---|
| `enabled` | boolean |
| `endHour` | int |
| `startHour` | int |

### `EmailVerifyRequest`
| field | type |
|---|---|
| `certCode` | String |

### `FindUserIdRequest`
| field | type |
|---|---|
| `name` | String |
| `phoneNumber` | String |

### `GuestCheckInRequest`
| field | type |
|---|---|
| `depositReturnAccount` | DepositReturnAccountChangeRequest |
| `receiptInfo` | ReceiptInfoChangeRequest |

### `GuestCheckOutRequest`
| field | type |
|---|---|
| `depositReturnAccount` | DepositReturnAccountChangeRequest |
| `review` | String |
| `score` | Integer |

### `GuestContractRequest`
| field | type |
|---|---|
| `endDate` | String |
| `isExtend` | boolean |
| `initialContractId` | Integer |
| `rid` | int |
| `startDate` | String |
| `toHost` | String |

### `HostProfileUpdateRequest`
| field | type |
|---|---|
| `account` | AccountData |
| `hostIntro` | String |
| `receiptInfo` | ReceiptInfoChangeRequest |

### `InquiriesRequest`
| field | type |
|---|---|
| `content` | String |
| `contractId` | Integer |

### `JoinRequest`
| field | type |
|---|---|
| `bankAccount` | String |
| `bankHolder` | String |
| `bankName` | String |
| `certNum` | String |
| `corpCeo` | String |
| `corpId` | String |
| `corpName` | String |
| `emailCertToken` | String |
| `hostIntro` | String |
| `invoiceeEmail` | String |
| `issuanceNumber` | String |
| `marketingAgree` | boolean |
| `name` | String |
| `ocrToken` | String |
| `passportImageUrl` | String |
| `password` | String |
| `phoneNumber` | String |
| `profileImageUrl` | String |
| `receiptRequested` | boolean |
| `recommenderPhoneNumber` | String |
| `taxReceiptType` | String |

### `LoginRequest`
| field | type |
|---|---|
| `password` | String |
| `username` | String |

### `MobileCertNumRequest`
| field | type |
|---|---|
| `birthday` | String |
| `genderDigit` | String |
| `provider` | String |
| `usageCode` | String |
| `userName` | String |
| `userPhone` | String |

### `MobileCertNumResendRequest`
| field | type |
|---|---|
| `txKey` | String |

### `MobileCertNumVerifyRequest`
| field | type |
|---|---|
| `authNumber` | String |
| `txKey` | String |

### `NotificationUpdateRequest`
| field | type |
|---|---|
| `category` | String |
| `channel` | String |
| `enabled` | boolean |

### `PassPortUpdateRequest`
| field | type |
|---|---|
| `ocrToken` | String |
| `passportImageUrl` | String |
| `phoneNumber` | String |

### `PassportOcrRequest`
| field | type |
|---|---|
| `passportImageUrl` | String |

### `PasswordResetEmailRequest`
| field | type |
|---|---|
| `newPassword` | String |
| `passwordResetToken` | String |

### `PasswordResetRequest`
| field | type |
|---|---|
| `certNum` | String |
| `newPassword` | String |

### `PasswordResetValidationRequest`
| field | type |
|---|---|
| `certNum` | String |

### `ProfileData`
| field | type |
|---|---|
| `name` | String |
| `password` | String |
| `profileImageUrl` | String |

### `ReasonRequest`
| field | type |
|---|---|
| `detailReason` | String |
| `reason` | String |

### `ReceiptInfoChangeRequest`
| field | type |
|---|---|
| `corpCeo` | String |
| `corpId` | String |
| `corpName` | String |
| `invoiceeEmail` | String |
| `issuanceNumber` | String |
| `receiptRequested` | boolean |
| `taxReceiptType` | String |

### `ReceiptInfoRequest`
| field | type |
|---|---|
| `receiptInfo` | ReceiptInfoChangeRequest |

### `RefreshTokenRequest`
| field | type |
|---|---|
| `refreshToken` | String |

### `RejectionScheduleChangeRequest`
| field | type |
|---|---|
| `hostMessage` | String |

### `ScoreReviewUpdateRequest`
| field | type |
|---|---|
| `review` | String |
| `score` | int |

### `SetScheduledChatMessageRequest`
| field | type |
|---|---|
| `connectedRoomIds` | ArrayList<String> |
| `content` | String |
| `dayOffset` | Integer |
| `sendTime` | String |
| `sendTrigger` | String |

### `SimpleReviewAddRequest`
| field | type |
|---|---|
| `reviewStage` | String |
| `templateIds` | List<Integer> |

### `SimpleStringRequest`
| field | type |
|---|---|
| `contents` | String |

### `StartEndDateRequest`
| field | type |
|---|---|
| `endDate` | String |
| `startDate` | String |

### `SurveyAnswer`
| field | type |
|---|---|
| `answer` | String |
| `order` | int |

### `SurveyRequest`
| field | type |
|---|---|
| `answers` | List<SurveyAnswer> |

### `ValidatePhoneNumberRequest`
| field | type |
|---|---|
| `phoneNumber` | String |