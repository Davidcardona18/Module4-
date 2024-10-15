#David Cardona = October 15, 2024. 

# Function to display the menu options
def show_menu():
    # Display the list of available choices
    print("\nPlease choose your option from the list below:")
    print("1. Learn Python")
    print("2. Learn Java")
    print("3. Learn Mathematics")
    print("4. Learn Languages")
    print("5. Learn History")
    print("6. Learn Accounting")
    print("7. Learn Economics")
    print("8. Learn Business Management")
    print("0. Exit")  # Option to exit the program

# Function to handle the user's input and provide feedback based on their choice
def handle_choice(choice):
    if choice == "1":
        print("You selected: Learn Python")
    elif choice == "2":
        print("You selected: Learn Java")
    elif choice == "3":
        print("You selected: Learn Mathematics")
    elif choice == "4":
        print("You selected: Learn Languages")
    elif choice == "5":
        print("You selected: Learn History")
    elif choice == "6":
        print("You selected: Learn Accounting")
    elif choice == "7":
        print("You selected: Learn Economics")
    elif choice == "8":
        print("You selected: Learn Business Management")
    elif choice == "0":
        print("Exiting the program...")  # Exit message
    else:
        # If the user enters an invalid option
        print("Invalid choice. Please select a valid option.")

# Main function to run the program in a loop
def main():
    # Continue looping until the user selects '0' to exit
    while True:
        # Show the menu to the user
        show_menu()
        # Get the user's input
        user_choice = input("Enter your choice: ")
        # If the user selects '0', exit the loop and end the program
        if user_choice == "0":
            handle_choice(user_choice)  # Display exit message
            break  # Exit the loop
        else:
            # Handle the user's choice for all other options
            handle_choice(user_choice)

# Check if the program is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the program
