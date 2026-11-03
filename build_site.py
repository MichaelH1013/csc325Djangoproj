"""Save the app's responses as files in _site so GitHub Pages can publish them."""
import os
from pathlib import Path

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csc325Djangoproj.settings")
django.setup()

from django.test import Client

PAGES = {
    "/": "index.html",
    "/about/": "about/index.html",
    "/api/status/": "api/status.json",
}


def main():
    client = Client(HTTP_HOST="localhost", HTTP_ACCEPT="application/json")
    for url, filename in PAGES.items():
        response = client.get(url)
        if response.status_code != 200:
            raise SystemExit(f"{url} returned {response.status_code}")
        output = Path("_site") / filename
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(response.content)
        print(f"{url} -> {output}")


if __name__ == "__main__":
    main()
