from typing import Any
import requests
from datetime import datetime

# Docs: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetNewsForApp_(v0002)
news_request_url = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/"
df_app_id = 975370


def get_last_posts() -> list[dict[str, Any]]:
    response = requests.get(news_request_url, params=dict(appid=df_app_id, count=1, maxlength=1000, format="json"))
    response.raise_for_status()
    return response.json()["appnews"]["newsitems"]


def main():
    posts = get_last_posts()
    for post in posts:
        print(post["title"])
        date = datetime.fromtimestamp(post["date"])
        print(date.isoformat())
        print(post["contents"])
        print(post["url"])
        print(post["author"])
        print()


if __name__ == "__main__":
    main()
