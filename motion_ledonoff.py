import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
LCDPin=7
MotionPin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LCDPin, GPIO.OUT)
GPIO.setup(MotionPin, GPIO.IN)

def MotionCallback(pin):
    if GPIO.input(pin):
        print "rising"
        GPIO.output(LCDPin, True)
    else:
        print "falling"
        GPIO.output(LCDPin, False)

GPIO.add_event_detect(MotionPin, GPIO.BOTH, callback=MotionCallback)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("done")
