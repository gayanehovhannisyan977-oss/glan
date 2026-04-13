def entrance():
    print("Are you student?")
    answer = input().lower()
    if answer == "yes":
        print("Enter your ID")
        ID = int(input())
    elif answer == "no":
        print("Are you teacher?")
        answer = input().lower()
        if answer == "yes":
            print("n")