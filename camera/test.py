from picamera import PiCamera

camera = PiCamera()
camera.resolution = (600, 400)
camera.capture('screen-shot.png')
