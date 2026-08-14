# 33m2 인증 · 계정 · 본인인증

> 출처: `/sign-in` `/sign-up` `/find-id` `/reset-password` 서버 렌더 페이로드 + JS 번들 Zod 스키마 + i18n 사전 + 세션 객체 실측.

---

## 1. 인증 아키텍처

```
Firebase Authentication  ──►  자체 백엔드  ──►  세션(JWT)
  (identitytoolkit.googleapis.com)
```

**세션 객체 (실측 스키마)**
```jsonc
{
  "uid": <number>,
  "accessToken": "<JWT>",
  "refreshToken": "<token>",
  "firebaseToken": "<token>",        // Firebase ID 토큰 보관
  "accessTokenExpiresAt": <epoch>,
  "expiresAt": <epoch>,
  "iat": <epoch>, "exp": <epoch>,    // JWT 표준 클레임
  "isHost": true,                    // 현재 모드
  "name": "...", "email": "...",
  "profileImageUrl": "...",
  "aid": "...",                      // 애널리틱스 ID 추정
  "rememberMe": true,
  "blocked": false,                  // 계정 정지
  "certified": true,                 // 본인인증 완료
  "verificationStatus": "..."        // 아래 enum
}
```

> 3중 토큰 구조: Firebase 토큰으로 1차 인증 → 자체 `accessToken`(만료 시각 포함) + `refreshToken` 발급.
> `isHost`가 세션에 들어있음 → **모드 전환이 세션 갱신을 동반**할 가능성 ❓

**인증 제공자** (JS 상수)
```
EMAIL_PASSWORD_PROVIDER · PHONE_PROVIDER · RECAPTCHA_ENTERPRISE
```
> reCAPTCHA Enterprise 사용 — 봇 방어.

---

## 2. 라우트 & 접근 경계 ✅ 실측

**공개 (비로그인 200)**
```
/guest/main · /guest/search · /guest/room/{rid}
/guest/support · /guest/support/faq · /guest/notice
/guest/campaign/event · /guest/campaign/article
/host/main            (호스트 랜딩)
/terms/using · /terms/privacy-policy
/sign-in · /sign-up · /find-id · /reset-password
```

**보호 (307 리다이렉트)**
```
/guest/contract · /guest/chat · /guest/notification · /guest/my/*
/host/room · /host/contract · /host/pay · /host/my/*
        ↓
/sign-in?redirect={인코딩된 원래 경로}
```

> ⭐ **되돌아갈 경로를 쿼리로 보존**하는 표준 패턴. 새 서비스도 동일하게.
> ⭐ 매물 상세까지 완전 공개 → **SEO 확보**. (Airbnb와 동일 전략)

---

## 3. 회원가입 플로우

`sign-up` 관련 i18n 네임스페이스가 단계를 드러냅니다:

| 네임스페이스 | 단계 |
|---|---|
| `signup_user_role` | **역할 선택** (임차인 / 임대인) |
| `signup_guest_landing` / `signup_landlord_landing` | 역할별 랜딩 |
| `signup_terms` | 약관 동의 |
| `signup_information` | 기본 정보 입력 |
| `signup_survey` / `signup_survey_landlord` | **가입 설문** |
| `signup_bank_account` (36키) | **정산 계좌 등록** (임대인) |
| `signup_complete` | 완료 |

> 라우트는 `/sign-up` 단일 페이지 + 클라이언트 상태 기반 단계 진행 (하위 경로 404 확인).

### 가입 페이로드 (Zod 스키마 실측)
```ts
{
  email: string,
  password: string,
  name: string,
  certNum: string,                  // 본인인증 번호
  marketingAgree: boolean,
  profileImageUrl: string,
  passportImageUrl: string,         // 외국인
  phoneNumber: string,
  hostIntro: string,                // 임대인 소개
  recommenderPhoneNumber: string,   // ★ 추천인 전화번호
  ocrToken: string,                 // ★ 신분증 OCR 토큰
  emailCertified: boolean
}
```
> 🆕 **추천인 제도**와 **신분증 OCR**이 존재합니다. 기존 문서에 없던 개념.

### 입력 검증 규칙 ✅
| 필드 | 규칙 | 에러 문구 |
|---|---|---|
| 이메일 | 형식 검증 | "이메일 형태로 입력해 주세요." / "수신 가능한 이메일 주소를 입력해 주세요" |
| 비밀번호 | **영문·숫자 조합 6~15자** | "영문, 숫자 조합 6자-15자로 입력해 주세요." |
| 비밀번호 확인 | 일치 | "비밀번호가 일치하지 않습니다." |
| 이름 | **10자 이하**, 특수문자 제한 | "이름은 10자 이하로 입력해 주세요." / "사용할 수 없는 문자가 포함되어 있습니다." |
| 중복 | 이메일 중복 검사 | "이미 가입된 계정이 있습니다" |

---

## 4. 본인인증 (Verification) ★

### 상태 enum — `VerificationStatus`
```
NONE · PENDING · EMAIL_SENT · ID_VERIFIED · CERTIFIED · HOLD
```

| 값 | 의미 (UI 문구 대응) |
|---|---|
| `NONE` | 미인증 — "본인인증 필요" |
| `PENDING` | 심사 중 — "여권 심사중" |
| `EMAIL_SENT` | 이메일 인증 메일 발송 — "이메일 인증 필요" |
| `ID_VERIFIED` | 신분 확인 완료 |
| `CERTIFIED` | 인증 완료 — "본인인증이 완료되었습니다" |
| `HOLD` | 보류 — "여권 인증 보류" → "여권 다시 등록하기" |

동반 필드: `certType`(인증 종류, nullable) · `passportImageUrl` · `holdReason` · `detailReason`(nullable) · `emailCertified` · `isCertificated`

### 🔒 핵심 게이트
> **"본인인증이 완료된 후 계약을 진행할 수 있습니다."**

⇒ 계약 요청의 **전제조건이 본인인증**입니다. 새 서비스도 동일 게이트가 필요합니다(임대차는 신원 확인이 법적·실무적으로 필수).

### 내국인 — 휴대폰 본인인증
통신사 enum: `SKT · KT · LGU · SKTMVNO · KTMVNO · LGUMVNO`
(알뜰폰 MVNO 3사 별도 — 국내 본인인증 표준)
관련 네임스페이스: `verify_phone`(55키) · `phone_verify` · `verification`(19키)

### 외국인 — 여권 인증
- 네임스페이스 `passport_verification` (54키)
- 여권 이미지 업로드 → **심사 대기** → 승인/보류
- **"심사에는 최대 1일이 소요됩니다."**
- 보류 시 사유(`holdReason`) 제공 + 재등록
- `ocrToken` — 신분증 OCR 사전 처리

> 🌏 **외국인 임차 수요**를 정면으로 지원합니다. 한달살기·중장기 체류 시장에서 중요한 축.
> 새 서비스도 초기부터 고려할 것.

### 이메일 인증
네임스페이스: `email_verification`(24) · `email_verify`(11) · `email_verification_required`(2) · `change_email`(11)
"인증 완료하기" 버튼 → `emailCertified: true`

---

## 5. 계정(User) 엔티티 — Zod 실측 17필드

```ts
{
  email: string,
  name: string,
  profileImageUrl: string,
  phoneNumber: string,
  userType: enum,                  // 임차인/임대인 구분 추정
  isCertificated: boolean,
  certType: enum | null,
  passportImageUrl: string,
  verificationStatus: enum,        // 위 6종
  holdReason: string,
  detailReason: string | null,
  hostIntro: string,               // 임대인 소개 (30자)
  isSuperHost: boolean,            // 우수 임대인
  bankName: string,                // 정산 계좌
  bankAccount: string,
  bankHolder: string,
  emailCertified: boolean
}
```

> **단일 User 테이블에 게스트·호스트 속성이 공존**합니다 (`hostIntro`, `isSuperHost`, `bank*`).
> 별도 Host 테이블이 아니라 역할 플래그 방식.

---

## 6. 계정 관련 화면

| 경로 | 화면 | i18n |
|---|---|---|
| `/sign-in` | 회원 로그인 + [아이디 찾기] [비밀번호 찾기] | `login`(17) |
| `/sign-up` | 가입 (다단계) | `signup_*` 9종 |
| `/find-id` | 아이디 찾기 | `find_id`(15) |
| `/reset-password` | 비밀번호 재설정 | `reset_password`(19) · `find_password` · `find_pw` |
| `/guest/my/account` · `/host/my/account` | 계정 정보 | `account`(82) · `user_information`(9) |
| `/{role}/my/account/delete` | 회원탈퇴 | |
| `/guest/my/notification` | 알림 설정 | `notification`(65) |

---

## 7. 계정 상태 / 제재

| 플래그·코드 | 의미 |
|---|---|
| `session.blocked` | 계정 정지 |
| `BLOCKED_USER` (JS 상수) | 차단 사용자 처리 분기 |
| i18n `dialog.title` | "규정 위반으로 이용이 중지되었습니다" (고객센터 33m2@spacev.kr 안내) |
| `error.restricted` | "비정상적인 트래픽이 감지되어 접속이 제한되었습니다" |
| `ENFORCEMENT_STATE_UNSPECIFIED` | reCAPTCHA Enterprise 상태 |
| 에러 코드 | `AUTH_001~012` · `USER_001~020` · `CERT_002~019, 099` |

---

## 8. 새 서비스 적용 권장

1. **본인인증을 계약의 전제조건**으로 (33m2와 동일) — 임대차 신원 확인은 필수
2. **외국인 여권 인증 트랙**을 초기부터 설계 (심사 대기 상태 포함)
3. 알뜰폰 MVNO 포함 통신사 인증
4. `redirect` 파라미터로 로그인 후 복귀
5. 비로그인 열람 전면 허용 (SEO)
6. 단일 User + 역할 플래그 (별도 Host 테이블 금지)
7. `verificationStatus`를 6단계로 세분화 (특히 `HOLD` + 사유)
8. 추천인·OCR은 선택 — 초기 MVP에서는 제외 가능
