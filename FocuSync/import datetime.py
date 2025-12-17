import datetime
import time # Imported to manage the waiting interval

def check_time(target_time):
    current_time = datetime.datetime.now()
    string_time = current_time.strftime('%d/%m/%Y %I:%M %p')

    # Check if the current time matches the target
    if string_time == target_time:
        return True
    else:
        print(f"Not yet... Current time: {string_time}")
        return False

# Main Execution Loop
active = True
target_alarm = '16/12/2025 04:12 PM'

print(f"Waiting for {target_alarm}...")

while active:
    # Call the function to check the time
    is_alarm_time = check_time(target_alarm)

    if is_alarm_time:
        print("BUZZ! BUZZ! BUZZ!")
        
        # We ask specifically to stop inside the alarm block
        stop = input('Alarm ringing! Type "Yes" to stop: ').title()
        
        if stop == 'Yes':
            print("Alarm stopped.")
            active = False
        # If they don't type Yes, the loop repeats and buzzes again
        
    else:
        # Wait 1 second before checking again to save CPU power
        time.sleep(1)