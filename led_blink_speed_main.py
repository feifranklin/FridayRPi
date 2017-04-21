import led_blink_speed_blink

if __name__ == '__main__':
    print 'enter main function'
    try:
        led_blink_speed_blink.blink(7, 5, 2) 
    except KeyboardInterrupt:
        GPIO.cleanup()
        print 'except keyboardinterrupt'

print 'exit'
