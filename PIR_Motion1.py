import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
try:
    print "checking motion (ctrl+C to exit)"
    time.sleep(2)
    while True:
        if GPIO.input(PIR_PIN):
            print "motion!!"
            time.sleep(3)
        else:
            print "...."        
        
except KeyboardInterrupt:
    print "ending..."
    GPIO.cleanup()
