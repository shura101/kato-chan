import requests

def get_waifu_image(nsfw=True):
    endpoint = "https://api.waifu.pics/nsfw/waifu" if nsfw else "https://api.waifu.pics/sfw/waifu"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json().get("url")
    return None