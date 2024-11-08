from datetime import datetime

# Shift times
full = "21:30:00"  # Full night starts at 21:30 (9:30 PM)
day = "07:30:00"   # Day shift starts at 07:30 (7:30 AM)
half = "17:30:00"  # Half night shift starts at 17:30 (5:30 PM)

# Convert time strings to time objects for accurate comparison
full_time = datetime.strptime(full, "%H:%M:%S").time()
day_time = datetime.strptime(day, "%H:%M:%S").time()
half_time = datetime.strptime(half, "%H:%M:%S").time()

def get_shift(current_time):
    """
    This function determines the current shift based on the current time.
    Full Night: 21:30 PM - 07:30 AM
    Day: 07:30 AM - 17:30 PM
    Half Night: 17:30 PM - 21:30 PM
    """
    # Convert current time string to datetime object
    current_time_obj = datetime.strptime(current_time, "%H:%M:%S").time()

    # Full Night shift is from 9:30 PM to 7:30 AM (next day)
    if full_time <= current_time_obj or current_time_obj < day_time:
        return "Full Night Shift"
    # Day shift is from 7:30 AM to 5:30 PM
    elif day_time <= current_time_obj < half_time:
        return "Day Shift"
    # Half Night shift is from 5:30 PM to 9:30 PM
    elif half_time <= current_time_obj < full_time:
        return "Half Night Shift"
    else:
        return "Unknown Shift"  # For any time outside these ranges

# Testing with different times
test_times = ["03:35:00", "08:00:00", "18:00:00", "21:00:00"]

for time in test_times:
    print(f"Current Time: {time} -> Shift: {get_shift(time)}")
