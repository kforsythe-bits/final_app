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

print(simulate_quarter(4))