trip=input("where do you want to go?")
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
           


