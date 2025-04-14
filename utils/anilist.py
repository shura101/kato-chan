import requests
import aiohttp

async def get_anime_info(title: str):
    query = '''
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        title {
          romaji
          english
          native
        }
        episodes
        status
        description(asHtml: false)
        coverImage {
          large
        }
        siteUrl
      }
    }
    '''
    variables = {"search": title}

    async with aiohttp.ClientSession() as session:
        async with session.post('https://graphql.anilist.co', json={"query": query, "variables": variables}) as resp:
            data = await resp.json()
            anime = data.get("data", {}).get("Media", None)
            if not anime:
                return "Anime tidak ditemukan."

            info = f"**{anime['title']['romaji']}**\n"
            info += f"Episodes: {anime.get('episodes', 'N/A')}\n"
            info += f"Status: {anime.get('status', 'N/A')}\n"
            info += f"\n{anime.get('description', 'Tidak ada deskripsi')[:500]}...\n"
            info += f"[Link Anilist]({anime['siteUrl']})"
            return info, anime['coverImage']['large']

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