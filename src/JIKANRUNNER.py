from jikan4snek import Jikan4SNEK

class Jinak():
    def __init__(self):
        self.base_url = "https://api.jikan.moe/v4/anime"

    # Synchronous method to fetch anime by genre and save to a file
    def get_anime_by_genre(self, genre_id, filename="anime_data.json"):
        url = f"{self.base_url}?genres={genre_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            animes = [
                {"title": anime['title'], "episodes": anime['episodes'], "score": anime['score']}
                for anime in data['data']
            ]

            # # Write the response to a file
            # with open(filename, 'w') as file:
            #     json.dump(animes, file, indent=4)

            print(f"Data saved to {filename}")
            return animes
        else:
            print(f"Error: {response.status_code}")
            return []

    # Asynchronous method to fetch anime by genre
    async def search_anime_by_genre(self, genre_id):
        # Perform the search for anime by genre
        anime_search = await self.jikan.search('anime', genre=genre_id)
        return anime_search
