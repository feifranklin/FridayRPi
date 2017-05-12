import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setwarnings(False)

# define variable for LED pin and motion sensor 
ledPin=7
motionPin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(motionPin, GPIO.IN)

camera = PiCamera()

def MotionCallback(pin):
    if GPIO.input(pin):
        print "rising(turn on) ", GetTimeStamp()
        GPIO.output(ledPin, True)
        camera.start_preview()
        camera.capture('/home/pi/Desktop/motion/image%s.jpg' % GetTimeStamp())
        camera.stop_preview()
        time.sleep(3)
    else:
        print "falling(turn off)", GetTimeStamp()
        GPIO.output(ledPin, False)

def GetTimeStamp():
    string1 = time.strftime("%d_%m_%Y")
    string2 = time.strftime("%I_%M_%S")
    return string1+" "+string2

GPIO.add_event_detect(motionPin, GPIO.BOTH, callback=MotionCallback)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("done")
