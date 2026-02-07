def create_menu():
    print("GYM TRACKER")
    print("Please type the corresponding number to the choice you want")
    print("1 - Create a new workout routine")
    print("2 - Load a new workout routine")
    print("3 - Exit")


def call_functions():
    user_choice = input("Enter number of choice: ")
    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        print("Must be 1, 2 or 3")
        user_choice = input("Enter number of choice: ")
    if user_choice == 1:
        create_new_workout()
    elif user_choice == 2:
        load_workout()
    elif user_choice == 3:
        quit()

def create_new_workout():
    print("temp")

def load_workout():
    print("temp")

create_menu()
call_functions()
