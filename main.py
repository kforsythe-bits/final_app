import submissions
import reports
import simulation

def show_menu():
    print("\n=============================================")
    print("     KAN COMICS: SLUSH PILE MANAGER MENU     ")
    print("=============================================")
    print("a. Log or Update a Comic Submission")
    print("b. View All Active Pitches")
    print("c. Review and Score Active Pitches (Record Review)")
    print("d. View Editorial Review Summary Report")
    print("e. Generate Historical Analytical Charts")
    print("f. Run Predictive Quarter Simulation")
    print("g. Generate Automated Correspondence")
    print("h. Save and Exit")
    print("=============================================")


def main():
    submission_database = submissions.load_submissions()
    historical_logs = submissions.load_logs()
    
    while True:
        show_menu()
        choice = input("Select an option (a-h): ").strip().lower()
        
        if choice == 'a':
            submissions.log_or_update_submission(submission_database)
        elif choice == 'b':
            submissions.view_submissions(submission_database)
        elif choice == 'c':
            submissions.record_pitch_review(submission_database, historical_logs)
        elif choice == 'd':
            reports.show_report(submission_database, historical_logs)
        elif choice == 'e':
            reports.generate_charts(submission_database, historical_logs)
        elif choice == 'f':
            simulation.run_simulation()
        elif choice == 'g':
            print("\n[Coming soon] Generate Automated Correspondence")
        elif choice == 'h':
            submissions.save_submissions(submission_database)
            submissions.save_logs(historical_logs)
            print("\nAll CSV databases saved successfully. Goodbye.")
            break
        else:
            print("\nInvalid choice! Please select a valid letter from the menu (a-h).")

main()