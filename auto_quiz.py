import random

print(
    "\n\n-----------------------------------------------------------------------------------------------------------------------------------------------------"
)
print(" \n \ntype Q to quit game \nand type LL to use lifeline \n \n")
# print("Note: If you use life line your money will be decrease by Rs. 5000 in each  step.")


def quiz():
    round = 0
    while round <= 50:
        round = round + 1

        print(
            "-----------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print(f"\nRound-{round}")

        operations = ["sum", "difference", "quotient", "product"]
        # operation_selecet = random.choice(operations)
        operation_selecet = random.choice(operations)

        first_question_digit = random.randrange(1000)
        second_question_dgit = random.randrange(1000)
        ran_num = random.randrange(1000)

        if (
            operation_selecet == "sum"
            or operation_selecet == "difference"
            or operation_selecet == "product"
        ):
            question = f"\nWhat is the {operation_selecet} of {first_question_digit} and {second_question_dgit} ?"
        elif operation_selecet == "quotient":
            question = f"\nWhat is the {operation_selecet} of ({first_question_digit} divided by {second_question_dgit}) ?"

        print(question)

        match operation_selecet:
            case "sum":
                correct_answer = first_question_digit + second_question_dgit
            case "difference":
                if first_question_digit > second_question_dgit:
                    correct_answer = first_question_digit - second_question_dgit
                else:
                    correct_answer = second_question_dgit - first_question_digit

            case "product":
                correct_answer = first_question_digit * second_question_dgit
            case "quotient":
                correct_answer = int(first_question_digit / second_question_dgit)

        correct_answer = str(correct_answer)

        option_list = [ran_num, ran_num, ran_num, correct_answer]
        final_option_list = random.shuffle(option_list)

        option = [
            random.randrange(1000),
            correct_answer,
            random.randrange(1000),
            random.randrange(1000),
        ]
        random.shuffle(option)

        options = [option[0], option[1], option[2], option[3]]

        print(f"a.{options[0]}", end="\t")
        print(f"b.{options[1]}")
        print(f"c.{options[2]}", end="\t")
        print(f"d.{options[3]} \n")

        print("Correct answer = ", correct_answer)

        user_answer = input("Your answer = ").lower()

        if user_answer == "a":
            answer = option[0]
        elif user_answer == "b":
            answer = option[1]
        elif user_answer == "c":
            answer = option[2]
        elif user_answer == "d":
            answer = option[3]
        else:
            answer = user_answer

        money = 0

        # answer_time = int(time.localtime().tm_sec)
        # if (answer_time == answer_time+30):
        #     break

        if answer == "q":
            print(" \nYou quite")
            money = 0
            break

        if answer == "ll":
            options = [ran_num, correct_answer]
            random.shuffle(options)

            print(f"\na.{options[0]}", end="\t")
            print(f"b.{options[1]}")

            print("correct answers is", correct_answer)

            user_ll_answer = input(" \nYour answer =")

            if user_ll_answer == "a":
                answer = options[0]
            elif user_ll_answer == "b":
                answer = options[1]
            else:
                answer = user_ll_answer

        if answer == correct_answer:
            print("Correct answer = ", correct_answer, "\n")
            print(
                "congratulation you are on next round  \n",
            )
            if round == 5:
                print("You have won Rs.", money + 10000)
            elif round == 10:
                print("You have won Rs.", money + 30000)
            elif round == 20:
                print("You have won Rs.", money + 50000)
            elif round == 30:
                print("You have won Rs.", money + 100000)
            elif round == 50:
                print("You have won Rs.", money + 1000000)

            continue

        # elif (user_answer != "a" or user_answer != "b" or user_answer != "c" or user_answer != "d"):
        #     break
        else:
            print("Correct answer = ", correct_answer)
            print("\nYour answers is wrong", "\n")
            if round > 1 and round < 5:
                if answer != correct_answer:
                    print("You have lost all money. You money is", money, "\n")
                    break
            elif round > 5 and round < 10:
                if answer != correct_answer:
                    print("Your money is", money + 10000, "\n")
                    break
            elif round > 10 and round < 20:
                if answer != correct_answer:
                    print("Your money is", money + 30000, "\n")
                    break
            elif round > 20 and round < 30:
                if answer != correct_answer:
                    print("Your money is", money + 50000, "\n")
                    break
            elif round > 30 and round < 50:
                if answer != correct_answer:
                    print("Your money is", money + 100000, "\n")
                    break

            break


quiz()
