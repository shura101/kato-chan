import requests
import aiohttp

def get_anime_info(title):
    url = "https://graphql.anilist.co"
    query = """
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        title {
          romaji
          english
          native
        }
        episodes
        status
        averageScore
        siteUrl
      }
    }
    """
    variables = {"search": title}
    
    response = requests.post(url, json={"query": query, "variables": variables})
    if response.status_code == 200:
        return response.json()["data"]["Media"]
    return None
    
  async def get_anime_by_genre(genre: str):
    query = '''
    query ($genre: String) {
      Page(perPage: 5) {
        media(genre_in: [$genre], type: ANIME) {
          title {
            romaji
          }
          siteUrl
        }
      }
    }
    '''
    variables = {"genre": genre.capitalize()}

    async with aiohttp.ClientSession() as session:
        async with session.post('https://graphql.anilist.co', json={"query": query, "variables": variables}) as resp:
            data = await resp.json()
            anime_list = data.get("data", {}).get("Page", {}).get("media", [])
            if not anime_list:
                return f"Tidak ditemukan anime dengan genre '{genre}'."

            hasil = f"Anime dengan genre '{genre}':\n\n"
            for anime in anime_list:
                hasil += f"- [{anime['title']['romaji']}]({anime['siteUrl']})\n"
            return hasil