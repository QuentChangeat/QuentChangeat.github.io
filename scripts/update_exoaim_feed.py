#!/usr/bin/env python3
"""Refresh _data/exoaim.json from the ExoAIM Lab RSS feeds.

Reads the news and publication feeds of exoaim.com, merges them, keeps the
newest items and writes them to _data/exoaim.json, which the home page shows
under "Latest from the lab". Standard library only.

Run locally with:  python3 scripts/update_exoaim_feed.py
"""
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

FEEDS = [
    ("News", "https://exoaim.com/post/index.xml"),
    ("Paper", "https://exoaim.com/publication/index.xml"),
]
KEEP = 6  # items stored; the home page shows the first 3
OUT = Path(__file__).resolve().parent.parent / "_data" / "exoaim.json"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "quentchangeat.github.io feed updater"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def clean(text):
    text = re.sub(r"<[^>]+>", "", text or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def parse(kind, xml_bytes):
    items = []
    for node in ET.fromstring(xml_bytes).iter("item"):
        title = clean(node.findtext("title"))
        link = (node.findtext("link") or "").strip()
        raw_date = node.findtext("pubDate")
        if not (title and link and raw_date):
            continue
        published = parsedate_to_datetime(raw_date).astimezone(timezone.utc)
        items.append({"kind": kind, "title": title, "url": link, "date": published.date().isoformat()})
    return items


def main():
    items = []
    for kind, url in FEEDS:
        try:
            items += parse(kind, fetch(url))
        except Exception as exc:  # leave the current file untouched on any failure
            print(f"Could not read {url}: {exc}", file=sys.stderr)
            return 1
    if not items:
        print("Feeds returned no items; keeping the current file.", file=sys.stderr)
        return 1

    items.sort(key=lambda it: it["date"], reverse=True)
    items = items[:KEEP]

    old = json.loads(OUT.read_text()) if OUT.exists() else {}
    if old.get("items") == items:
        print("No new items.")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"updated": date.today().isoformat(), "items": items}, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(items)} items to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
