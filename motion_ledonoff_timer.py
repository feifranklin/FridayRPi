import RPi.GPIO as GPIO
import time
import motion_email

GPIO.setwarnings(False)
LCDPin=7
MotionPin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LCDPin, GPIO.OUT)
GPIO.setup(MotionPin, GPIO.IN)
threshold = 0

def MotionCallback(pin):
    global threshold
    f = open('motion.log', 'a')
    if GPIO.input(pin):
        print "rising"
        GPIO.output(LCDPin, True)
        f.write(time.strftime("motion detected: %a, %d %b %Y %H:%M:%S +0000\n", time.localtime()))
        f.close()
        if threshold < 5:
            threshold += 1
        else:
            print 'prepare email'
            motion_email.MotionSendEmail()
            threshold = 0  
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
