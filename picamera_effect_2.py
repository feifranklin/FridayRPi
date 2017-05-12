from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    print('effect = %s' % effect)
    camera.annotate_text = '%s' % effect
    sleep(5)


camera.stop_preview()

