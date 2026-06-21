#number 1
'''trip=input("where do you want to go?")
match trip:
    case "forest":
        choose=input("hide or walk")
        if choose == "hide":
            print("you hide behind a tree")
        elif choose == "walk":
            print("you find a sleeping wolf")
        else:
            print("unvalid forest action")
    case "cave":
        choose=input("do you have a torch") 
        if choose == "yes":
            turn=input("left or right")
            if turn == "left":
                print("you find gold")
            elif turn == "right":
                print("you find bats")
            else:
                print("invalid cave path")
        else:
            print("its too dark to enter")
    case "river":
        print("you find boat")
    case _:
        print("unknoen place")
#number 2
num_1 = float(input("choose first number"))
num_2 = float(input("choose second number"))
action = input("whitch action you want") 
if action == "add":
    print(num_1 + num_2)
elif action == "subtract":
    print(num_1 - num_2)
elif action == "multiply":
    print(num_1 * num_2)
else:
    print("unknoen action")
#mumber 3
computer_choice = "rock"
user_choice = input("enter your choice")
if user_choice == computer_choice:
    print("draw")
elif user_choice =="paper":
    print("you win")
elif user_choice == "scissors":
    print("computer win")
elif user_choice == "rock":
    print("draw")
else:
    print("invalid move")'''
#number 4
correct_pin = 4321
balance = int(500)
user_pin = int(input("enter your pin"))
if user_pin == correct_pin:
    money = int(input("how much money do you want to draw"))
    if money > balance:
        print("not enough money")
    else:
        recepit = input("do you want a recepit")
        if recepit == "yes":
            print("withdrawal approved with recepit")
        elif recepit == "no":
            print("withdrawal approved without recepit")
        else:
            print("withdrawal approved1")
else:
    print("wrong pin")            
    


        


