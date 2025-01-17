import tkinter as tk
from tkinter import PhotoImage
from craps import CrapsGame  # Importing the CrapsGame class


class CrapsGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Craps Game")
        self.root.geometry("600x600")

        # Load dice images
        self.dice_images = {
            1: PhotoImage(file="images/1.gif"),
            2: PhotoImage(file="images/2.gif"),
            3: PhotoImage(file="images/3.gif"),
            4: PhotoImage(file="images/4.gif"),
            5: PhotoImage(file="images/5.gif"),
            6: PhotoImage(file="images/6.gif")
        }

        # UI components
        self.header = tk.Label(root, text="Craps Game", font=("Arial", 20))
        self.header.pack(pady=10)

        self.dice_frame = tk.Frame(root)
        self.dice_frame.pack(pady=10)

        self.play_one_button = tk.Button(root, text="Play One Game", command=self.play_one_game)
        self.play_one_button.pack(pady=5)

        # Label and Entry for number of games
        self.num_games_label = tk.Label(root, text="Enter number of games to play:")
        self.num_games_label.pack(pady=5)

        self.num_games_entry = tk.Entry(root)
        self.num_games_entry.pack(pady=5)

        self.play_many_button = tk.Button(root, text="Play Many Games", command=self.play_many_games)
        self.play_many_button.pack(pady=5)

        self.stats_label = tk.Label(root, text="", font=("Arial", 12))
        self.stats_label.pack(pady=10)

    def play_one_game(self):
        """Plays a single game and updates the result display."""
        game = CrapsGame()  # Using CrapsGame class
        youWin = game.play()
        self.display_dice(game)  # Display only two dice
        if youWin:
            self.stats_label.config(text="You win!")
        else:
            self.stats_label.config(text="You lose!")

    def play_many_games(self):
        """Plays a number of games based on user input and updates the stats."""
        try:
            number = int(self.num_games_entry.get())  # Get user input for number of games
            if number <= 0:
                self.stats_label.config(text="Please enter a positive number.")
                return
        except ValueError:
            self.stats_label.config(text="Invalid input. Please enter a number.")
            return

        wins = 0
        losses = 0
        win_rolls = 0
        loss_rolls = 0
        game = CrapsGame()  # Using CrapsGame class

        for _ in range(number):
            has_won = game.play()
            rolls = game.getNumberOfRolls()
            if has_won:
                wins += 1
                win_rolls += rolls
            else:
                losses += 1
                loss_rolls += rolls

        avg_win_rolls = win_rolls / wins if wins else 0
        avg_loss_rolls = loss_rolls / losses if losses else 0

        stats = f"Games Played: {number}\n"
        stats += f"Wins: {wins}, Losses: {losses}\n"
        stats += f"Avg Rolls per Win: {avg_win_rolls:.2f}\n"
        stats += f"Avg Rolls per Loss: {avg_loss_rolls:.2f}\n"

        self.stats_label.config(text=stats)

    def display_dice(self, game):
        """Displays only two dice images based on the first roll of the game."""
        for widget in self.dice_frame.winfo_children():
            widget.destroy()  # Remove previous dice images

        # Only display the first roll (two dice)
        die1_value, die2_value = game.rolls[0]  # Only take the first roll
        die1_image = tk.Label(self.dice_frame, image=self.dice_images[die1_value])
        die2_image = tk.Label(self.dice_frame, image=self.dice_images[die2_value])
        die1_image.pack(side=tk.LEFT, padx=10)
        die2_image.pack(side=tk.LEFT, padx=10)
