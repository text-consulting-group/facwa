# facwa.kr

## front
- facwa.kr
- (last)hugo v0.143.1+extended+withdeploy darwin/arm64 BuildDate=2025-02-04T08:57:38Z VendorInfo=brew
- 260422 / hugo v0.160.1+extended+withdeploy darwin/arm64


## search-catalog
- https://catalog.facwa.kr/

## decap-cms
- https://decapcms.org/docs/intro/
- netlify identify / 두루미 계정
- git gateway enable
- invited user only
- 접근주소 : https://facwa.kr/admin

## 성과정리 콘텐츠

- https://docs.google.com/spreadsheets/d/1LoJ5-cXCgUkguG_dCn9Lt4qL1-NmpXV64RRQARHHhI0/edit?pli=1#gid=1370010693


## 데이터 확인 2023-06-01

엑셀 slug : 904 / 공개 889 / 비공개 15

- R1 한국전쟁 : 124 items 공개 (128 items)
  - S1 포로, 수용소 : 102 items
  - S2 피난민 : 6 items
  - S3 학살 : 8 items
  - S4 일상 : 8 items

- R2 R2 DMZ&판문점 : 55 items (66 items)
  - S1 판문점 : 17 items
  - S2 DMZ&MDR : 38 items

- R3 R3 일본군 '위안부' : 6 items (slug 181- 186)
  - S1 일본군 ‘위안부’ - 2
  - S2 오키나와 - 3
  - S3 아시아태평양전쟁 - 1

- R4 빅픽처 : 704 items (slug 201-904 )

## Production 관련
- netlify 오류는 https://github.com/team-durumi/facwa/commit/d1e835648722dd48315f9cee1dc3e3dad1055a07
- search catalog ENV 값에 build 값이 포함되어 있음.
- opengraph 설정을 위해서 page의 개별 param값으로 사용하면 안 되는 항목(audio, video)
- npm install issue

## 2026-04-22 로고 수정 전 업데이트
### 1. 꼬인 모듈과 캐시 정리
hugo mod clean
hugo cache clean

### 2. 서버 실행 / 휴고 버전 업
hugo server --ignoreCache --disableFastRender
hugo v0.160.1+extended+withdeploy darwin/arm64

### 3.날짜
날짜 관련 오류 886개 수정
날짜 관련 형식은 하나로 지정되어 있지 않고, 범위를 나타내거나 특정일을 나타내는데, 모든 형식이 달라서 전체 수정(빌드오류)

### 4.로고 수정 요청
관련메 메인 텍스트 메뉴 전체 수정
공지사항 관련 메뉴 삭제 (연구소로 이동)

### 5.production 관련 수정
깃허브 연결

## 실서버 배포(pages)
- 직접배포
    - hugo --minify && npx wrangler pages deploy --project-name facwa --branch main
    - 도메인 복구: Cloudflare Pages 프로젝트 `facwa`에 `facwa.kr`을 다시 연결 후 DNS(CNAME)가 SSL 발급 상태인지 확인
