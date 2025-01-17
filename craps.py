"""
File: craps.py

This module studies and plays the game of craps.
"""

from die import Die

class CrapsGame:
    """Represents a player who rolls a pair of dice and plays the Craps game."""

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        result = ""
        for (v1, v2) in self.rolls:
            result += f"Roll: ({v1}, {v2}), Sum: {v1 + v2}\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of rolls."""
        return len(self.rolls)

    def play(self):
        """Plays a game, saves the rolls for that game, and returns True for a win and False for a loss."""
        self.rolls = []  # Reset rolls for this game
        self.die1.roll()
        self.die2.roll()
        v1, v2 = self.die1.getValue(), self.die2.getValue()
        self.rolls.append((v1, v2))
        initialSum = v1 + v2

        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True

        while True:
            self.die1.roll()
            self.die2.roll()
            v1, v2 = self.die1.getValue(), self.die2.getValue()
            self.rolls.append((v1, v2))  # Track every roll
            laterSum = v1 + v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

