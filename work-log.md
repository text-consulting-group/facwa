# Work Log - facwa

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
