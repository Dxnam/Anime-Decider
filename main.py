import random

def anime_decision_maker():
    print("Welcome to the Automated Decision-Making App!")
    print("Enter 'go' to get a random anime suggestion, or 'quit' to exit.")
    
    # Predefined list of animes
    anime_list = [
        "Attack on Titan",
        "Naruto",
        "My Hero Academia",
        "One Piece",
        "Demon Slayer",
        "Jujutsu Kaisen"
    ]
    
    while True:
        user_input = input("\nYour choice (go/quit): ").strip().lower()
        
        if user_input == 'go':
            # Randomly select an anime
            selected_anime = random.choice(anime_list)
            print(f"🎥 Watch this: {selected_anime}")
        elif user_input == 'quit':
            print("Goodbye! Enjoy your anime time!")
            break
        else:
            print("Invalid input. Please enter 'go' or 'quit'.")

# Run the app
if __name__ == "__main__":
    anime_decision_maker()
