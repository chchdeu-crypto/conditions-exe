trip=input("where do you want to go?")
match trip:
    case forest:
        choose=input("hide or walk")
        if choose == "hide":
            print("you hide behind a tree")
        elif choose == "walk":
            print("you find a sleeping wolf")
        else:
            print("unvalid forest action")

