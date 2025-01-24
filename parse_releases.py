import requests
from rich import print

df_app_id = 975370


def main() -> None:
    response = requests.get(f"https://api.steamcmd.net/v1/info/{df_app_id}", params={"pretty": 1})
    response.raise_for_status()
    # print(response.text)

    data = response.json()["data"][str(df_app_id)]["depots"]["branches"]
    print(data)


if __name__ == "__main__":
    main()
