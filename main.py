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

def show_report(submissions, logs):
    if not logs:
        print("\n[System Alert] No review transactions recorded yet.")
        return

    total_reviews = len(logs)
    total_days = 0
    max_days = -1
    slowest_pitch = ""
    
    reviewer_counts = {}

    for log in logs:
        total_days += log["days_in_queue"]
        
        if log["days_in_queue"] > max_days:
            max_days = log["days_in_queue"]
            slowest_pitch = log["title"]
            
        rev_id = log["reviewer_id"]
        if rev_id not in reviewer_counts:
            reviewer_counts[rev_id] = 0
        reviewer_counts[rev_id] += 1

    avg_days = total_days / total_reviews

    print("\n--- EDITORIAL REVIEW SUMMARY REPORT ---")
    print(f"Total Reviews Logged:     {total_reviews}")
    print(f"Total Combined Queue Days: {total_days} days")
    print(f"Average Processing Speed:  {avg_days:.1f} days per pitch")
    print(f"Slowest Pipeline Bottleneck: '{slowest_pitch}' ({max_days} days in pile)")
    
    print("\nTotal Completed Evaluations by Reviewer:")
    for reviewer, count in reviewer_counts.items():
        print(f"   {reviewer}: {count} pitch(es)")
    print("---------------------------------------")

def main():
    submission_database = load_submissions()
    historical_logs = load_logs()
    
    while True:
        show_menu()
        choice = input("Select an option (a-g): ").strip().lower()
        
        if choice == 'a':
            log_or_update_submission(submission_database)
        elif choice == 'b':
            view_submissions(submission_database)
        elif choice == 'c':
            record_pitch_review(submission_database, historical_logs)
        elif choice == 'd':
            show_report(submission_database, historical_logs)
        elif choice == 'e':
            print("\n[Coming soon] Generate Analytical Charts")
        elif choice == 'f':
            print("\n[Coming soon] Generate Automated Correspondence")
        elif choice == 'g':
            save_submissions(submission_database)
            save_logs(historical_logs)
            print("\nAll CSV databases saved successfully. Goodbye.")
            break
        else:
            print("\nInvalid choice! Please select a valid letter from the menu (a-g).")

main()