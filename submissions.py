import csv
import datetime

ACTIVE_CSV = "active_submissions.csv"
HISTORICAL_CSV = "historical_logs.csv"

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

def load_logs():
    logs = []
    with open(HISTORICAL_CSV, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            logs.append({
                "log_id": row["LogID"],
                "title": row["Title"],
                "reviewer_id": row["ReviewerID"],
                "days_in_queue": int(row["DaysInQueue"]),
                "final_decision": row["FinalDecision"],
                "date_received": row["DateReceived"]
            })
    return logs

def save_logs(logs):
    with open(HISTORICAL_CSV, mode="w", newline="") as file:
        fieldnames = ["LogID", "Title", "ReviewerID", "DaysInQueue", "FinalDecision", "DateReceived"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for log in logs:
            writer.writerow({
                "LogID": log["log_id"],
                "Title": log["title"],
                "ReviewerID": log["reviewer_id"],
                "DaysInQueue": log["days_in_queue"],
                "FinalDecision": log["final_decision"],
                "DateReceived": log["date_received"]
            })

def show_menu():
    print("\n=============================================")
    print("     KAN COMICS: SLUSH PILE MANAGER MENU     ")
    print("=============================================")
    print("a. Log or Update a Comic Submission")
    print("b. View All Active Pitches")
    print("c. Review and Score Active Pitches (Record Review)")
    print("d. View Editorial Review Summary Report")
    print("e. Generate Analytical Charts")
    print("f. Generate Automated Correspondence")
    print("g. Save and Exit")
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

def record_pitch_review(submissions, logs):
    print("\n--- Review and Score Active Pitches ---")
    title = input("Enter Comic Project Title to review: ").strip()
    
    if title not in submissions:
        print(f"Validation Error: '{title}' does not exist in active submissions.")
        return

    reviewer_id = input("Enter Reviewer ID (e.g., REV-01): ").strip().upper()
    if not reviewer_id:
        print("Validation Error: Reviewer ID cannot be blank.")
        return

    try:
        score = float(input("Enter Technical Score (1.0 - 5.0): "))
        if not (1.0 <= score <= 5.0):
            print("Validation Error: Score must be between 1.0 and 5.0.")
            return

        days_in_queue = int(input("Enter Days Spent in Queue: "))
        if days_in_queue < 0:
            print("Validation Error: Days in queue cannot be negative.")
            return
    except ValueError:
        print("Validation Error: Please enter valid numbers for score and days.")
        return

    print("Select Final Decision: 1) Accepted  2) Rejected")
    decision_choice = input("Enter choice (1 or 2): ").strip()
    if decision_choice == "1":
        decision = "Accepted"
    elif decision_choice == "2":
        decision = "Rejected"
    else:
        print("Validation Error: Invalid decision choice. Review canceled.")
        return

    submissions[title]["score"] = score
    submissions[title]["status"] = decision

    new_log_id = f"LOG-{8821 + len(logs)}"
    logs.append({
        "log_id": new_log_id,
        "title": title,
        "reviewer_id": reviewer_id,
        "days_in_queue": days_in_queue,
        "final_decision": decision,
        "date_received": submissions[title]["date_received"]
    })

    print(f"Success! Review {new_log_id} recorded for '{title}' ({decision}, Score: {score}).")