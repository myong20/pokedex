# 포켓몬 도감

1025마리 포켓몬과 메가진화·거다이맥스·리전폼, 포켓몬 카드 목록을 한글로 찾아보는 정적 웹페이지예요.

## 구조
- `src/template.html` — 화면(HTML·CSS·JS)
- `data/pokemon.json`, `data/forms.json` — 포켓몬·모습 데이터 (PokeAPI 데이터 기반)
- `data/cards.json` — 영어판 카드 목록 (pokemon-tcg-data 기반)
- `scripts/build.py` — 위 파일을 합쳐 `public/index.html` 을 만듦

## 로컬에서 보기
```bash
python3 scripts/build.py
```
그다음 `public/index.html` 을 브라우저로 열면 돼요.

## 배포
`main` 에 합쳐지면 GitHub Actions(`.github/workflows/deploy.yml`)가 Vercel 에 배포해요.
PR 을 열면 미리보기 주소로 배포돼요. 저장소 Settings → Secrets and variables → Actions 에 아래 3개가 있어야 해요.

| 이름 | 값 |
|---|---|
| `VERCEL_TOKEN` | Vercel 계정 설정 → Tokens 에서 만든 토큰 |
| `VERCEL_ORG_ID` | 프로젝트의 `.vercel/project.json` 의 `orgId` |
| `VERCEL_PROJECT_ID` | 같은 파일의 `projectId` |
