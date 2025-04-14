import requests

def get_waifu_image(mode="sfw", category="waifu"):
    url = f"https://api.waifu.pics/{mode}/{category}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("url")
    else:
        return None