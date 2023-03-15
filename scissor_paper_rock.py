import random

while True:
    print(
        "\n\n----------------------------------------------------------------------------"
    )

    options = ["scissor", "paper", "rock"]
    s = options[0]
    p = options[1]
    r = options[2]

    print(
        """
    1 = s = scissor
    2 = p = paper
    3 = r = rock
    """
    )

    user = input("Your turn -->")
    computer = random.choice(options)

    # print("-----------------------------------------------------------------------------\n")

    if user == "s" or user == "1":
        user_choice = options[0]
    elif user == "p" or user == "2":
        user_choice = options[1]
    elif user == "r" or user == "3":
        user_choice = options[2]
    else:
        break

    if user_choice == computer:
        result = "Draw"
    elif user_choice == options[0]:
        if computer == options[1]:
            result = "You won"
        else:
            result = "You lose"
    elif user_choice == options[1]:
        if computer == options[2]:
            result = "You won"
        else:
            result = "You lose"
    elif user_choice == options[2]:
        if computer == options[0]:
            result = "You won"
        else:
            result = "You lose"

    print("You = ", user_choice)
    print("Computer = ", computer)
    print(result)
