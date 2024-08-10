

        #ROCK , PAPER , SCISSORS GAME

import random
def guessing_game():

    print("\nWELCOME TO THE ROCK,PAPER,SCISSORS GAME!")
    print("CHOICES: ROCK ,PAPER ,SCISSORS\n")

    items=["paper", "rock", "scissor"]

    rand=random.choice(items)
    attempts=0
    while True:
        user_choice=input("ENTER YOUR CHOICE: ").lower()
        if user_choice=="exit":
            print("GAME ENDED:")
            break

        elif user_choice==rand:
            print("congratulations you won :")
            print(f"YOU WON THE GAME BY GUESSING THE CORRRECT OUTPUT {user_choice} and in {attempts+1} attempts\n") 
            play_again = input("If you want to play again, enter 'yes', else type 'exit' to quit: ").lower()

            if play_again != 'yes':
                print("THANKS FOR PLAYING!")
            else:
                guessing_game()


        else:
            print("Try Again")

            attempts=attempts+1




guessing_game()            
