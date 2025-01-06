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
    
game1 = Game("The Witcher 3", "RPG", 10)

print(game1)