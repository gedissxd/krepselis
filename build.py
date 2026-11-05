"""Build the standalone index.html (served by GitHub Pages) from src/app.html."""
from pathlib import Path

root = Path(__file__).parent
s = (root / "src" / "app.html").read_text(encoding="utf8")
head_end = s.index("</style>") + len("</style>")
head, body = s[:head_end], s[head_end:]
page = (
    '<!doctype html>\n<html lang="lt">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="7 dienų mitybos planas pagal jūsų poreikius, su receptais, '
    'gaminimu 2 kartus per savaitę ir pirkinių sąrašu Maximos ir Rimi kainomis.">\n'
    "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}"
    "[hidden]{display:none!important}</style>\n"
    + head + "\n</head>\n<body>" + body + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(page, encoding="utf8")
print("built index.html")
