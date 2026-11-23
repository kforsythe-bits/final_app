import matplotlib.pyplot as plt

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

def generate_charts(submissions, logs):
    if not logs or not submissions:
        print("\n[System Alert] Insufficient database volume to generate analytical graphs.")
        return

    genre_scores = {}
    genre_counts = {}
    
    for title, details in submissions.items():
        gen = details["genre"]
        if gen not in genre_scores:
            genre_scores[gen] = 0.0
            genre_counts[gen] = 0
        genre_scores[gen] += details["score"]
        genre_counts[gen] += 1

    genres_list = list(genre_scores.keys())
    avg_scores_list = []
    for g in genres_list:
        avg_scores_list.append(genre_scores[g] / genre_counts[g])

    plt.figure()
    plt.bar(genres_list, avg_scores_list, color="skyblue", edgecolor="black")
    plt.title("Average Talent Evaluation Score by Genre")
    plt.xlabel("Comic Book Genres")
    plt.ylabel("Average Structural Score (1-5)")
    plt.savefig("genre_scores_bar.png")
    plt.close()

    log_ids = []
    wait_times = []
    for log in logs:
        log_ids.append(log["log_id"])
        wait_times.append(log["days_in_queue"])

    plt.figure()
    plt.plot(log_ids, wait_times, marker="o", color="purple", linestyle="-", linewidth=2)
    plt.title("Slush Pile Pipeline Wait Time Trend")
    plt.xlabel("Review Log Record Sequence")
    plt.ylabel("Days Spent in Processing Queue")
    plt.savefig("queue_wait_line.png")
    plt.close()

    print("\n[Graphics Engine] Graphs compiled and saved as PNG graphics inside project folder!")   