import baseline_generator as bg
import cipher_solver as ciph

# Define constants for reusable paths
DEFAULT_BASELINE = "data/eng_baseline.json"

def main():
    """Main function to start the Ceasar Encryption Programme."""
    print("*** Ceasar Encryption Programme ***")
    main_menu()


def main_menu() -> None:
    """Displays the main menu and handles user input for different actions."""
    while True:
        action_choice = input(
            "\nChoose an option:"
            "\nDecrypt (d)"
            "\nEncrypt (e)"
            "\nCreate new baseline (b)"
            "\nExit (x)\n"
        ).strip().lower()
       
        if action_choice == "d":
            decrypt_menu()
        elif action_choice == "e":
            encrypt_menu()
        elif action_choice == "b":
            bg.get_baseline()
        elif action_choice == "x":
            print("Exiting the program. Goodbye!")
            return  # Exit the loop and end the program
        else:
            print("Invalid choice. Please type 'd', 'e', 'b', or 'x' and hit enter.\n")


def decrypt_menu() -> None:
    """Displays the decrypt menu and handles user input for decryption options."""
    while True:
        action_choice = input(
            "\nChoose an option:"
            "\nUse key (k)"
            "\nSolve key (s)"
            "\nReturn to main menu (r)\n"
        ).strip().lower()
        
        if action_choice == "r":
            return # Exit the function and return to the main menu
        elif action_choice == "k":
            ciph.decrypt()
        elif action_choice == "s":
            ciph.cipher_solver()
        else:
            print("Invalid input. Please type 'k', 's', or 'r'.\n")


def encrypt_menu() -> None:
    """Displays the encrypt menu and handles user input for encryption options."""
    while True:
        ciph.encrypt()

        while True:
            action_choice = input("Choose an option:"
                            "\nEncrypt new text (e)"
                            "\nReturn to main menu(r)\n").strip().lower()
            if action_choice == "e":
                # Restart the encryption process by breaking out of the inner loop
                break
            elif action_choice == "r":
                # Exit the function and return to the main menu
                return
            else:
                print("Invalid input. Please type 'e' or 'r'.\n")



if __name__ == "__main__":
    main()