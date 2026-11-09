def show_menu():
    print("\n=============================================")
    print("     KAN COMICS: SLUSH PILE MANAGER MENU     ")
    print("=============================================")
    print("a. Log a New Comic Submission")
    print("b. Review and Score Active Pitches")
    print("c. Run Quarter Simulation & Generate Charts")
    print("d. Generate Automated Correspondence")
    print("e. Save and Exit")
    print("=============================================")

def main():
    while True:
        show_menu()
        choice = input("Select an option (a-e): ").strip().lower()
        
        if choice == 'a':
            print("\n[Coming soon] Log a New Comic Submission")
        elif choice == 'b':
            print("\n[Coming soon] Review and Score Active Pitches")
        elif choice == 'c':
            print("\n[Coming soon] Run Quarter Simulation & Generate Charts")
        elif choice == 'd':
            print("\n[Coming soon] Generate Automated Correspondence")
        elif choice == 'e':
            print("\nDatabase saved successfully. Terminating operational run loop. Goodbye.")
            break
        else:
            print("\nInvalid choice! Please select a valid letter from the menu (a-e).")

main()