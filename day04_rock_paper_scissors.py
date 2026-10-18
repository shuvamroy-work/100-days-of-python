"""
Day 04: Rock Paper Scissors Game
Topic: Lists, Indexing & the random Module
Author: [Shuvam Roy]
"""

 
import random
 
# A list stores multiple items in one variable.
# Index positions: 0 = Rock, 1 = Paper, 2 = Scissors
CHOICES = ["Rock", "Paper", "Scissors"]
 
 
def get_result(player: int, computer: int) -> str:
    """Return 'win', 'lose' or 'draw' from the player's point of view."""
    # Same index on both sides means the round is a draw
    if player == computer:
        return "draw"
 
    # Winning combinations: Rock beats Scissors, Paper beats Rock,
    # Scissors beats Paper (written using their index numbers)
    elif (
        (player == 0 and computer == 2)
        or (player == 1 and computer == 0)
        or (player == 2 and computer == 1)
    ):
        return "win"
 
    # Every other combination is a loss
    else:
        return "lose"
 
 
def main():
    print("=" * 40)
    print("      ROCK PAPER SCISSORS GAME")
    print("=" * 40)
 
    try:
        # Take the player's choice as an index number
        player = int(
            input("Type 0 for Rock, 1 for Paper or 2 for Scissors: ").strip()
        )
 
        # Validate: the index must exist in the list (0, 1 or 2)
        if player < 0 or player >= len(CHOICES):
            print("Invalid number! Please choose 0, 1 or 2.")
            return
 
        # Computer picks a random valid index from the list
        computer = random.randint(0, len(CHOICES) - 1)
 
        # Use indexing to convert numbers back into readable names
        print(f"\nYou chose     : {CHOICES[player]}")
        print(f"Computer chose: {CHOICES[computer]}\n")
 
        result = get_result(player, computer)
 
        if result == "win":
            print("You win! 🎉")
        elif result == "lose":
            print("You lose! 😢")
        else:
            print("It's a draw! 🤝")
 
    except ValueError:
        # Runs if the user types text instead of a number
        print("Please enter a valid number (0, 1 or 2).")
 
 
if __name__ == "__main__":
    main()
 