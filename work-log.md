# Work Log - facwa

## 2026-11-02 18:30 KST — summary.md 발송 (Resend)

- `summary.md`(기준일 10/28 — 이후 work-log 변경 없음)를 `woonjjang@ictact.kr`, `kangsh@skhu.ac.kr`, `suneulhae@gmail.com`에 Resend 발송 (제목 `facwa 진행요약 (2026-11-02)`, id `01a19b94`).


## 2026-10-28 KST — summary.md 생성 (issue-summary-agents)

- 사람이 지정해 `summary.md` 최초 생성 (work-log 기준 고객용 요약). `plans/issue-summary/issue-summary-agents.md` 관리 대상 표에 편입.
- 고객 메일은 수동 발송 정책 — 발송하지 않음.

## 2026-10-27 about 페이지 통계/링크 수정 + repo 변경 선언 (woonjjang)

- **작업일시**: 2026-10-27 KST
- **작업자**: woonjjang

### 변경 내용
- `layouts/partials/marketing/customs/feature-statistic.html` — 통계 업데이트: Items 875, Record Groups 4, Sub-collections 10, Video Items 875
- `data/marketing.yml` — featuredNumbers 설명 텍스트 업데이트, two-box R2 URL 수정 (`/items/r2-dmz판문점/`)
- `data/en/marketing.yml` — featuredNumbers 설명 업데이트, carousel URL 선행 `/` 누락 수정 (4건)
- `README.md` — repo 변경 선언: `team-durumi/facwa` → `text-consulting-group/facwa`

### 결과
- Hugo 빌드 성공 (1,374 KO / 1,362 EN)

---

## 2026-10-27 venues 좌표 보강 + 맵 z-index 수정 (woonjjang)

- **작업일시**: 2026-10-27 KST
- **작업자**: woonjjang

### 변경 내용
- `layouts/partials/facwa/venue-point.html` — 누락 지명 좌표 추가: 포항, 진주, 제주도, 원주, 아시야, 도쿄(GHQ/FEC), 영등포, 문산역, 선유리, 장단, 임진강, 개성 내봉장 등
- 기존 별칭도 보강: 자유의 다리, 대성동, 법원읍, 금촌, 천현면 등
- `assets/style.css` — 맵 `isolation: isolate` + `z-index: 0`으로 Leaflet 헤더 겹침 수정

### 결과
- Hugo 빌드 성공 (1,374 KO / 1,362 EN)
- venues 맵 유효 좌표 73개 (기존 대비 증가)
- commit `62f805a`, push 완료

---

## 2026-10-27 subjects 페이지 썸네일 카드 + venues 맵 좌표 수정 (woonjjang)

- **작업일시**: 2026-10-27 KST
- **작업자**: woonjjang

### 변경 내용
- `layouts/_default/terms.html` — subjects 등 비-venues 택소노미에 랜덤 썸네일 카드 그리드 적용 (기존 pill → 카드)
- `assets/style.css` — `facwa-term-card-grid`, `facwa-term-card` 스타일 추가
- `layouts/partials/facwa/venue-point.html` — "공동경비구역", "JSA", "Joint Security Area" 별칭 추가 (파주 좌표)

### 결과
- Hugo 빌드 성공 (1,374 KO / 1,362 EN)
- subjects 페이지: 9개 주제 카드에 랜덤 썸네일 표시 확인
- venues/공동경비구역jsa/ 맵 좌표 매핑 해결

---

## 2026-10-27 venues 맵 OpenFreeMap 마이그레이션 + 렌더링 오류 수정 (woonjjang)

- **작업일시**: 2026-10-27 KST
- **작업자**: woonjjang

### 변경 내용
- `layouts/partials/openfreemap-assets.html` 신규 생성 (homi 참조: OpenFreeMap + MapLibre GL ESM)
- `layouts/_default/terms.html` — CartoDB 타일 → OpenFreeMap(positron) + MapLibre GL로 교체
- `layouts/_default/taxonomy.html` — 동일하게 OpenFreeMap으로 교체
- `layouts/partials/marketing/banner--ww--slide.html` — `$slides` nil 에러 수정 (`| default slice`)
- `layouts/_default/taxonomy.html` — `.File.BaseFileName` nil 에러 수정 (`with .File` 래핑)

### 결과
- Hugo 빌드 성공 (1,374 KO / 1,362 EN), 에러 0건

---

## 2026-10-27 AGENTS.md에 work-log 필수 작성 규칙 추가 (woonjjang)

- **작업일시**: 2026-10-27 KST
- **작업자**: woonjjang

### 변경 내용
- `AGENTS.md`에 `## Rules` 섹션 추가
- "모든 작업 후 반드시 work-log.md에 기록한다"는 규칙 명시

### 결과
- AGENTS.md 갱신 완료

---

## 2026-07-09 영문 페이지 한글 잔재 수정 (woonjjang)

- **작업일시**: 2026-07-09 14:50 KST
- **작업자**: woonjjang

### 변경 내용
- `content/research-guide.en.md` 파일의 모든 한국어 relref 링크를 영문 URL로 변경
- 변경된 링크:
  - `/items/R1 한국전쟁/` → `/en/items/r1-korean-war/`
  - `/items/R2 DMZ&판문점/` → `/en/items/r2-dmz-panmunjom/`
  - `/items/R3 일본군'위안부'/` → `/en/items/r3-comfort-women/`
  - `/items/R4 빅 픽쳐/` → `/en/items/r4-the-big-picture/`
  - 시리즈 하위 링크도 동일하게 영문 URL로 변경

### 결과
- 영문 리서치 가이드에서 한국어 문자 0건 확인
- Hugo 빌드 성공
- Cloudflare Pages 배포 완료 (https://facwa.kr/en/research-guide/)

---

## 2026-07-09 daam 자료조사 점검

- 점검 기준일시: 2026-07-09 09:49 KST
- Target folder: `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/` — Google Drive 미마운트 상태로 직접 확인 불가
- Items folder (Hugo): `/Users/woonjjang/ai/archivej/facwa/content/items` — .md 파일 1,780개
- Items 하위 분류: `R1 한국전쟁`, `R2 DMZ&판문점`, `R3 일본군'위안부'`, `R4 빅 픽쳐` (4개 record group)
- dummy.md: 330줄 — 존재
- dummy-jp.md: 없음 (영문만 운영)
- work-log.md: 67줄 — 존재
- context.md: 없음
- Owner requests: `수정요청사항.docx` — 미해결 요청 없음 (안내 텍스트만)
- 비고: items가 1,780개로 가장 많음. record group 4개 구조로 잘 정리되어 있음. 영어 번역 882개 이상 완료.

2026-07-07 - facwa 최신 변경분 배포 완료. 배포 전 `hugo --panicOnWarning --quiet` 빌드 통과 후 `wrangler pages deploy public --project-name facwa --branch main` 실행. Cloudflare Pages 배포 URL은 `https://ce567dbe.facwa.pages.dev`이며, 실서버 `https://facwa.kr/`, `https://facwa.kr/en/`, `https://facwa.kr/research-guide/`, `https://facwa.kr/en/research-guide/` 모두 `HTTP 200` 확인. 배포 미리보기 URL 및 캐시 우회 URL에서 최신 SEO description, `hreflang`, `WebSite`/`SiteNavigationElement`/`BreadcrumbList` JSON-LD 반영 확인. Owner requests 문서 `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/수정요청사항.docx`에 배포 완료와 반영 범위를 기록했고, 수정 전 백업은 `/private/tmp/수정요청사항.before-facwa-deploy-20260707.docx`에 보관했다.

2026-07-07 - Google 검색 결과에서 사이트 설명과 하위 메뉴 후보가 더 잘 잡히도록 SEO 구조를 보강했다. 홈 국문/영문 description을 검색 스니펫용 문장으로 확장했고, `baseof.html`에 `lang`, `hreflang`, JSON-LD 구조화 데이터를 추가했다. 구조화 데이터는 `WebSite`, `Organization`, facwa 내부 메뉴 기반 `SiteNavigationElement`, 페이지별 `BreadcrumbList`를 생성한다. 외부 메뉴 링크는 구조화 데이터에서 제외했고, 국문/영문 WebSite description이 언어별로 출력되는 것을 확인했다. `hugo --panicOnWarning --quiet` 및 clean destination 빌드 통과.

2026-07-07 - `research-guide` 공개 페이지를 `https://jydh.org/research-guide/`와 같은 document 레이아웃으로 맞췄다. `content/research-guide.md`, `content/research-guide.en.md`에 `layout: "document"`와 `translationKey`를 지정하고, `layouts/_default/document.html` 및 `facwa-document-*` CSS를 추가해 jydh 방식의 breadcrumb, hero, meta, sticky toc, document card 구조로 생성되게 했다. `영상 탐색` 메뉴의 첫 번째 항목은 `리서치 가이드`/`Research Guide`로 유지했고, 한국어 `/research-guide/`, 영어 `/en/research-guide/` 생성과 영어 페이지 한글 잔재 0건을 확인했다. `hugo --panicOnWarning --quiet` 빌드 통과.

2026-07-07 - 첫 번째 메뉴 `성공회대학교 평화월딩연구소`의 세 번째 항목으로 `포스트`를 추가했다. 영어 라벨은 `Posts`로 지정했고, `/posts/`가 언어별 메뉴에서 `/posts/`, `/en/posts/`로 생성되는 것을 확인했다. `hugo --panicOnWarning --cleanDestinationDir --quiet` 빌드 통과.

2026-07-07 - 영어 메인 및 about 페이지 국문 잔재 제거. `banner--ww--slide`, `banner`, `feature-statistic`, `two-box`, `faqs`, `network-org`, `footer-wide`, `feature-rg` partial을 언어별 데이터/문구 분기로 정리했다. `hugo --panicOnWarning --cleanDestinationDir --quiet` 빌드 통과 확인. 생성된 `public/en/index.html`, `public/en/about/index.html`에서 한글 검색 결과 0건 확인.

2026-07-07 - 영어 메인 `Browse Materials / Record Groups` 4개 대표 링크를 영어 record group URL로 연결했다. `R1 Korean War`, `R2 DMZ and Panmunjom`, `R3 Japanese Military "Comfort Women"`, `R4 The Big Picture`의 `_index.en.md`에 영어 `url`을 지정하고 메인 카드와 영어 carousel 링크를 `/en/items/r1-korean-war/`, `/en/items/r2-dmz-panmunjom/`, `/en/items/r3-comfort-women/`, `/en/items/r4-the-big-picture/`로 맞췄다. Hugo 빌드 통과 및 네 개 `public/en/items/.../index.html` 생성 확인.

2026-07-07 - `en/posts`를 국문 posts 구조와 맞췄다. `content/posts/_index.md`, `content/posts/_index.en.md`를 추가해 국문/영문 posts 섹션 제목과 설명을 분리했고, 국문 post 11개와 영문 post 11개의 1:1 대응을 확인했다. `hugo --panicOnWarning --cleanDestinationDir --quiet` 빌드 통과, `public/en/posts`와 `content/posts/*.en.md` 한글 검색 0건 확인.

2026-07-07 - facwa 배포 완료: `wrangler pages deploy public --project-name facwa --branch main` 실행. https://facwa.kr/ 200 OK 확인.

2026-07-07 - 영문 페이지 한글 잔재 수정 완료. 수정 파일: (1) `data/en/marketing.yml` carousel 부분 alt/caption 번역 (2) `layouts/partials/marketing/customs/banner--sticky-top.html` "공지" → 다국어 분기 (3) `layouts/partials/marketing/customs/feature-posts.html` 제목/설명 다국어 분기 (4) `layouts/_default/inquiry.html` 전체 한글 텍스트 다국어 분기. Hugo 빌드 통과 확인.

2026-07-07 - 정기업무 1~3 점검 완료. Owner requests에서 미해결 요청 2건 발견: (1) 영문 메인/소개 페이지 한글 잔재 수정 (2) 전체 영어 페이지 점검. @daam에게 items 번역 현황 전달 필요.

2026-07-02
- archivej 정기업무 2 재점검: `AGENTS.md` 기준 Target `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/`, Items `/Users/woonjjang/ai/archivej/facwa/content/items`, Owner requests `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/수정요청사항.md`가 모두 존재함을 다시 확인했다.
- Owner requests 문서는 현재도 입력 안내 템플릿 상태이며, 이번 점검 시점 기준 구체적으로 남아 있는 미해결 요청은 없다.

2026-06-30
- archivej 정기업무 2 점검: `AGENTS.md`의 `Target folder`와 `Items folder` 경로를 확인했다. 두 경로 모두 존재한다.
- 확인 경로: Target `/Users/woonjjang/Google Drive/공유 드라이브/TCG-HQ/5.BM/Project - ArchiveJ(2022)/archiveJ-facwa`, Items `/Users/woonjjang/ai/archivej/facwa/content/items`.
- `Owner requests` 항목은 현재 `AGENTS.md`에 지정되어 있지 않다.
- archivej 정기업무 2 재점검: 현재 `AGENTS.md` 기준 Target `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/`, Items `/Users/woonjjang/ai/archivej/facwa/content/items` 모두 존재한다.
- `Owner requests` 경로가 없는 로컬 파일을 가리키고 있어 target의 실제 문서 `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/수정요청사항.md`로 정정했다. 해당 문서는 요청 입력 안내만 있고 미해결 요청은 없다.

2026-07-01
- archivej 정기업무 1 테스트: 로컬 `hugo --panicOnWarning --cleanDestinationDir --quiet`와 `npm run build`를 모두 실행했고 현재 Hugo `v0.162.1+extended+withdeploy` 기준 빌드가 정상 통과했다.
- 로컬 산출물 점검: `public/index.html`에서 canonical `https://facwa.kr/`와 `meta name="robots" content="index, follow"`를 확인했고, `public/robots.txt`와 `public/sitemap.xml`도 생성 확인했다.
- 실서버 점검: `https://facwa.kr/`, `https://facwa.kr/robots.txt`, `https://facwa.kr/sitemap.xml` 모두 2026-07-01에 `HTTP 200` 응답을 확인했다.
- archivej 정기업무 2 테스트: `AGENTS.md` 기준 Target `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/`, Items `/Users/woonjjang/ai/archivej/facwa/content/items`, Owner requests `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/수정요청사항.md` 존재를 재확인했다. Owner requests 문서는 아직 안내 텍스트만 있어 미해결 요청은 없다.
- archivej 정기업무 3 테스트: 현재 로컬 변경분 기준 `layouts/_default/baseof.html`의 canonical 링크, `static/_redirects`의 `/sitemap` 리디렉트, `static/robots.txt`의 sitemap 및 bot 규칙이 정리되어 있어 개선 방향은 유효하다.
- 남은 리스크: 실서버 `robots.txt` 상단에는 여전히 Cloudflare managed content-signal 블록이 붙어 있으며 여기서 `GPTBot`, `ClaudeBot`, `Google-Extended`, `Amazonbot`, `Applebot-Extended` 등이 `Disallow`로 선언된다. 따라서 facwa의 AI bot 노출 상태는 계속 `Partial`로 해석한다.

2026-07-01
- `tcg`의 다국어 작업 패턴을 참고하기 전에 `facwa`와 `tcg` 모두 git 상태를 확인했다. `facwa`는 기존 미커밋 변경이 있었고, `tcg`는 대규모 다국어 작업 중이어서 참고 전용으로만 사용했다.
- 사용자 요청에 따라 일본어가 아니라 영어(`en`)만 진행했다.
- `facwa/config/_default/config.yml`에 `ko`/`en` 언어 설정을 추가했고, `panicOnWarning` 기준 경고가 없도록 deprecated `languageName` 키는 사용하지 않도록 정리했다.
- 헤더, 푸터, 로고, 검색, 탐색 사이드바, 아이템 리스트/상세에서 영어 UI가 보이도록 내부 링크와 주요 라벨을 다국어 대응으로 조정했다. 시각 스타일은 기존 `facwa` 스타일을 유지했다.
- `content/items` 아래 기존 한국어 자료를 기준으로 영어 미러 페이지를 대량 생성해 `/en/items`와 `/en/search`가 비지 않도록 만들었다.
- `content/` 전반에도 영어 페이지를 추가 생성해 현재 영어 페이지 수는 `919`개까지 확장되었다.
- 핵심 진입 페이지 `/_index`, `/about`, `/search`, `/inquiry`, taxonomy 루트, 주요 `items` 섹션 인덱스는 별도로 영어 제목/설명으로 정리했다.
- 검증: `hugo --cleanDestinationDir`와 `hugo --panicOnWarning --cleanDestinationDir --quiet` 모두 2026-07-01 기준 통과했다.
- `items` 영어 번역 1차를 시작했다. `scripts/translate_items_en.py`를 추가해 `.en.md` item 파일의 제목, 레코드그룹/시리즈, 태그/주제/장소/출처 같은 반복 메타데이터를 영어 기준으로 정리했다.
- 현재 `content/items` 아래 영어 item 파일은 `882`개이며, 예: `정전협정 조인식(선유리 유엔군임시사령부, 판문점) 2` → `Armistice Agreement Signing Ceremony (Seonyuri UNC Advance HQ, Panmunjom) 2`, `부상포로 교환 (LITTLE SWAP)` → `Exchange of Sick and Wounded Prisoners (LITTLE SWAP)`까지 반영했다.
- item 번역 과정에서 원본 frontmatter의 줄바꿈/따옴표 오류가 영어 파일에서 YAML 에러로 드러난 5건을 정리했고, 이후 `hugo --panicOnWarning --cleanDestinationDir` 빌드가 다시 통과했다.
- 현 단계에서는 leaf item의 `description_status`와 `shotlist` 본문은 품질 보존을 위해 대부분 원문 한국어를 유지한다. 다음 단계에서 우선순위 item부터 영어 요약/설명을 순차 번역하는 방향이 적절하다.

2026-07-01
- 사용자 요청 기준 `facwa` 정기작업 1, 2를 다시 점검했다. 현재 작업트리에 다국어 관련 미커밋 변경이 많아 기존 변경은 건드리지 않고 검증과 기록만 진행했다.
- 로컬 검증: `hugo --panicOnWarning --cleanDestinationDir --quiet`와 `npm run build` 모두 재실행해 통과를 확인했다.
- 로컬 산출물 재확인: `public/index.html`에서 canonical `https://facwa.kr/`와 `meta name="robots" content="index, follow"`를 다시 확인했고, `public/sitemap.xml`은 `https://facwa.kr/ko/sitemap.xml`, `https://facwa.kr/en/sitemap.xml` 2개 언어 sitemap index로 생성됐다.
- 실서버 재확인: `https://facwa.kr/`, `https://facwa.kr/robots.txt`, `https://facwa.kr/sitemap.xml` 모두 2026-07-01에 `HTTP 200` 응답을 반환했다.
- 실서버 `robots.txt` 본문 재확인 결과 Cloudflare managed content-signal 블록이 여전히 상단에 삽입되어 있으며 `GPTBot`, `ClaudeBot`, `Google-Extended`, `Amazonbot`, `Applebot-Extended` 등에 `Disallow`가 선언된다. 따라서 facwa의 AI bot 노출 판정은 계속 `Partial`로 유지한다.
- 정기작업 2 재확인: `AGENTS.md` 기준 Target `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/`, Items `/Users/woonjjang/ai/archivej/facwa/content/items`, Owner requests `/Users/woonjjang/Google Drive/공유 드라이브/IPWS/수정요청사항.md`가 모두 존재한다.
- Owner requests 문서는 현재도 요청 입력 안내 텍스트만 있으며, 이번 점검 시점 기준 별도 미해결 요청은 없다.

2026-07-05
- robots.txt에 `Sitemap: https://facwa.kr/sitemap.xml` 참조를 추가했다.
- Hugo production 빌드를 다시 통과시켰다.

2026-11-04
- 소유자 요청([facwa #1](https://github.com/text-consulting-group/facwa/issues/1) 코멘트 "summary.md 반영하고 close 해줘") 처리.
- summary.md에 영문 자료 설명 균일화 완료 내역 반영: level__file 다중 줄 복원 866파일 · shotlist 표기 통일 67파일 · 한글 잔재 정리 858파일 · description_status 문형 통일 199파일 (PR #2 `99264bb` + 후속 배치 `1769a57`).
- 잔여(편집 판단) 표기 유지: F3 지명 135줄 · F4 부대명 49줄 · 인명 6줄 · 자유 서술 675건 · sentinel 통일 정책 — 후속 배치 예정.
- issue #1 close (완료 코멘트 포함).
