import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# define variable for LED pin and motion sensor 
ledPin=7
motionPin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(motionPin, GPIO.IN)

def MotionCallback(pin):
    if GPIO.input(pin):
        print "rising(turn on) ", GetTimeStampMS()
        GPIO.output(ledPin, True)
    else:
        print "falling(turn off)", GetTimeStampMS()
        GPIO.output(ledPin, False)

def GetTimeStamp():
    string1 = time.strftime("%d/%m/%Y")
    string2 = time.strftime("%I:%M:%S")
    return string1+" "+string2


GPIO.add_event_detect(motionPin, GPIO.BOTH, callback=MotionCallback)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("done")
