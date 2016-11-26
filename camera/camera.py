def make_picture(file_name):
    try:
        from picamera import PiCamera
        camera = PiCamera()
        camera.resolution = (600, 400)
        camera.capture(file_name)
        return True
    except Exception:
        return False
