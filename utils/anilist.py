import requests

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