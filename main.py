# First page menu
def display_menu():
    print("=================================")
    print("        Password Manager         ")
    print("=================================")
    print("1. Create vault")
    print("2. Unlock vault")
    print("3. Exit")


# Gets a valid user input from the menu options
def get_user_input():
    while True:
        user_input = input("Select an option: ")
        
        try:
            user_input = int(user_input)
            if (user_input >= 1 and user_input <= 3):
                # Valid input, return the value
                return user_input
            print("Invalid option. Please choose a number between 1 and 3.")
            
        except ValueError:
            print("Invalid input. Please enter a number.")
        


# Entering the Password Manager functionalities

# Entering first time, need to create a vault
def create_vault():
    print("Feature to create a vault is not implemented yet.")


# Unlocking an existing vault
def unlock_vault():
    print("Feature to unlock a vault is not implemented yet.")


def main():
    display_menu()

    user_input = get_user_input()
        
    if user_input == 1:
        create_vault()
    elif user_input == 2:
        unlock_vault()
    else:
        print("Exiting the Password Manager. Goodbye!")
        return

if __name__ == "__main__":
    main()