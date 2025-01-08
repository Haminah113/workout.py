import time

def workout_cycle():
    # Time duration for each stage (in seconds)
    warm_up_duration = 5    # Warm-up
    exercise_duration = 10  # Exercise
    cool_down_duration = 5  # Cool-down

    while True:
        # Warm-up stage
        print("Warm-up: START")
        time.sleep(warm_up_duration)
        print("Warm-up: DONE")
        time.sleep(1)  # Short break before the next stage

        # Exercise stage
        print("Exercise: START")
        time.sleep(exercise_duration)
        print("Exercise: DONE")
        time.sleep(1)  # Short break before the next stage

        # Cool-down stage
        print("Cool-down: START")
        time.sleep(cool_down_duration)
        print("Cool-down: DONE")
        time.sleep(1)  # Short break before restarting the cycle

# Run the workout cycle
workout_cycle()