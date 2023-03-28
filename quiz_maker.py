# Though It is still not completed but can be used.......

import random
import getpass


print(
    "\n\n-----------------------------------------------------------------------------------------------------------------------------------------------------\n"
)

while True:
    question = input("Enter question \n-->")

    question_answer = getpass.getpass("Enter answer :")

    option_number = int(input("\nHow many option you want to make (2,3,4,5)-->"))

    if option_number == 2:
        option_a = input("\nFirst option:\n-->")
        option_b = input("Second option:\n-->")
        options = [option_a, option_b]
    elif option_number == 3:
        option_a = input("\nFirst option:\n-->")
        option_b = input("Second option:\n-->")
        option_c = input("Third option:\n-->")
        options = [option_a, option_b, option_c]
    elif option_number == 4:
        option_a = input("\nFirst option:\n-->")
        option_b = input("Second option:\n-->")
        option_c = input("Third option:\n-->")
        option_d = input("Forth option:\n-->")
        options = [option_a, option_b, option_c, option_d]
    elif option_number == 5:
        option_a = input("\nFirst option:\n-->")
        option_b = input("Second option:\n-->")
        option_c = input("Third option:\n-->")
        option_d = input("Forth option:\n-->")
        option_e = input("Fifth option:\n-->")
        options = [option_a, option_b, option_c, option_d, option_e]
    else:
        print("Not valid")
        break
    print("\n")
    print(question)

    if option_number == 2:
        print("a.", options[0], end="\t")
        print("b.", options[1])
    elif option_number == 3:
        print("a.", options[0], end="\t")
        print("b.", options[1])
        print("c.", options[2])
    elif option_number == 4:
        print("a.", options[0], end="\t")
        print("b.", options[1])
        print("c.", options[2], end="\t")
        print("d.", options[3])
    elif option_number == 5:
        print("a.", options[0], end="\t")
        print("b.", options[1])
        print("c.", options[2], end="\t")
        print("d.", options[3])
        print("e.", options[4])

    contestent_answer = input("\nYour answer = ")

    if contestent_answer == "a":
        contestent_answer = option_a
    elif contestent_answer == "b":
        contestent_answer = option_b
    elif contestent_answer == "c":
        contestent_answer = option_c
    elif contestent_answer == "d":
        contestent_answer == option_d
    elif contestent_answer == "e":
        contestent_answer = option_e
    # elif(contestent_answer != option_a or contestent_answer != option_b or contestent_answer != option_c or contestent_answer != option_d or contestent_answer!= option_e):
    #     break

    print("Correct answer = ", question_answer, "\n")

    if contestent_answer == question_answer:
        result = "true"
        print(contestent_answer, " is correct answer\n\n")
        continue
    else:
        result = "false"
        print(contestent_answer, " is wrong answer\n\n")
        break
