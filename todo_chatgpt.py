from print_list import printlist

print("Welcome to Handaleko To-Do List")
tasks = []

while True:
    user_choice = input("Enter one of these commands:\n1- add\n2- view\n3- remove\n4- exit\n>>> ").lower()

    if user_choice == "add":
        tasks.append(input("Enter the task you want to add:\n>>> "))
        print("Task added".upper())
        print("Your Tasks:")
        printlist(tasks)
    elif user_choice == "remove":
        if not tasks:
            print("There is no task to remove")
        else:
            printlist(tasks)
            remove_c_int = int(input("Enter the number of the task you want to remove:\n>>> ")) - 1
            tasks.pop(remove_c_int)
            print("Task removed".upper())
            if not tasks:
                print("Now your to-do list is empty")
            else:
                print("Your new list:".upper())
                printlist(tasks)
    elif user_choice == "view":
        if not tasks:
            print("There is no task to view")
        else:
            print("Your to-do list:".upper())
            printlist(tasks)
    elif user_choice == "exit":
        exit()
    else:
        print("Please enter an available command")
