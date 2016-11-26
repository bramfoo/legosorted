import RPi.GPIO as gpio
import time

def spin():
    gpio.setmode(gpio.BOARD)
    gpio.setup(18, gpio.OUT)
    gpio.output(18, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(18, gpio.LOW)

if __name__ == "__main__":
    spin()
