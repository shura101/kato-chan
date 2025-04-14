import requests

def get_waifu_image(mode: str = "sfw"):
    """Mengambil gambar waifu berdasarkan mode (SFW atau NSFW)."""
    url = f"https://nekos.life/api/v2/img/{mode}/waifu"  # URL untuk nekos.life API
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("url")  # Mengambil URL gambar dari response
    return None