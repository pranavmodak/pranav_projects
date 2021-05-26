todo=[]

while True:
    to_do_list=input("Enter your task: ")
    todo.append(to_do_list)
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
    
print("your todo is: "+str(todo))