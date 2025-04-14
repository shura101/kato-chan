import requests

def get_waifu_image(mode: str = "sfw"):
    url = f"https://api.waifu.pics/sfw/{mode}"  # Contoh API untuk waifu
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("url")
    return None