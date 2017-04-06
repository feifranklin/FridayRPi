import RPi.GPIO as GPIO
import datetime         # datetime.datetime.now()
import time             # sleep()

buttonPIN = 13          # variable for switch GPIO pin 
ledRed = 7              # variable for red GPIO pin  
ledGreen = 12           # variable for green GPIO pin  
ledYellow = 16          # variable for yellow GPIO pin  

# create a list
lights = [ledRed, ledGreen, ledYellow]

led_index = 0
led_on_state = False

#define callback function
def my_callback(pin):
    # determie the active LED
    global led_index
    active_led = lights[led_index]

    if GPIO.input(pin) == GPIO.HIGH:
        print "Push down at\t", str(datetime.datetime.now())
        led_on_state = True
    else:
        print "Push up at\t", str(datetime.datetime.now())
        led_on_state = False


    # turn on/off led only when state is changed
    if led_on_state:
        GPIO.output(active_led, True)
    else:
        GPIO.output(active_led, False) 
        led_index = (led_index + 1) % len(lights)

#m main function
try: 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #GPIO.setup(buttonPIN, GPIO.IN)
    
    # original: GPIO.setup(ledRed, GPIO.OUT)
    # use loop for setup all 3 LED
    for led in lights:
        GPIO.setup(led, GPIO.OUT)


    GPIO.add_event_detect(buttonPIN, GPIO.BOTH, callback=my_callback)
    print "press swtich button"
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print "exit"
    GPIO.cleanup()


print "done"


