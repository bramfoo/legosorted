import logging  # General logging
import time
import Adafruit_PCA9685

from legoServo import legoServo

MOVE_DELAY = 0.01
RESET_DELAY = 0.005 # Resetting can be quicker, but not too quick to shake the whole setup
WAIT_DELAY = 0.25

logger = logging.getLogger(__name__)

class legoPlatform:

    def __init__(self):
        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)

        # Add servos
        # The defaults don't work very well
        self.servo_top = legoServo("F-B", 11, 400, 180, 640)  # Side servo (forward/back) on channel 11
        self.servo_bottom = legoServo("L-R", 15, 365, 140, 590)  # Middle servo (left/right) on channel 15
        self.servoList = [self.servo_bottom, self.servo_top]

    def addServo(self, name, channel, rotation_min, rotation_max):
        servo = legoServo(name, channel, rotation_min, rotation_max)
        self.servoList.append(servo)
        return name


    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)

    # Initialisation. Moves all servos to center, given that we may not know the starting position
    def initialise(self):
        logging.info("Initialising...")
        # Move both servos from both extremes to center. Do not rely on knowing the servo position
        for servo in self.servoList:
            self.pwm.set_pwm(servo.channel, 0, servo.center)
            # Now we should reliably be in the center
            servo.pos = servo.center

    # Helper function to move a servo to a specific direction
    def moveServo(self, servo, start, end, speed=MOVE_DELAY):
        logging.info('Moving servo {0} from position {1} to {2}'.format(servo, start, end))
        step = 5 if (end - start > 0) else -5
        for position in range(start, end, step):
            logging.debug('Moving servo {0} to position {1}'.format(servo, position))
            self.pwm.set_pwm(servo.channel, 0, position)
            time.sleep(speed)
        logging.debug('Servo ' + str(servo) + ' now at position ' + str(servo.pos))
        servo.pos = end

     # Recenter platform
    def recenter(self):
        logging.info('Recentering platform')
        for servo in self.servoList:
            self.moveServo(servo, servo.pos, servo.center, RESET_DELAY)

    # Tilt the platform in one of four directions
    def tilt(self, direction):
        logging.info('Moving platform to {}'.format(direction))

        if (direction == "left"):
            self.moveServo(self.servoList[0], self.servoList[0].pos, self.servoList[0].min)
        if (direction == "right"):
            self.moveServo(self.servoList[0], self.servoList[0].pos, self.servoList[0].max)
        if (direction == "up"):
            self.moveServo(self.servoList[1], self.servoList[1].pos, self.servoList[1].min)
        if (direction == "down"):
            self.moveServo(self.servoList[1], self.servoList[1].pos, self.servoList[1].max)
        time.sleep(WAIT_DELAY)
