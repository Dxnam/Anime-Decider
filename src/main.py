import random
import asyncio
import JIKANRUNNER
import genre_enum

async def anime_decision_maker(genre_id):
    jinak_instance = JIKANRUNNER.Jinak()  # Create an instance of Jinak class
    animeInfo = await jinak_instance.search_anime_by_genre(genre_id)
    # Extract and return the title from the search results
    if animeInfo and 'data' in animeInfo:
        return animeInfo['data'][0].get('title', 'No title available')
    else:
        return 'No anime found for this genre.'

# Run the app asynchronously
if __name__ == "__main__":
    genre = input("What genre are you in the mood for? ").strip()
    genre_code = genre_enum.Genre.get_code(genre)
    
    if genre_code:
        chosen_anime = asyncio.run(anime_decision_maker(genre_code))
        print(f"Your anime recommendation: {chosen_anime}")
    else:
        print("Invalid genre entered. Please try again.")
