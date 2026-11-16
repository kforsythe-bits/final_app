import csv
import datetime

ACTIVE_CSV = "active_submissions.csv"

def load_submissions():
    submissions = {}
    with open(ACTIVE_CSV, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["Title"]
            submissions[title] = {
                "creator_name": row["CreatorName"],
                "genre": row["Genre"],
                "score": float(row["Score"]),
                "status": row["Status"],
                "date_received": row["DateReceived"]
            }
    return submissions

def save_submissions(submissions):
    with open(ACTIVE_CSV, mode="w", newline="") as file:
        fieldnames = ["Title", "CreatorName", "Genre", "Score", "Status", "DateReceived"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for title, details in submissions.items():
            writer.writerow({
                "Title": title,
                "CreatorName": details["creator_name"],
                "Genre": details["genre"],
                "Score": details["score"],
                "Status": details["status"],
                "DateReceived": details["date_received"]
            })

def show_menu():
    print("\n=============================================")
    print("     KAN COMICS: SLUSH PILE MANAGER MENU     ")
    print("=============================================")
    print("a. Log or Update a Comic Submission")
    print("b. View All Active Pitches")
    print("c. Review and Score Active Pitches (Record Review)")
    print("d. Run Quarter Simulation & Generate Charts")
    print("e. Generate Automated Correspondence")
    print("f. Save and Exit")
    print("=============================================")

def view_submissions(submissions):
    print("\n--- CURRENT SUBMISSION QUEUE ---")
    for title, details in submissions.items():
        print(f"\nTitle: {title}")
        print(f"  Creator: {details['creator_name']}")
        print(f"  Genre:   {details['genre']}")
        print(f"  Score:   {details['score']}/5.0")
        print(f"  Status:  {details['status']}")
        print(f"  Date:    {details['date_received']}")
    print("--------------------------------")

def log_or_update_submission(submissions):
    print("\n--- Log or Update a Comic Submission ---")
    title = input("Enter Comic Project Title: ").strip()
    
    if title in submissions:
        print(f"\nMatch found! Updating existing profile data for: '{title}'")
        try:
            new_score = float(input("Assign structural quality rating score (1.0 - 5.0): "))
            if 1.0 <= new_score <= 5.0:
                submissions[title]["score"] = new_score
                
                print("Select Status: 1) Accepted  2) Rejected  3) Pending Review")
                status_choice = input("Enter status number choice: ").strip()
                status_map = {"1": "Accepted", "2": "Rejected", "3": "Pending Review"}
                submissions[title]["status"] = status_map.get(status_choice, "Pending Review")
                print(f"Successfully updated metadata parameters for '{title}'.")
            else:
                print("Validation Error: Score value was out of range bounds. Changes canceled.")
        except ValueError:
            print("Validation Error: System expected numeric digits.")
    else:
        print(f"\n'{title}' is a fresh concept. Initializing database submission logging...")
        creator = input("Enter Creator's Full Name: ").strip()
        genre = input("Enter Comic Genre: ").strip()
        today_str = str(datetime.date.today())
        
        submissions[title] = {
            "creator_name": creator,
            "genre": genre,
            "score": 0.0,
            "status": "Pending Review",
            "date_received": today_str
        }
        print(f"Success: '{title}' added to the queue under 'Pending Review'.")

def main():
    submission_database = load_submissions()
    
    while True:
        show_menu()
        choice = input("Select an option (a-f): ").strip().lower()
        
        if choice == 'a':
            log_or_update_submission(submission_database)
        elif choice == 'b':
            view_submissions(submission_database)
        elif choice == 'c':
            print("\n[Coming soon] Review and Score Active Pitches")
        elif choice == 'd':
            print("\n[Coming soon] Run Quarter Simulation & Generate Charts")
        elif choice == 'e':
            print("\n[Coming soon] Generate Automated Correspondence")
        elif choice == 'f':
            save_submissions(submission_database)
            print("\nDatabase saved successfully. Terminating operational run loop. Goodbye.")
            break
        else:
            print("\nInvalid choice! Please select a valid letter from the menu (a-f).")


main()