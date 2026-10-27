# facwa.kr

> **Repo 변경**: `https://github.com/team-durumi/facwa` → **`https://github.com/text-consulting-group/facwa`**

## front
- facwa.kr
- (last) hugo v0.165.0+extended+withdeploy darwin/arm64 BuildDate=2026-08-12T14:26:28Z VendorInfo=Homebrew
- 261027 / hugo v0.165.0+extended+withdeploy darwin/arm64


## 성과정리 콘텐츠

- https://docs.google.com/spreadsheets/d/1LoJ5-cXCgUkguG_dCn9Lt4qL1-NmpXV64RRQARHHhI0/edit?pli=1#gid=1370010693


## 데이터 확인 2026-10-27

총 875 items (국문 기준)

- R1 한국전쟁 : 113 items
  - S1 포로&수용소 : 95 items
  - S2 피난민 : 6 items
  - S3 학살 : 8 items
  - S4 일상 : 4 items

- R2 DMZ&판문점 : 52 items
  - S1 판문점 : 18 items
  - S2 DMZ&MDR : 34 items

- R3 일본군 '위안부' : 6 items
  - S1 일본군 '위안부' : 2 items
  - S2 오키나와 : 3 items
  - S3 아시아태평양전쟁 : 1 item

- R4 빅 픽쳐 : 704 items
  - S1 The Big Picture : 704 items

## TCG
- netlify 오류는 https://github.com/team-durumi/facwa/commit/d1e835648722dd48315f9cee1dc3e3dad1055a07
- search catalog ENV 값에 build 값이 포함되어 있음.
- opengraph 설정을 위해서 page의 개별 param값으로 사용하면 안 되는 항목(audio, video)
- npm install issue

## 실서버 배포(pages)
- 직접배포
    - hugo --minify && npx wrangler pages deploy --project-name facwa --branch main
    - 도메인 복구: Cloudflare Pages 프로젝트 `facwa`에 `facwa.kr`을 다시 연결 후 DNS(CNAME)가 SSL 발급 상태인지 확인
