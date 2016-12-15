from gpiozero import LED
from picamera import PiCamera

led = LED(18)  # Add some ambient light for crispier picture :-)

camera = PiCamera()
camera.resolution = (600, 400)


def make_picture(file_name):
    try:
        toggle_light(True)
        camera.capture(file_name)
        toggle_light(False)
        return True
    except Exception:
        return False


def toggle_light(status):
    led.on() if status else led.off()

if __name__ == "__main__":
    make_picture('test-image.png')
