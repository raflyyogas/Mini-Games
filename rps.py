from random import randint
import time

choice = ["Rock", "Paper", "Scissor"]
bot = choice[randint(0,2)]

while True:
    print("\nPreparing the RPS games")
    time.sleep(2)
    player = input("Rock, Paper, Scissor: ")
    print("Wait till the result come :)")
    time.sleep(1.5)
    print("\nThe result is: ")
    time.sleep(1)
    if player == bot:
        print("Tie!")
        print("Bot choice is:",bot)
        opsi = input("\nStop or playing again? (S / P) ")
        if opsi == 'S' or opsi == 's':
            print("\aThanks for playing")
            break
    elif player == "Rock":
        if bot == "Paper":
            print("You lose!", bot, "covers", player)
            print("Bot choice is:",bot)
            opsi = input("\nStop or playing again? (S / P) ")
            if opsi == 'S' or opsi == 's':
                print("\aThanks for playing")
                break
        else:
            print("You win!", player, "smashes", bot)
            print("Bot choice is:",bot)
            opsi = input("\nStop or playing again? (S / P) ")
            if opsi == 'S' or opsi == 's':
                print("\aThanks for playing")
                break
    elif player == "Paper":
        if bot == "Scissor":
            print("You lose!", bot, "cut", player)
            print("Bot choice is:",bot)
            opsi = input("\nStop or playing again? (S / P) ")
            if opsi == 'S' or opsi == 's':
                print("\aThanks for playing")
                break
        else:
            print("You win!", player, "covers", bot)
            print("Bot choice is:",bot)
            opsi = input("\nStop or bot again? (S / P) ")
            if opsi == 'S' or opsi == 's':
                print("\aThanks for playing")
                break
    elif player == "Scissor":
        if bot == "Rock":
            print("You lose...", bot, "smashes", player)
            print("Bot choice is:",bot)
            opsi = input("\nStop or playing again? (S / P) ")
            if opsi == 'S' or opsi == 's':
                print("\aThanks for playing")
                break
        else:
            print("You win!", player, "cut", bot)
            print("Bot choice is:",bot)
            opsi = input("\nStop or playing again? (S / P) ")
            if opsi == 'S' or opsi == 's':
                print("\aThanks for playing")
                break
    else:
        print("Wrong input!")
    bot = choice[randint(0,2)]