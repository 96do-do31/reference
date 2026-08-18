# 상태 머신 다이어그램 (Mermaid) — 33m2 · Airbnb

> 텍스트 상태도(`33m2/DOMAIN.md` §3, `airbnb/flows-and-screens.md` FLOW-A02)를 렌더 가능한 mermaid로 정규화.
> **신뢰도**: 전이 트리거·라벨은 실측(i18n 키·DOMAIN). 개별 `contractStatus` 코드값 일부는 ❓추정(§표기).
> GitHub·mermaid.live에서 렌더됨.

---

## 1. 33m2 계약 진행 축 (contract progress) ★

계약의 **생애 축**. 결제 축(§2)과 분리해서 봐야 함(DOMAIN §2.4 "상태 2축").

```mermaid
stateDiagram-v2
    [*] --> 승인대기: 임차인 계약 요청 (인사 메시지 동반)
    승인대기 --> 취소: 임대인 거절 / 24h 미승인
    승인대기 --> 결제대기: 임대인 승인
    결제대기 --> 취소_미결제: 결제 마감시한 초과
    결제대기 --> 취소_선점: 다른 임차인 선결제
    결제대기 --> 입주대기: 결제 완료
    입주대기 --> 거주중: 입주일 도래 + [입주 확인하기]
    거주중 --> 거주중: [계약 연장하기] (같은 마스터에 계약 추가)
    거주중 --> 퇴실중: [퇴실하기]
    퇴실중 --> 임대인확인: 임대인 [퇴실 점검 완료]
    임대인확인 --> 보증금반환: 차감 정산
    보증금반환 --> 계약종료
    계약종료 --> [*]
    취소 --> [*]
    취소_미결제 --> [*]
    취소_선점 --> [*]

    note right of 결제대기
      ★ 결제마감 타이머 존재
      선결제자 확정(경쟁) = 관찰된 결함
      새 서비스는 홀드/선점 방지 권장
    end note
```

UI 라벨(`guest_lease_list.status.*`): `lease_pending`계약대기 · `movein_waiting`입주대기 · `staying`거주중 · `moving_out`퇴실중 · `lease_ended`계약종료 · `cancelled`취소 · `payment_cancelled`결제취소.

---

## 2. 33m2 결제 축 (payment) — 진행 축과 병행

```mermaid
stateDiagram-v2
    [*] --> 승인대기: approval_pending
    승인대기 --> 결제대기: 임대인 승인 → payment_pending
    승인대기 --> 취소: canceled
    결제대기 --> 결제완료: payment_completed
    결제대기 --> 결제취소: payment_canceled (미결제/선점)
    결제완료 --> [*]
    취소 --> [*]
    결제취소 --> [*]
```

---

## 3. 33m2 일정 변경 서브플로우 (schedule change) 🆕

`contract.tenant.schedule_change` / `landlord.respond_reschedule`. **총 계약기간 유지**(입주·퇴실일만 이동).

```mermaid
stateDiagram-v2
    [*] --> 변경요청: 임차인 일정 변경 요청
    변경요청 --> 변경확정: 임대인 승인
    변경요청 --> 변경취소: 임대인 거절 / 임차인 취소 / 자동 취소
    변경확정 --> [*]
    변경취소 --> [*]

    note right of 변경요청
      ⛔ 입주 확인 완료 후 불가
      ⛔ 해당 일정에 확정 계약 존재 시 승인 불가
      🔒 기간 자체 증감 불가 (연장은 별도 플로우)
    end note
```

---

## 4. 33m2 계약 취소 결정 흐름 (cancel) — 위약금 유도 분기

```mermaid
flowchart TD
    A[임차인 취소 시도] --> B{입주 전인가?}
    B -->|일정만 바꾸고 싶다| C[일정 변경 요청으로 유도<br/>5.3]
    B -->|임대인 사정| D[임대인에게 채팅 유도<br/>임대인이 직접 취소 → 위약금 회피]
    B -->|진행| E[환불 금액 확인]
    E --> F{환불 프리셋<br/>WEAK/MIDDLE/STRONG}
    F --> G[환불 실행 → payment_canceled]
    D -.->|연장 계약 존재| H[⛔ 취소 불가<br/>마지막 계약 먼저 취소]
```

> 환불률(✅검증): 15일전 무료/10%/20% · 8일전 20%/30%/50% · 1일전 40%/50%/70% · 당일이후 취소불가.

---

## 5. 입주·퇴실 타임라인 (movein_moveout 6단계)

```mermaid
stateDiagram-v2
    [*] --> 계약확정
    계약확정 --> 입주대기
    입주대기 --> 거주중: 입주 확인
    거주중 --> 퇴실: 퇴실 신청
    퇴실 --> 임대인확인: 퇴실 점검
    임대인확인 --> 보증금반환
    보증금반환 --> [*]
```

정산 시점(✅검증): 입주일 **D+0 ~ D+2**. 보증금 330,000원 고정.

---

## 6. Airbnb 예약 라이프사이클 (ReservationStatus) ★

enum 실측(`airbnb/data-model.md` §7) + FLOW-A02. 33m2보다 상태가 세분됨(INQUIRY·PREAPPROVED·AT_CHECKPOINT).

```mermaid
stateDiagram-v2
    [*] --> INQUIRY: 게스트 문의
    [*] --> NEW: 신규 요청
    INQUIRY --> PREAPPROVED: 호스트 사전승인
    NEW --> PENDING: 예약요청(REQUEST_TO_BOOK)
    PREAPPROVED --> PENDING: 게스트 요청 전환
    PENDING --> ACCEPTED: 호스트 수락 (AcceptRtbMutation)
    PENDING --> DECLINED: 호스트 거절
    PENDING --> TIMEDOUT: 24h 무응답
    NEW --> CONFIRMED: 즉시예약(INSTANT_BOOK)
    ACCEPTED --> CONFIRMED: 결제 확정
    CONFIRMED --> AT_CHECKPOINT: 에어락 검문 (이상거래)
    AT_CHECKPOINT --> CONFIRMED: 통과
    AT_CHECKPOINT --> CANCELLED: 실패
    CONFIRMED --> CANCELLED: 게스트/호스트 취소
    CONFIRMED --> COMPLETED: 체크아웃 완료
    COMPLETED --> [*]
    DECLINED --> [*]
    CANCELLED --> [*]
    TIMEDOUT --> [*]
    COMPLETED --> 상호리뷰: 양측 제출 or 14일 후 공개
```

> 33m2엔 없는 **이원 예약(즉시/요청)**과 **AT_CHECKPOINT(에어락)**이 근간. 일정변경은 `AcceptReservationAlterationMutation`으로 정식 지원.

---

## 7. Airbnb 상호 리뷰 공개 규칙 (FLOW-A03)

```mermaid
flowchart LR
    A[COMPLETED] --> B[게스트→호스트 리뷰<br/>다단계 Step]
    A --> C[호스트→게스트 리뷰]
    B --> D{양측 제출?}
    C --> D
    D -->|예| E[즉시 공개]
    D -->|14일 경과| E
    E --> F[프로필 노출<br/>Contextual*ProfileReviews]
```

카테고리 평점 6종: 청결도·정확도·체크인·의사소통·위치·가격대비.

---

## 8. 새 서비스 시사점 (제안)

- **2축 분리 채택**(33m2): 진행 축 × 결제 축을 별도 컬럼으로. 클라이언트가 조합 계산하지 않고 **서버가 액션 가용성 플래그 하달**(DOMAIN §4).
- **예약 이원화 도입 검토**(Airbnb): 즉시예약/예약요청. 33m2식 승인→결제 단선보다 전환·유연성 우위.
- **선결제 경쟁 승인 제거**(33m2 결함): 결제대기 진입 시 **홀드(hold)**로 선점 방지.
- 상태값은 이 문서의 enum을 기준선으로 삼되 신규 상태(예: 정산보류)는 명세 확정 시 추가.
