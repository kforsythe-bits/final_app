import datetime

submission_database = {
    "Neon City Blues": {"creator_name": "Alex Rivera", "genre": "Sci-Fi/Noir", "score": 0.0, "status": "Pending Review", "date_received": "2026-11-01"},
    "Galactic Detectives": {"creator_name": "Maria Rossi", "genre": "Action", "score": 4.2, "status": "Accepted", "date_received": "2026-10-26"},
    "Broken Gargoyle": {"creator_name": "David Chen", "genre": "Fantasy", "score": 2.5, "status": "Rejected", "date_received": "2026-10-28"}
}

def show_menu():
    print("\n=============================================")
    print("     KAN COMICS: SLUSH PILE MANAGER MENU     ")
    print("=============================================")
    print("a. Log or Update a Comic Submission")
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

def log_or_update_submission():
    print("\n--- Log or Update a Comic Submission ---")
    title = input("Enter Comic Project Title: ").strip()
    
    if title in submission_database:
        print(f"\nMatch found! Updating existing profile data for: '{title}'")
        try:
            new_score = float(input("Assign structural quality rating score (1.0 - 5.0): "))
            if 1.0 <= new_score <= 5.0:
                submission_database[title]["score"] = new_score
                
                print("Select Status: 1) Accepted  2) Rejected  3) Pending Review")
                status_choice = input("Enter status number choice: ").strip()
                status_map = {"1": "Accepted", "2": "Rejected", "3": "Pending Review"}
                submission_database[title]["status"] = status_map.get(status_choice, "Pending Review")
                print(f"Successfully updated metadata parameters for '{title}'.")
            else:
                print("Validation Error: Score value was out of range bounds. Changes canceled.")
        except ValueError:
            print("Validation Error: System expected numeric digits. String characters cannot be applied.")
            
    else:
        print(f"\n'{title}' is a fresh concept. Initializing database submission logging...")
        creator = input("Enter Creator's Full Name: ").strip()
        genre = input("Enter Comic Genre: ").strip()
        today_str = datetime.date.today().strftime("%Y-%m-%d")
        
        submission_database[title] = {
            "creator_name": creator,
            "genre": genre,
            "score": 0.0,
            "status": "Pending Review",
            "date_received": today_str
        }
        print(f"Success: '{title}' added to the queue under 'Pending Review'.")

def main():
    while True:
        show_menu()
        choice = input("Select an option (a-e): ").strip().lower()
        
        if choice == 'a':
            log_or_update_submission()
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