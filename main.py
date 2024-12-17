import json
from pathlib import Path
from typing import Any
import requests
import re

# Docs: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetNewsForApp_(v0002)
news_request_url = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/"
df_app_id = 975370

root_dir = Path(__file__).parent
output_file = root_dir / "last_update.json"


def get_last_posts(*, count) -> list[dict[str, Any]]:
    response = requests.get(
        news_request_url,
        params=dict(appid=df_app_id, count=count, maxlength=100, format="json"),
    )
    response.raise_for_status()
    return response.json()["appnews"]["newsitems"]


def is_update(title: str) -> bool:
    """
    If title contains version number or "beta N", return True
    """
    return re.search(r"\d{2}\.\d{2,}|beta\s*\d+", title, re.IGNORECASE)


def main():
    posts = get_last_posts(count=1)
    post = posts[0]

    if output_file.exists():
        prev_update = json.loads(output_file.read_text(encoding="utf-8"))

    if is_update(post["title"]) and (not output_file.exists() or prev_update["date"] < post["date"]):
        Path(output_file).write_text(json.dumps(post), encoding="utf-8")
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
