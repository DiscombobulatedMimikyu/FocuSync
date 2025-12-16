
import serial
import time

print("Start")
port="COM12" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
time.sleep(2)
print("Connected")
run = True
while run:
    want_buzz = input('On buzzer? ')
    if want_buzz.lower() == 'yes':
        bluetooth.write(b'1')
        print('Buzzer On :)')
    else:
        bluetooth.write(b'0')
        run = False
        print('No Buzzer Then :(')
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
