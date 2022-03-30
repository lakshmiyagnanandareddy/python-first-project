import random
Y = "y"

def introduction():
    print("This is the guessing game\n"
          "You have to find the computer guess in 7 chances\n"
          "Hint : weather the your guess is lower than computer guess or higher than the computer guess")


def randm():
    comp_number = random.randint(1, 100)
    return comp_number


def main():
    introduction()
    comp_score = 0
    user_score = 0
    y = "y"
    while Y == y:
        comp_number = randm()
        for i in range(7):
            user_number = int(input("Enter the guess number "))
            if comp_number == user_number:
                print("you won the game")
                user_score = user_score+1
                break
            elif comp_number < user_number:
                #print(comp_number)
                print("Your number is less than computer number")
            elif comp_number > user_number:
                print("Your number is greater than computer number")
            elif i == 6:
                comp_score = comp_score+1
        print("your score is ", user_score)
        print("computer score is", comp_score)
        y = input("Enter 'y' to play again ")


main()
