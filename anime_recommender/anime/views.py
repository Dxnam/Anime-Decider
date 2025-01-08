import sys
import os

# Add the src directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
import JIKANRUNNER


from django.shortcuts import render
import JIKANRUNNER, main
import genre_enum

def home(request):
    if request.method == "POST":
        genre = request.POST.get("genre").upper()
        genre_id = genre_enum.Genre.get_code(genre.strip())
        
        if genre_id:
            jinak_instance = JIKANRUNNER.Jinak()
            # anime_list = jinak_instance.get_anime_by_genre(genre_id)
            chosen_anime = main.anime_decision_maker_api(genre_id)
        else:
            chosen_anime = {"title": "Invalid genre entered", "image": ""}
        
        return render(request, "result.html", {"anime": chosen_anime})
    
    return render(request, "home.html")
