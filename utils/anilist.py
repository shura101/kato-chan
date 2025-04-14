import requests

def search_anime(query: str):
    url = "https://graphql.anilist.co"
    headers = {"Content-Type": "application/json"}
    payload = {
        "query": """
        query ($search: String) {
          Media(search: $search, type: ANIME) {
            title {
              romaji
            }
            episodes
            averageScore
            description(asHtml: false)
            siteUrl
          }
        }
        """,
        "variables": {"search": query}
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json().get("data", {}).get("Media", {})
        return {
            "title": data.get("title", {}).get("romaji", "Tidak diketahui"),
            "episodes": data.get("episodes", "???"),
            "score": data.get("averageScore", "???"),
            "description": data.get("description", "Deskripsi tidak tersedia."),
            "url": data.get("siteUrl", "")
        }
    else:
        return None