# quentchangeat.github.io

Personal site of Quentin Changeat. It is deliberately small: the research group,
team, publications and vacancies live at **[exoaim.com](https://exoaim.com)**, and
this site points there.

Built by GitHub Pages with plain Jekyll; no theme, no JavaScript, fonts self-hosted.

## What to edit

| To change | Edit |
| --- | --- |
| Bio, headline | `index.html` |
| Email, CV link, footer links (Scholar, ORCID…) | `_config.yml` |
| CV | replace `img/cv_quentin_changeat.pdf` |
| Teaching / datasets pages | `teaching.md`, `datasets.md` |
| Colours, fonts, spacing | `assets/css/site.css` |
| Photo / social-share card | `assets/img/portrait.jpg`, `assets/img/og-image.png` (1200×630) |

## "Latest from the lab" updates itself

`.github/workflows/update-exoaim.yml` runs every Monday (or on demand from the
**Actions** tab → *Update latest ExoAIM items* → *Run workflow*). It runs
`scripts/update_exoaim_feed.py`, which reads the exoaim.com news and publication
RSS feeds and rewrites `_data/exoaim.json` only when something is new.
The home page shows the three newest items.

Notes:
- To run it by hand only, delete the `schedule:` lines in the workflow.
- GitHub pauses scheduled workflows after 60 days without activity in the
  repository; re-enable it from the Actions tab if that happens.
- Repository *Settings → Actions → General → Workflow permissions* must allow
  "Read and write" so the job can commit.

## Old URLs

`/publications` and `/projects` redirect to the matching pages on exoaim.com.
Dataset downloads and the CV keep their old `/img/...` paths so existing links work.

## Preview locally

```sh
bundle install
bundle exec jekyll serve   # http://localhost:4000
```
