# This is a Terminal version of the program, for testing and logic purposes.
# It is not intended to be used by the user.
# It is a simple version of the program that allows the user to input the data manually.
# This should be used to test the logic of the program, and to test the output of the program.

import json

# establishing the Game class

class Game:
    def __init__(self, name, genre, rating, platform):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.platform = platform

    def __str__(self):
        return f"Name: {self.name}, Genre: {self.genre}, Rating: {self.rating}, Platform: {self.platform}"

    @staticmethod
    def to_dict(self):
        return {
            "name": self.name,
            "genre": self.genre,
            "rating": self.rating,
            "platform": self.platform
        }
    
def create_games():
    games = []
    while True:
        name = input("Enter the game name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        genre = input("Enter the game genre: ")
        ratingValid = False
        while not ratingValid:
            rating = input("Enter the game rating: ")
            try:
                rating = int(rating)
                if rating < 0 or rating > 10:
                    print("Rating must be between 0 and 10")
                else:
                    ratingValid = True
            except ValueError:
                print("Rating must be an integer betweem 0 and 10")
        platform = input("Enter the platform: ")
        game = Game(name, genre, rating, platform)
        games.append(game)
        print(f"Game '{name}' added successfully!")
    return games

def save_games(games):
    games_dict = [game.to_dict() for game in games]
    with open("games.json", "w") as file:
        json.dump(games_dict, file)
    print("Games saved successfully!")

def load_games():
    try:
        with open("games.json", "r") as file:
            games_dict = json.load(file)
            games = [Game(game["name"], game["genre"], game["rating"], game["platform"]) for game in games_dict]
            print("Games loaded successfully!")
            return games
    except FileNotFoundError:
        print("No games found!")
        return []
    except json.JSONDecodeError:
        print("Error loading games! File may be corrupted, or empty. Restarting list")
        return []

# Example usage
if __name__ == "__main__":

    games_list = load_games()

    new_games = create_games()
    games_list.extend(new_games)

    for game in games_list:
        print(game)

    save_games(games_list)