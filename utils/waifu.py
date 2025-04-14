import requests
import aiohttp

async def fetch_random_waifu():
    url = "https://api.waifu.pics/sfw/waifu"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data["url"]
            else:
                return "https://media.tenor.com/f0uvs96FfXsAAAAd/waifu-anime.gif"  # fallback image

def get_waifu_image(nsfw=True):
    endpoint = "https://api.waifu.pics/nsfw/waifu" if nsfw else "https://api.waifu.pics/sfw/waifu"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json().get("url")
    return None