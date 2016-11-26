from picamera import PiCamera
from gpiozero import LED

led = LED(18)

def make_picture(file_name):
    try:
        camera = PiCamera()
        camera.resolution = (600, 400)
        toggleLight(True)
        camera.capture(file_name)
        toggleLight(False)
        return True
    except Exception:
        return False

def toggleLight(self, status):
    if (status):
        led.on()
    else:
        led.off()
