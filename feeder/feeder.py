from gpiozero import LED
import time

# It's not really a LED, but the functionality suffices (for now)
led = LED(22)

def spin():
    led.off()
    time.sleep(0.1)
    led.on()
#    time.sleep(0.1)
    time.sleep(0.5) # (Longer for testing)
    led.off()

if __name__ == "__main__":
    spin()
