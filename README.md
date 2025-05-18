<!-----  QUICK START  --->
## Quick Start

```bash
poetry install                                # create the virtual-env & install deps
poetry run playwright install chromium        # one-time download of the browser
poetry run python -m tip_trust.scrape.fb_playwright --help