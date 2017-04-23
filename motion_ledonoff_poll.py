import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# define variable for LED pin and motion sensor 
ledPin=7
motionPin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(motionPin, GPIO.IN)


def GetTimeStamp():
    string1 = time.strftime("%d/%m/%Y")
    string2 = time.strftime("%I:%M:%S")
    return string1+" "+string2

try:
    while True:
        if GPIO.input(motionPin):
            print "motion: ", GetTimeStamp()
            GPIO.output(ledPin, True)
        else:
            GPIO.output(ledPin, False) 
except KeyboardInterrupt:
    GPIO.cleanup()
    print("done")
