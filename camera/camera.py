from gpiozero import LED

led = LED(18)


def make_picture(file_name):
    try:
        from picamera import PiCamera
        camera = PiCamera()
        camera.resolution = (600, 400)
        toggle_light(True)
        camera.capture(file_name)
        toggle_light(False)
        return True
    except Exception:
        return False


def toggle_light(status):
    led.on() if status else led.off()
