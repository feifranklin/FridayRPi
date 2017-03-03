import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
BUZZ_PIN = 11
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZ_PIN, GPIO.OUT)
try:
    print "checking motion (ctrl+C to exit)"
    time.sleep(2)
    while True:
        if GPIO.input(PIR_PIN):
            print "motion!!"
            GPIO.output(BUZZ_PIN, True)
            time.sleep(3)
            GPIO.output(BUZZ_PIN, False)
        else:
            print "...."        
        
except KeyboardInterrupt:
    print "ending..."
    GPIO.cleanup()
