# Jhunjhunu Blog website

Jhunjhunu Ki Kahani, Jhunjhunu Ke Logon Ki Zubaani.

Static bilingual site (Hindi default, English), served by GitHub Pages from `docs/`.

- Edit content in `build.py` (the `COPY` and `INFO` blocks); styles and images live in `static/`.
- Rebuild: `python3 build.py https://vipinjanu77-max.github.io/jhunjhunu-blog/` (pass the custom domain, e.g. `https://jhunjhunublog.in/`, once connected). The output goes to `docs/`.
- Commit and push; Pages redeploys in about a minute.

No dependencies beyond Python 3.
