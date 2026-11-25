import random
import matplotlib.pyplot as plt

WEEKS_PER_QUARTER = 12
MIN_WEEKLY_PITCHES = 15
MAX_WEEKLY_PITCHES = 45
PITCHES_PER_EDITOR = 8
HIGH_SCORE_RATE = 0.20
TRIALS = 1000


def simulate_quarter(editors):
    bottlenecked_high_pitches = 0
    weekly_capacity = editors * PITCHES_PER_EDITOR
    
    for week in range(WEEKS_PER_QUARTER):
        incoming_pitches = random.randint(MIN_WEEKLY_PITCHES, MAX_WEEKLY_PITCHES)
        
        if incoming_pitches > weekly_capacity:
            backlog_size = incoming_pitches - weekly_capacity
            
            for pitch in range(backlog_size):
                if random.random() <= HIGH_SCORE_RATE:
                    bottlenecked_high_pitches = bottlenecked_high_pitches + 1
                    
    return bottlenecked_high_pitches

def average_bottlenecked_pitches(editors, trials):
    total = 0
    for trial in range(trials):
        total = total + simulate_quarter(editors)
    return total / trials

def run_simulation():
    options = [2, 3, 4, 5, 6]
    results = []

    print("\nSimulating", TRIALS, "quarters for each editor staffing level...")
    print("Editors   Avg High-Scoring Pitches Bottlenecked Per Quarter")
    for editors in options:
        average = average_bottlenecked_pitches(editors, TRIALS)
        results.append(average)
        print("  ", editors, "         ", round(average, 2))

    recommended = 0
    for i in range(len(options)):
        if results[i] < 2.0 and recommended == 0:
            recommended = options[i]

    if recommended == 0:
        print("\nNone of the options were sufficient. Recruit more reviewer staff.")
    else:
        print("\nRecommendation: Schedule", recommended, "editors to manage submission flow.")

run_simulation()