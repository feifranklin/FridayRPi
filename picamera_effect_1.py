from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate =15
camera.start_preview()
camera.annotate_text = 'hello frank'
camera.brightness = 70
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
camera.resolution = (64, 64)
camera.brightness = 30
camera.framerate =15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/min.jpg')
camera.stop_preview()

