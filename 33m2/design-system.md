# 33m2 디자인 시스템

> 출처: `web.33m2.co.kr` CSS 번들 (빌드 `live/20260813-074532-d5acc50`, 192KB) 파싱.
> 기계 판독용 사이드카: `_shared/captures/33m2.design-tokens.json`
> 프레임워크: **Tailwind CSS v4** (`@theme` 토큰 방식)

---

## 1. 폰트

```
font-family: Pretendard, "pretendard Fallback", ui-sans-serif, system-ui, sans-serif
```
국내 서비스 표준 웹폰트. 새 서비스도 동일 선택 권장 (한글 자간·가독성).

---

## 2. 타이포그래피 스케일 (22종)

| 토큰 | font-size | line-height | letter-spacing |
|---|---|---|---|
| `typo-display1` | 56px | 72px | -0.4px |
| `typo-display2` | 48px | 60px | -0.4px |
| `typo-display3` | 40px | 52px | -0.4px |
| `typo-title1` | 32px | 48px | -0.4px |
| `typo-title2` | 28px | 40px | -0.3px |
| `typo-title3` | 24px | 36px | -0.2px |
| `typo-headline1` | 22px | 34px | -0.2px |
| `typo-headline2` | 20px | 30px | -0.2px |
| `typo-headline3` | 18px | 26px | -0.1px |
| `typo-body1` | 16px | 24px | -0.1px |
| `typo-body1-reading` | 16px | **26px** | -0.1px |
| `typo-body2` | 15px | 22px | -0.1px |
| `typo-body2-reading` | 15px | **24px** | -0.1px |
| `typo-label1` | 14px | 20px | -0.1px |
| `typo-label1-reading` | 14px | **22px** | -0.1px |
| `typo-label2` | 13px | 18px | -0.1px |
| `typo-caption1` | 12px | 16px | -0.1px |
| `typo-caption2` | 11px | 14px | -0.1px |
| `typo-caption3` | 10px | 12px | -0.1px |

> 💡 **`-reading` 변형**이 흥미롭습니다. 같은 크기에서 **행간만 넓힌** 버전으로,
> 긴 본문(방 소개, 안내문)에 사용합니다. 한글 가독성을 위한 좋은 설계 — 채택 권장.
>
> 자간이 전 스케일에서 **음수**(-0.1 ~ -0.4px)입니다. Pretendard의 한글 조판 관행.

---

## 3. 컬러 팔레트 (73 토큰)

7개 색상 계열 × 10단계(50~900) + 흑백 + `gray-0`.

### Purple — 브랜드 (CTA·강조)
| | 50 | 100 | 200 | 300 | 400 | 500 | **600** | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|---|
| hex | `#f5f1ff` | `#e7e2f4` | `#ded5f6` | `#c6b5f6` | `#a78af7` | `#895ffc` | **`#7240fe`** | `#5227c9` | `#380dad` | `#280e6e` |

> `purple-600 #7240fe` = 주 브랜드 컬러. "계약 시작하기" CTA, 가격 강조, 활성 탭.

### Gray — 텍스트·배경·보더
| 토큰 | hex | 용도 추정 |
|---|---|---|
| `gray-0` | `#f8f8f8` | 최연한 배경 |
| `gray-50` | `#f4f4f4` | 섹션 배경 |
| `gray-100` | `#e2e2e2` | 구분선 |
| `gray-200` | `#d7d7d7` | 보더 |
| `gray-300` | `#c1c1c1` | 비활성 보더 |
| `gray-400` | `#aaa6a6` | 플레이스홀더 |
| `gray-500` | `#888686` | 보조 텍스트 |
| `gray-600` | `#696969` | |
| `gray-700` | `#4e4e4e` | |
| `gray-800` | `#353535` | |
| `gray-900` | `#252525` | 본문 텍스트 |
| `black` | `#000` | 강조 텍스트·버튼 |
| `white` | `#fff` | |

### Red — 오류·경고·취소
`50 #ffedef` · `100 #fee1e5` · `200 #ffbcc4` · `300 #fe8d9b` · `400 #fc6174` · **`500 #f04459`** · `600 #e62f45` · `700 #d21f35` · `800 #aa182a` · `900 #8d1624`

### Orange — 주의·할인
`50 #fff0ea` · `100 #fde1d5` · `200 #fdcbb7` · `300 #fbac8d` · `400 #ff8e61` · **`500 #fa6c34`** · `600 #f55719` · `700 #d8470e` · `800 #b54012` · `900 #98360f`

### Yellow — 배지·평점
`50 #fff8e2` · `100 #fcf2cf` · `200 #fcecb5` · `300 #fadf87` · `400 #ffd857` · **`500 #ffcd29`** · `600 #feb519` · `700 #e89e00` · `800 #b87e00` · `900 #9f6c00`

### Green — 성공·완료
`50 #eafdf3` · `100 #d7f4e5` · `200 #b5ebce` · `300 #90deb4` · `400 #4ccf89` · **`500 #0db45b`** · `600 #009d49` · `700 #00803c` · `800 #015d2c` · `900 #004420`

### Blue — 정보·링크
`50 #edf4ff` · `100 #e2ebfb` · `200 #d2e2fc` · `300 #accafb` · `400 #7ba8f1` · **`500 #4e90f9`** · `600 #2375f6` · `700 #0a58d3` · `800 #023c98` · `900 #022d71`

---

## 4. 반경 (radius)

| 토큰 | 값 |
|---|---|
| `xs` | 0.125rem (2px) |
| `sm` | 0.25rem (4px) |
| `md` | 0.375rem (6px) |
| `lg` | 0.5rem (8px) |
| `xl` | 0.75rem (12px) |
| `2xl` | 1rem (16px) |
| `3xl` | 1.5rem (24px) |
| (full) | `9999px` — 칩·필터 버튼 |

## 5. 간격 (spacing)

Tailwind v4 기본 배수 방식: `--spacing: 0.25rem` (4px) × n

## 6. 브레이크포인트

| 이름 | 값 | 비고 |
|---|---|---|
| (custom) | `375px` | **모바일 기준선** — 이 아래는 소형 대응 |
| (custom max) | `480px` | 소형 전용 규칙 |
| (custom) | `600px` | |
| `sm` | 40rem (640px) | |
| `md` | 48rem (768px) | |
| `lg` | 64rem (1024px) | 데스크톱 2단 레이아웃 전환 추정 |
| `xl` | 80rem (1280px) | |
| `2xl` | 96rem (1536px) | |

> 375px·480px 커스텀 브레이크포인트의 존재 = **모바일 우선 설계**의 증거.

## 7. 그림자

CSS에서 관찰된 실사용 그림자는 거의 없음 (`box-shadow: none` 다수).
**보더 + 배경 대비로 계층을 표현**하는 플랫한 디자인 언어.
`inset 0 0 0 1000px #00000026` = 이미지 오버레이 딤(15% 검정).

---

## 8. 캘린더 컴포넌트

`react-day-picker` (v9) 사용 — `--rdp-*` 커스텀 프로퍼티 다수 확인.

| 토큰 | 값 |
|---|---|
| `--rdp-day-width/height` | 44px |
| `--rdp-day_button-width/height` | 42px |
| `--rdp-day_button-border-radius` | 100% (원형) |
| `--rdp-months-gap` | 2rem |
| `--rdp-nav_button-size` | 2.25rem |
| `--rdp-disabled-opacity` | 0.5 |
| `--rdp-outside-opacity` | 0.75 |
| `--rdp-animation_duration` | 0.3s |
| `--rdp-animation_timing` | `cubic-bezier(0.4,0,0.2,1)` |

> 새 서비스도 동일 라이브러리를 쓰면 캘린더 UX를 빠르게 맞출 수 있습니다.
> 단, 33m2는 **범위 선택이 아니라 시작일 단일 선택**(`range_start/range_end` 토큰은 라이브러리 기본값)입니다.

---

## 9. 새 서비스 적용 시 권장

1. **타이포 토큰 체계를 그대로 차용** — 특히 `-reading` 변형 아이디어
2. **10단계 팔레트 구조 유지**, 브랜드 색만 교체
3. Pretendard 사용
4. Tailwind v4 `@theme` 토큰 방식 채택 (CSS 변수로 노출되어 런타임 테마 전환 용이)
5. 그림자 대신 **보더+배경 대비** 중심의 플랫 디자인 (한국 서비스 관행에 부합)
6. `react-day-picker` v9

> ⚠️ **색상 값을 그대로 복제하지 마세요.** 브랜드 아이덴티티는 고유해야 합니다.
> 여기 기록된 건 *스케일 구조와 단계 설계*를 참고하기 위한 것입니다.
