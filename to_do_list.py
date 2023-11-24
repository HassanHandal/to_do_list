from print_list import printlist
print("welcome to Handaleko to do list")
tasks = []
while True:
    user_choice = input("Enter one of these commads: \n1- add\n2- view\n3- remove\n4- exit \n>>>")
    if user_choice.lower() == "add":
        new_task = input("enter the task you want to add :\n>>> ")
        tasks.append(new_task)
        print("task added".upper())
        print("Your Tasks :")
        printlist(tasks)
    elif user_choice.lower() == "remove" :
        if not tasks:
            print("There is no task to remove")
        else:
            printlist(tasks)
            remove_c_str = input("enter the number of the task you need to remove :\n>>> ")
            remove_c_int = int(remove_c_str)
            tasks.pop(remove_c_int-1)
            print("task removed".upper())
            if not tasks:
                print("Now your to do list is empty")
            else:
                print("Your new list :".upper())
                printlist(tasks)
    elif user_choice.lower() == "view" :
        if not tasks:
            print("there is no task to view")
        else:
            print("that's your to do list".upper())
            printlist(tasks)
    elif user_choice.lower() == "exit":
        exit()
    else:
        print("please enter an available command")
