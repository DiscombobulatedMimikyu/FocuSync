import serial
import time as t
from datetime import datetime
import get_json as db
SERIAL_PORT = "COM7"
BAUD_RATE = 9600

bt = serial.Serial(SERIAL_PORT, BAUD_RATE)

alarm_time = f'{date} {time}'

alarm_triggered = False

def check_alarm():
    global alarm_triggered
    
    while True:
        now = datetime.now().strftime('%d/%m/%Y %I:%M %p')
        if now == alarm_time and not alarm_triggered:
            bt.write(b"START")
            alarm_triggered = True
            stop = input('Stop? ').title()
            if stop == 'Yes':
                bt.write(b"STOP")
        t.sleep(2)

check_alarm()


