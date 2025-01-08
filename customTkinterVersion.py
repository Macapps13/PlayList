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

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("PlayList")
        font = ctk.CTkFont(family="Helvetica", size=15)

        self.button = ctk.CTkButton(self, text="Add Game", command=self.add_game, font=font)
        self.button.grid(row=0, column=0, padx=20, pady=20)

    def add_game(self):
        print("add game")


app = App()
app.mainloop()