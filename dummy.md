# Dummy Notes - facwa

작성일: 2026-07-01
대상 프로젝트: `facwa`
프로젝트 유형: `digital-archives`

## 1. 목적

이 문서는 `facwa` Hugo 프로젝트의 현재 `content/` 구조와 국문/영문 콘텐츠 상태를 빠르게 파악하기 위한 작업 기반 문서다.

- 이후 `/items`, `/posts`, `/about`, taxonomy, search, multilingual QA 작업의 출발점으로 사용한다.
- 특히 영어(`en`) 페이지는 수량상으로는 많이 생성되었지만, 본문 품질은 아직 균일하지 않으므로 이 문서에서 현재 상태를 구분해 둔다.

## 2. 콘텐츠 전체 통계

`content/` 기준 전체 파일 수

- 국문(`ko`) 파일: 928
- 영문(`en`) 파일: 911
- 합계: 1839

`content/items/` 기준 파일 수

- 국문 item 파일: 882
- 영문 item 파일: 882
- item 계층은 현재 국문/영문 파일 수가 동일하다.

대표 관찰

- `content/items/`는 국문과 영문이 1:1 대응하도록 맞춰진 상태다.
- `content/posts/`, `content/pages` 계층도 영문 파일이 존재하지만, 상당수는 아직 국문 본문 복제 상태다.
- 즉, “영문 경로가 열린 상태”와 “영문 본문 품질이 완성된 상태”는 다르다.

## 3. `content/` 구조 개요

최상위 주요 콘텐츠 파일/폴더

- `_index.md`, `_index.en.md`
- `about.md`, `about.en.md`
- `browse.md`, `browse.en.md`
- `search.md`, `search.en.md`
- `inquiry.md`, `inquiry.en.md`
- `library.md`, `library.en.md`
- `promotions.md`, `promotions.en.md`
- `symposium-210327.md`, `symposium-210327.en.md`
- `posts/`
- `categories/`
- `creators/`
- `subjects/`
- `sources/`
- `venues/`
- `shorts/`
- `items/`

해석

- 메인 소개형 페이지와 실험/보조 페이지가 함께 존재한다.
- 실운영 핵심은 `items`, `posts`, `about`, `search`, taxonomy 계층이다.
- `browse`, `library`, `promotions`, `symposium-210327`는 보조적이거나 실험적 성격이 섞여 있다.

## 4. 메인/소개 페이지 읽기 메모

### 4-1. 홈

국문 `content/_index.md`

- 제목: `홈`
- 설명: `평화월딩영상아카이브`

영문 `content/_index.en.md`

- 제목: `Home`
- 설명: `Peace Worlding Film Archives`

메모

- 현재 홈 자체는 frontmatter가 매우 얇고, 실제 화면 구성은 레이아웃/partial 중심이다.

### 4-2. 소개 페이지

국문 `content/about.md`

- 제목: `소개합니다.`
- 설명: 영상 자료를 “거대한 수집기관”보다 “미군 영상카메라맨이 소속된 부대명칭” 기준으로 추적하게 정리했다는 방향성이 드러난다.

영문 `content/about.en.md`

- 제목: `About`
- 설명: footage의 holding institution보다 production context와 military unit을 추적하는 구조라는 점을 강조한다.

메모

- 국문/영문 모두 실제 본문 텍스트보다는 partial 조합으로 페이지를 렌더링한다.
- 영어 소개는 짧지만 방향 설명은 들어가 있다.

## 5. 포스트(`content/posts`) 읽기 메모

포스트 수

- 국문: 11
- 영문: 11

포스트 범주

- `meetings`: 학술회의/심포지엄
- `articles`: 논문
- `books`: 책
- `projects`: 사업

대표 포스트 관찰

### 5-1. `post-01`

- 분류: `meetings`
- 주제: 냉전아시아, 한국전쟁/냉전 영상, NARA 자료, 시각자료 생산·관리 맥락
- 상태:
  - 국문은 상세 행사 소개와 프로그램이 있다.
  - 영문 파일은 존재하지만 현재 본문은 국문 그대로다.

### 5-2. `post-05`

- 분류: `articles`
- 주제: 한국전쟁 푸티지영상 연구 방법론, cataloging, 메타데이터, 교차분석
- 상태:
  - 국문은 논문 초록 및 링크까지 포함
  - 영문 파일은 존재하지만 현재 국문 복제 상태

### 5-3. `post-08`

- 분류: `books`
- 주제: 작은 ‘한국전쟁’들, 비주얼 히스토리, 사진/영상 기반 한국전쟁 재해석
- 상태:
  - 국문은 상세한 책 소개가 정리되어 있음
  - 영문 파일은 존재하지만 현재 국문 복제 상태

포스트 전반 메모

- 포스트는 사이트의 연구성과/행사/출판/사업 성격을 가장 직접적으로 보여준다.
- 그러나 영어 품질은 아직 “파일 존재” 수준이며, 실제 번역/요약 작업이 많이 남아 있다.

## 6. 카테고리 및 taxonomy 구조 메모

### 6-1. 카테고리 루트

국문

- `카테고리`: 공지를 포함한 블로그 콘텐츠 분류

하위 카테고리

- `논문`
- `책`
- `학술회의`
- `사업`

영문

- `Categories`: projects, meetings, articles, books 탐색 진입점

메모

- 영문 루트 설명은 정리되었지만, 하위 category 콘텐츠는 대부분 국문 기반 요약 또는 미번역 상태로 볼 필요가 있다.

### 6-2. 인명/주제/출처/장소

루트 폴더

- `creators/`
- `subjects/`
- `sources/`
- `venues/`

메모

- 이들은 `items` 메타데이터에서 자동 파생되는 탐색 축이다.
- 영문 루트 파일은 만들어졌지만, 실제 term 페이지의 영문 품질은 item 번역 품질과 직접 연결된다.

## 7. `items` 구조 상세 메모

`items`는 이 프로젝트의 핵심 콘텐츠다.

루트

- `content/items/_index.md`
- `content/items/_index.en.md`

국문 루트 설명

- 성공회대학교 평화월딩연구소 수집자료

영문 루트 설명

- Institute for Peace and Worlding Studies collected records

### 7-1. Record Group 구성

국문/영문 공통 파일 수

- `R1 한국전쟁`: 111
- `R2 DMZ&판문점`: 54
- `R3 일본군’위안부’`: 10
- `R4 빅 픽쳐`: 706

해석

- `R4 빅 픽쳐` 비중이 압도적으로 크다.
- `R1`, `R2`는 한국전쟁 포로/정전/DMZ 축에서 연구 가치가 높다.
- `R3`는 규모는 작지만 정치적·역사적 민감도가 높은 컬렉션이다.

### 7-2. 시리즈 구성

`R1 한국전쟁`

- `S1 포로&수용소`: 90
- `S2 피난민`: 7
- `S3 학살`: 9
- `S4 일상`: 4

`R2 DMZ&판문점`

- `S1 판문점`: 18
- `S2 DMZ&MDR`: 35

`R3 일본군’위안부’`

- `S1 일본군’위안부’`: 3
- `S2 오키나와`: 4
- `S3 아시아태평양전쟁`: 2

`R4 빅 픽쳐`

- `S1 The Big Picture`: 705

### 7-3. item 메타데이터 패턴

대표 field

- `slug`
- `acquisition_transfer`
- `public_access_status`
- `level__rg`
- `level__series`
- `level__file`
- `level__file_number`
- `level__local_identifier`
- `date`
- `venues`
- `sources`
- `creators`
- `subjects`
- `tags`
- `time_courts`
- `title`
- `description_status`
- `description`
- `shotlist`
- `media_type`
- `media.embed_url`
- `components`

메모

- `description_status`는 item 요약에 가까운 짧은 설명 역할을 한다.
- `shotlist`는 장면 단위 해제이며, 번역 비용이 큰 영역이다.
- `media.embed_url`은 YouTube 기반이 많고, thumbnail도 해당 구조를 따른다.

## 8. 영문 item 번역 현재 상태

현재 반영된 것

- item 영어 파일 `882`개 생성
- title 일부 영어화
- `level__rg`, `level__series`, `venues`, `sources`, `subjects`, `tags`, `time_courts` 등 반복 메타데이터 일부 영어화
- YAML이 깨지는 영어 item 파일 5건 정리 완료

대표 반영 예시

- `부상포로 교환 (LITTLE SWAP)` → `Exchange of Sick and Wounded Prisoners (LITTLE SWAP)`
- `정전협정 조인식(선유리 유엔군임시사령부, 판문점) 2` → `Armistice Agreement Signing Ceremony (Seonyuri UNC Advance HQ, Panmunjom) 2`
- `R1 한국전쟁` → `R1 Korean War`
- `S4 일상` → `S4 Everyday Life`

아직 남은 문제

- 많은 `description_status`는 여전히 한국어 원문이다.
- `shotlist`는 대부분 한국어 원문이다.
- 일부 제목은 부분 번역만 되거나 한국어/영어가 섞여 있다.
- posts/pages와 달리 item 쪽은 “영문 경로 + 일부 메타 영문화” 수준으로 이해하는 것이 정확하다.

## 9. 국문/영문 콘텐츠 정합성 메모

좋은 점

- 국문/영문 파일 짝은 현재 빠짐없이 존재한다.
- 영어 경로(`/en/...`)는 콘텐츠 수 기준으로 구조가 열려 있다.
- 빌드 기준으로 YAML 오류와 Hugo 경고를 정리한 상태다.

주의점

- “영문 파일 존재”가 “영문 번역 완료”를 의미하지 않는다.
- 포스트 본문은 영문 파일이 있지만 국문 원문 복제 상태가 많다.
- item 본문은 메타데이터 번역이 먼저 진행되었고, 설명문/shotlist는 후속 과제다.

## 10. 실무 우선순위 제안

### 10-1. 영어 품질 우선순위

1. `about`, `posts`, `categories`의 대표 페이지 영문 본문 작성
2. `items`의 `description_status` 짧은 문장부터 영어 요약 작성
3. 중요 item에 한해 `shotlist` 영어 번역
4. taxonomy term 페이지 영어 라벨/설명 다듬기

### 10-2. archive 작업 기준 메모

- 현재 `dummy.md`는 구조 파악용으로 충분하다.
- 이후 item 번역 자동화는 `scripts/translate_items_en.py`를 보수적으로 확장하는 편이 안전하다.
- 공격적인 자동 번역보다는:
  - title
  - RG/series
  - venue/source/subject
  - description_status
  순서로 확장하는 것이 낫다.

## 11. 현재 판단 요약

- `facwa`의 핵심은 여전히 `items`다.
- `posts`는 연구성과/행사/책/사업을 보여주는 해설 레이어다.
- 국문 콘텐츠는 연구/아카이브 맥락이 충분히 살아 있다.
- 영문 콘텐츠는 “구조와 경로는 확보됨, 품질 번역은 진행 중” 상태다.
- 다음 작업에서 가장 효과가 큰 영역은 `posts`와 `description_status` 영문화다.
