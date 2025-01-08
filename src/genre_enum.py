from enum import Enum

class Genre(Enum):
    ACTION = 1
    ADVENTURE = 2
    CARS = 3
    COMEDY = 4
    DEMONS = 5
    DRAMA = 6
    FANTASY = 7
    GAME = 8
    HAREM = 9
    HISTORICAL = 10
    HORROR = 11
    JOSEI = 12
    KIDS = 13
    MAGIC = 14
    MAHOU_SHOUJO = 15
    MECHA = 16
    MILITARY = 17
    MUSIC = 18
    MYSTERY = 19
    PARODY = 20
    POLICE = 21
    PSYCHOLOGICAL = 22
    ROMANCE = 23
    SAMURAI = 24
    SCHOOL = 25
    SCI_FI = 26
    SHOUJO = 27
    SHOUNEN = 28
    SLICE_OF_LIFE = 29
    SPACE = 30
    SPORTS = 31
    SUPER_POWER = 32
    SUPERNATURAL = 33
    THRILLER = 34
    VAMPIRE = 35
    YAOI = 36
    YURI = 37

    @classmethod
    def get_code(cls, genre_name):
        try:
            return cls[genre_name].value
        except KeyError:
            return None  # In case the genre does not exist

# Example usage
genre_code = Genre.get_code("ACTION")
print(f"The code for ACTION genre is: {genre_code}")