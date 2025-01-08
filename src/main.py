import random
import asyncio
import JIKANRUNNER
import genre_enum


# Asynchronous decision maker (optional usage)
async def anime_decision_maker(genre_id):
    jinak_instance = JIKANRUNNER.Jinak()  # Create an instance of Jinak class
    anime_info = await jinak_instance.search_anime_by_genre(genre_id)
    if anime_info and 'data' in anime_info:
        return anime_info['data'][0].get('title', 'No title available')
    else:
        return "No anime found for this genre."


# Synchronous decision maker (default usage)
def anime_decision_maker_api(genre_id):
    jinak_instance = JIKANRUNNER.Jinak()  # Create an instance of Jinak class
    anime_list = jinak_instance.get_anime_by_genre(genre_id)
    if anime_list:
        return random.choice(anime_list)
    else:
        return {"title": "No anime found for this genre."}


# Main application logic
if __name__ == "__main__":
    genre = input("What genre are you in the mood for? ").strip()
    genre_code = genre_enum.Genre.get_code(genre)

    if genre_code:
        # Use the synchronous method to fetch and recommend an anime
        chosen_anime = anime_decision_maker_api(genre_code)
        print(f"Your anime recommendation: {chosen_anime['title']}")
        print(f"Anime rating: {chosen_anime['score']}")
        print(f"Number of episodes: {chosen_anime['episodes']}")
    else:
        print("Invalid genre entered. Please try again.")