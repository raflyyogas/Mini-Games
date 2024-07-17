import random
import time

def get_bot_choice():
    choice = ["Rock", "Paper", "Scissors"]
    return random.choice(choice)

def get_result(player, bot):
    if player == bot:
        return "Tie"
    elif (player == "Rock" and bot == "Scissors") or (player == "Paper" and bot == "Rock") or (player == "Scissors" and bot == "Paper"):
        return "Win"
    else:
        return "Lose"

def display_result(player, bot, result):
    if result == "Tie":
        return f"Both chose {player}. It's a tie!"
    elif result == "Win":
        if player == "Rock":
            return f"Rock smashes Scissors. You win!"
        elif player == "Paper":
            return f"Paper covers Rock. You win!"
        elif player == "Scissors":
            return f"Scissors cut Paper. You win!"
    else:
        if bot == "Rock":
            return f"Rock smashes Scissors. You lose!"
        elif bot == "Paper":
            return f"Paper covers Rock. You lose!"
        elif bot == "Scissors":
            return f"Scissors cut Paper. You lose!"

def main():
    score = {"Player": 0, "Bot": 0}
    
    while True:
        print("\nPreparing the Rock, Paper, Scissors game")
        time.sleep(2)
        
        player = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if player not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice, please choose Rock, Paper, or Scissors.")
            continue
        
        print("Wait till the result comes :)")
        time.sleep(1.5)
        
        bot = get_bot_choice()
        result = get_result(player, bot)
        
        print("\nThe result is: ")
        time.sleep(1)
        
        print(display_result(player, bot, result))
        print(f"Bot chose: {bot}")
        
        if result == "Win":
            score["Player"] += 1
        elif result == "Lose":
            score["Bot"] += 1
        
        print(f"\nScore -> Player: {score['Player']} | Bot: {score['Bot']}")
        
        opsi = input("\nStop or play again? (S / P): ").lower()
        if opsi == 's':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
