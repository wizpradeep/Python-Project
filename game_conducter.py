# Try it , It help in conducting indoor games like: Cards, etc efficiently..


def game():
    while True:
        player_number = int(input("\n\nEnter number of players (2-5)..\n-->"))
        if player_number >= 2 and player_number <= 5:
            break
        else:
            continue

    while True:
        name = input("Do you want to name players?\n(y/n)-->").lower()
        if name:
            break
        else:
            continue

    if name == "y":
        if player_number == 2:
            while True:
                Player_01 = input("Enter name of player_01:").title()
                if Player_01:
                    break
                else:
                    continue
            while True:
                Player_02 = input("Enter name of player_02:").title()
                if Player_02:
                    break
                else:
                    continue
        elif player_number == 3:
            while True:
                Player_01 = input("Enter name of player_01:").title()
                if Player_01:
                    break
                else:
                    continue
            while True:
                Player_02 = input("Enter name of player_02:").title()
                if Player_02:
                    break
                else:
                    continue
            while True:
                Player_03 = input("Enter name of player_03:").title()
                if Player_03:
                    break
                else:
                    continue

        elif player_number == 4:
            while True:
                Player_01 = input("Enter name of player_01:").title()
                if Player_01:
                    break
                else:
                    continue
            while True:
                Player_02 = input("Enter name of player_02:").title()
                if Player_02:
                    break
                else:
                    continue
            while True:
                Player_03 = input("Enter name of player_03:").title()
                if Player_03:
                    break
                else:
                    continue
            while True:
                Player_04 = input("Enter name of player_04:").title()
                if Player_04:
                    break
                else:
                    continue

        elif player_number == 5:
            while True:
                Player_01 = input("Enter name of player_01:").title()
                if Player_01:
                    break
                else:
                    continue
            while True:
                Player_02 = input("Enter name of player_02:").title()
                if Player_02:
                    break
                else:
                    continue
            while True:
                Player_03 = input("Enter name of player_03:").title()
                if Player_03:
                    break
                else:
                    continue
            while True:
                Player_04 = input("Enter name of player_04:").title()
                if Player_04:
                    break
                else:
                    continue
            while True:
                Player_05 = input("Enter name of player_05:").title()
                if Player_05:
                    break
                else:
                    continue

        else:
            Player_01 = "Player_01"
            Player_02 = "Player_02"
            Player_03 = "Player_03"
            Player_04 = "Player_04"
            Player_05 = "Player_05"
    else:
        Player_01 = "Player_01"
        Player_02 = "Player_02"
        Player_03 = "Player_03"
        Player_04 = "Player_04"
        Player_05 = "Player_05"

    match player_number:
        case 2:
            players = [Player_01, Player_02]
        case 3:
            players = [Player_01, Player_02, Player_03]
        case 4:
            players = [Player_01, Player_02, Player_03, Player_04]
        case 5:
            players = [Player_01, Player_02, Player_03, Player_04, Player_05]

    print("\n\n")
    for i in range(1, player_number + 1):
        print(f"Player_0{i} = {players[i-1]}")

    round = 1

    s_p_1 = 0
    s_p_2 = 0
    s_p_3 = 0
    s_p_4 = 0
    s_p_5 = 0

    while True:
        print(f"\n\n-------Round {round}--------------------------- \n")

        score = [s_p_1, s_p_2, s_p_3, s_p_4, s_p_5]

        for pla in range(player_number):
            print(f"{pla+1}.{players[pla]} = {score[pla]}")

        won = input("\nWho won ? \n-->")

        if won:
            for ro in players:
                if won in ro:
                    round += 1
                else:
                    round = round
        else:
            round = round

        if won == "1":
            s_p_1 += 1
        elif won == "2":
            s_p_2 += 1
        elif won == "3":
            s_p_3 += 1
        elif won == "4":
            s_p_4 += 1
        elif won == "5":
            s_p_5 += 1
        elif won == "q" or won == "Q":
            break

    if s_p_1 > s_p_2 and s_p_1 > s_p_3 and s_p_1 > s_p_4 and s_p_1 > s_p_5:
        print(
            f"\nCongratulations {players[0]} !!.. You won the game by scoring {s_p_1}. "
        )
    elif s_p_2 > s_p_1 and s_p_2 > s_p_3 and s_p_2 > s_p_4 and s_p_2 > s_p_5:
        print(
            f"\nCongratulations {players[1]} !!.. You won the game by scoring {s_p_2}."
        )
    elif s_p_3 > s_p_1 and s_p_3 > s_p_2 and s_p_3 > s_p_4 and s_p_3 > s_p_5:
        print(
            f"\nCongratulations {players[2]} !!.. You won the game by scoring {s_p_3}."
        )
    elif s_p_4 > s_p_1 and s_p_4 > s_p_2 and s_p_4 > s_p_3 and s_p_4 > s_p_5:
        print(
            f"\nCongratulations {players[3]} !!.. You won the game by scoring {s_p_4}."
        )
    elif s_p_5 > s_p_1 and s_p_5 > s_p_2 and s_p_5 > s_p_3 and s_p_5 > s_p_4:
        print(
            f"\nCongratulations {players[4]} !!.. You won the game by scoring {s_p_5}."
        )


game()
