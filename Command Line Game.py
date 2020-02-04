import random
import sys
import time

answer_A = ["a", "A"]
answer_B = ["b", "B"]
answer_C = ["c", "C"]
answer_Y = ["y", "yes"]
answer_N = ["n", "no"]
choices = "yes, no"


snake = 0

snakes = ['cobra', 'viper', 'king snake']


def get_snake():
    return random.choice(snakes)


def print_pause(message, delay=1):
    time.sleep(delay)
    print(message)


def restart_game():
    print("Restart Game?")
    choice = input(">>> ")
    if choice in answer_N:
        print_pause("Thanks For Playing!", 3)
        sys.exit()
    elif choice in answer_Y:
        print_pause("Starting New Game", 3)
        intro()


def validate_entry(prompt, options):
    while True:
        response = input(prompt)
        if response.lower() in options:
            return response.lower()
        print_pause(f'Sorry, I do not understand "{response}".')


def intro():
    print_pause("\n\nYou have just been knighted by King Max II.", 3)
    print_pause("The King summons you to fight for your kingdom to defend "
                "your honor.", 3)
    print_pause("You are to face the most feared arena warrior in the "
                "kingdoms history, Gareth The Great.\n", 3)
    answer = validate_entry("Will you accept the kings summon? "
                            "(Yes or No)\n", choices)
    if answer == 'yes':
        print_pause('\nKing Max II: "I knew i had chosen the bravest knight '
                    'of all kingdoms, get ready for battle."', 3)
        option_fight()
    elif answer == 'no':
        print_pause("\nKing Max II regrets knighting you and sends you to the "
                    "guillotine!", 2)
        print_pause("You DIED!", 3)
        restart_game()


def option_fight():
    print_pause("\nYou walk into the underground dungeon beneath the arena", 3)
    print_pause("An old and strange man calls for your attention.\n", 3)
    answer = validate_entry("Do you speak to the old man? (Yes or No)\n",
                            choices)
    if answer == 'yes':
        print_pause('\n"Old Man: Gareth The Great, the warrior you are about '
                    'to face has a weakness.', 3)
        print_pause('he is afraid of snakes!"', 3)
        option_prepare()
    else:
        print_pause('"kick rocks old man!"', 3)
        option_prepare()


def option_prepare():
    snakess = get_snake()
    global snake
    snake = 0
    print_pause("\nYou walk into the arena, and thousands of people stand "
                "and chant your name!", 2)
    print_pause("You see Gareth The Great standing 8ft tall, a massive "
                "human specimen", 2)
    print_pause("You see someone on the crowd with a snake", 2)
    answer = validate_entry("Do you ask for their snake? (Yes or No)\n",
                            choices)
    if answer == "yes":
        snake = 1
        print_pause("\nYou have acquired a", 2)
        print(snakess)
        print_pause("Lets start this battle!", 4)
        option_finale()
    else:
        snake = 0
        option_finale()


def option_finale():
    print_pause("\nThe battle begins, you are outmatched", 2)
    print_pause("Gareth strikes at you.", 2)
    print("\nWhat do you do next?:", )
    print("""    A. Defend yourself with your shield.
    B. Attack Gareth with your sword.
    C. Use snake against Gareth.""")
    choice = input("")
    if choice in answer_A:
        print_pause("\nGareth's strength is too great for your shield.", 2)
        print_pause("His sword slices through your shield and cuts you in "
                    "half.", 2)
        print("You DIED!")
        restart_game()
    elif choice in answer_B:
        print("\nYou attack Gareth but he defends and slices through you "
              "like butter.")
        print_pause("You DIED!", 3)
        restart_game()
    elif choice in answer_C:
        if snake > 0:
            print_pause("You throw the snake at Gareth", 2)
            print_pause("Gareth quickly gives up as he is deathly afraid "
                        "of snakes.", 2)
            print_pause("You WIN!", 3)
            restart_game()
        else:
            print("You don't have a snake to use, Gareth slices through you")
            print_pause("You DIED!", 3)
            restart_game()


intro()

