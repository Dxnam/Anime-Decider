from jikan4snek import Jikan4SNEK

class Jinak():
    def __init__(self):
        self.jikan = Jikan4SNEK()  # Initialize Jikan4SNEK instance

    async def getAnimeInfo(self, id):
        try:
            # Asynchronously fetch anime details
            anime = await self.jikan.get(id).anime()  # Correct method based on the documentation
            anime = anime['data']
            animeInfo = {
                "title": anime['title'],
                "synopsis": anime['synopsis'],
                "score": anime['score'],
                "url": anime['url']
            }
            return animeInfo
        except Exception as e:
            # Handle potential errors
            return f"An error occurred: {str(e)}"
        
    async def search_anime_by_genre(self, genre_id):
        # Perform the search for anime by genre
        anime_search = await self.jikan.search('anime', genre=genre_id)
        return anime_search
