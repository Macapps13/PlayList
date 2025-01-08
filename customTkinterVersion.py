# This version serves as a basis for GUI design, utilising earlier python logic

import customtkinter as ctk
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

    def to_dict(self):
        return {
            "name": self.name,
            "genre": self.genre,
            "rating": self.rating,
            "platform": self.platform
        }

app = ctk.CTk()
app.geometry("600x400")
app.title("PlayList")

app.mainloop()