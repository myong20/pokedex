"""src/template.html 에 data/*.json 을 넣어서 index.html(배포용)과 pokedex-artifact.html 을 만든다."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
t = (root / "src/template.html").read_text(encoding="utf-8")
for key, name in [("__DATA__", "pokemon"), ("__FORMS__", "forms"), ("__CARDS__", "cards")]:
    t = t.replace(key, (root / f"data/{name}.json").read_text(encoding="utf-8"))

(root / "pokedex-artifact.html").write_text(t, encoding="utf-8")
head = ('<!doctype html>\n<html lang="ko"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
page = t.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
(root / "public").mkdir(exist_ok=True)
(root / "public/index.html").write_text(head + page + "\n</html>\n", encoding="utf-8")
print("built public/index.html")
