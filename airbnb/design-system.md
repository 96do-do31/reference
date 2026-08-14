# Airbnb DLS (Design Language System) 토큰

> 출처: `core-guest-spa/entrypoints/client.*.css` (1.5MB). **CSS 변수 1615개**.

> 사이드카: `_shared/captures/airbnb.design-tokens.json`


## 1. 폰트

| 용도 | 폰트 |
|---|---|
| 본문 | **`Airbnb Cereal VF`** (가변 폰트) |
| 레거시 폴백 | `Circular` → system-ui |
| 한국 결제 | **`kakaopay System Sans`** ← 카카오페이 연동 |
| 코드 | SFMono-Regular, Consolas, Menlo |

## 2. 코어 팔레트 (브랜드 네이밍)

| 토큰 | HEX | 역할 |
|---|---|---|
| `black` | `#000000` |  |
| `hof` | `#222222` | 본문 텍스트 |
| `foggy` | `#6A6A6A` | 보조 텍스트 |
| `bobo` | `#B0B0B0` | 비활성 텍스트 |
| `deco` | `#DDDDDD` | 보더 |
| `bebe` | `#EBEBEB` | 구분선 |
| `faint` | `#F7F7F7` | 배경 |
| `white` | `#FFFFFF` |  |
| `arches` | `#C13515` | 오류/경고 |
| `arches2` | `#B32505` | 오류 hover |
| `arches12` | `#FFF8F6` | 오류 배경 |
| `ondo` | `#E07912` | 주의 |
| `spruce` | `#008A05` | 성공 |
| `rausch` | `#FF385C` | **브랜드 (Airbnb Red)** |
| `product-rausch` | `#E00B41` | 제품 강조 |
| `plus` | `#92174D` | Airbnb Plus |
| `luxe` | `#460479` | Airbnb Luxe |

> 💡 색을 **의미가 아닌 고유 이름**(hof·foggy·bobo·deco·bebe·faint)으로 명명하고,
> 그 위에 `bg-*` / `text-*` / `border-*` 의미 토큰 102개를 얹는 2단 구조입니다.
> 리브랜딩 시 코어만 교체하면 되는 성숙한 설계 — 채택 권장.


### 의미 토큰 예시
```
--palette-bg-primary            #FFFFFF
--palette-bg-primary-hover      #F7F7F7
--palette-bg-primary-disabled   #F7F7F7
--palette-bg-primary-error      #FFF5F3
--palette-bg-primary-core       #FF385C
--palette-bg-primary-inverse    #222222
--palette-text-primary          #222222
--palette-text-primary-error    #C13515
--palette-text-primary-inverse  #FFFFFF
```
> 각 의미 토큰이 `-hover` `-disabled` `-error` `-inverse` 변형을 가집니다.


## 3. 타이포그래피

네이밍 규칙: `--typography-{카테고리}-{굵기}_{fontSize}_{lineHeight}-{속성}`

| 카테고리 | 스케일 (px) |
|---|---|
| `special-display-medium` | 40/44 · 48/54 · 60/68 · 72/74 |
| `titles-semibold` | 14/18 · 16/20 · 18/24 · 22/26 · 26/30 · 32/36 |
| `titles-medium` | 14/18 · 16/20 · 18/24 |
| `subtitles-book` | 14/18 · 16/22 · 18/24 |
| `body-paragraphs-text` | 14/20 · 16/22 |

> 크기·행간이 **토큰 이름에 박혀 있어** 사용처에서 값을 바로 알 수 있습니다.


## 4. 브레이크포인트

| 이름 | 값 | 사용 빈도 |
|---|---|---|
| (모바일 기준) | 375px | 2 |
| **sm** | **744px** | 22 (최다) |
| **md** | **950px** | 9 |
| **lg** | **1128px** | 12 |

> 744 / 950 / 1128 이 3대 브레이크포인트. 그 외 100여 개는 컴포넌트 국소 대응.


## 5. 컴포넌트 토큰 (`--dls-*`, 102개)
```
--dls-button_padding: 14px 24px
--dls-button_font-size: var(--typography-body-text_16_20-font-size)
--dls-base-input-internal-padding: 20px (top/bottom)
--dls-modal-header_height / background-color / border-color
```

## 6. 모션 (`--motion-*`, 34개)

스프링 타이밍 함수를 `linear(...)` 다항식으로 정의 (예: `--feedback-bar_spring-timing-function`).
페이지 전환 프리셋: `slide-up-from-bottom_duration: 667ms`, `--overlay-*` 애니메이션 토큰군.


## 7. 33m2와 비교

| 축 | 33m2 | Airbnb |
|---|---|---|
| CSS 변수 | 280 | **1,615** |
| 색상 토큰 | 73 (7색×10단계) | **349** (코어 17 + 의미 332) |
| 명명 | Tailwind식 `gray-500` | **고유명 + 의미 2단** |
| 타이포 | 22종 `typo-*` | 104 토큰, 크기 내장 명명 |
| 폰트 | Pretendard | Airbnb Cereal VF (자체 제작) |
| 프레임워크 | Tailwind v4 | 자체 DLS + linaria/aphrodite |
| 상태 변형 | 별도 클래스 | 토큰에 내장 (`-hover`/`-disabled`) |

> 🔵 **새 서비스 권장**: 33m2의 Tailwind 실용성 + Airbnb의 **2단 토큰 구조**(코어 팔레트 → 의미 토큰) 결합.
> 상태 변형(`-hover`/`-disabled`/`-error`)을 토큰 레벨에서 정의하면 다크모드·리브랜딩이 쉬워집니다.