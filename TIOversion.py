# This is a Terminal version of the program, for testing and logic purposes.
# It is not intended to be used by the user.
# It is a simple version of the program that allows the user to input the data manually.
# This should be used to test the logic of the program, and to test the output of the program.


# establishing the Game class

class Game:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"Name: {self.name}, Genre: {self.genre}, Rating: {self.rating}"
    
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
        game = Game(name, genre, rating)
        games.append(game)
        print(f"Game '{name}' added successfully!")
    return games

# Example usage
if __name__ == "__main__":
    games_list = create_games()
    for game in games_list:
        print(game)