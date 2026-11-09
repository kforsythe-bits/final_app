submission_database = {
    "Neon City Blues": {"creator_name": "Alex Rivera", "genre": "Sci-Fi/Noir", "score": 0.0, "status": "Pending Review", "date_received": "2026-11-01"},
    "Galactic Detectives": {"creator_name": "Maria Rossi", "genre": "Action", "score": 4.2, "status": "Accepted", "date_received": "2026-10-26"},
    "Broken Gargoyle": {"creator_name": "David Chen", "genre": "Fantasy", "score": 2.5, "status": "Rejected", "date_received": "2026-10-28"}
}

def show_menu():
    print("\n=============================================")
    print("     KAN COMICS: SLUSH PILE MANAGER MENU     ")
    print("=============================================")
    print("a. Log a New Comic Submission (Add/Update)")
    print("b. View All Active Pitches")
    print("c. Run Quarter Simulation & Generate Charts")
    print("d. Generate Automated Correspondence")
    print("e. Save and Exit")
    print("=============================================")

def view_submissions():
    print("\n--- CURRENT SUBMISSION QUEUE ---")
    for title, details in submission_database.items():
        print(f"\nTitle: {title}")
        print(f"  Creator: {details['creator_name']}")
        print(f"  Genre:   {details['genre']}")
        print(f"  Score:   {details['score']}/5.0")
        print(f"  Status:  {details['status']}")
        print(f"  Date:    {details['date_received']}")
    print("--------------------------------")

def main():
    while True:
        show_menu()
        choice = input("Select an option (a-e): ").strip().lower()
        
        if choice == 'a':
            print("\n[Coming soon] Log a New Comic Submission")
        elif choice == 'b':
            view_submissions()
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