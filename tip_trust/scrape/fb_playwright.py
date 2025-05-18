# tip_trust/scrape/fb_playwright.py
"""
Simple Facebook scraper (Playwright version).
Run with:  poetry run python -m tip_trust.scrape.fb_playwright --dry
"""

import playwright.sync_api as pw        # ← new header import
import argparse
from pathlib import Path

def run_scraper(dry: bool = False):
    if dry:
        print("DRY-RUN: no browser launched")
        return

    with pw.sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # … scrape logic here …
        browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", action="store_true", help="skip browser launch")
    args = parser.parse_args()
    run_scraper(dry=args.dry)