schedule=[]

while True:
    sch=input("Enter your task: ")
    schedule.append(sch)
    print("task added")
    playmore=input("do you want to add more y/n").lower()
    if playmore=="y":
        print()
    elif playmore=="n":
        print("bye")
        break
    else:
        print("command not found breaking")
        break
    
print("your schedule is: "+str(schedule))