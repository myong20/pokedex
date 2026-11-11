# 포켓몬 도감

1025마리 포켓몬과 메가진화·거다이맥스·리전폼, 한국어판 포켓몬 카드를 한글로 찾아보는 정적 웹페이지예요.

## 구조
- `src/template.html` — 화면(HTML·CSS·JS)
- `data/pokemon.json`, `data/forms.json` — 포켓몬·모습 데이터 (PokeAPI 데이터 기반)
- `scripts/build.py` — 위 파일을 합쳐 `public/index.html` 을 만듦

## 로컬에서 보기
```bash
python3 scripts/build.py
```
그다음 `public/index.html` 을 브라우저로 열면 돼요.

## 배포
`main` 에 합쳐지면 GitHub Actions(`.github/workflows/deploy.yml`)가 Vercel 에 배포해요.
PR 을 열면 미리보기 주소로 배포돼요.

저장소 Settings → Secrets and variables → Actions 에 `VERCEL_TOKEN`(Vercel 계정 설정 → Tokens 에서 만든 토큰) 하나만 있으면 돼요.
