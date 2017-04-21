import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

def MotionCallback(PRI_PIN):
    print "Motion detected"

print "checking motion (ctrl+C to exit)"
time.sleep(2)

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MotionCallback)
    while 1:
        time.sleep(100)        
        
except KeyboardInterrupt:
    print "ending..."
    GPIO.cleanup()
