import logging  # General logging
import time
import Adafruit_PCA9685

from legoServo import legoServo

delay_period = 0.01
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

    # Returns all servos given to the center position
    def reset(self):
        logging.info('Resetting servo(s) {0} to center position'.format(self.servoList))
        for servo in self.servoList:
            self.pwm.set_pwm(servo.channel, 0, servo.center)


    # Helper function to move a servo to a specific direction
    def moveServo(self, servo, start, end):
        logging.info('Moving servo {0} from position {1} to {2}'.format(servo, start, end))
        step = 5 if (end - start > 0) else -5
        for position in range(start, end, step):
            logging.debug('Moving servo {0} to position {1}'.format(servo, position))
            self.pwm.set_pwm(servo.channel, 0, position)
            time.sleep(delay_period)


    # Tilt the platform in one of four directions
    def tilt(self, direction):
        logging.info('Moving platform to {}'.format(direction))

        # FIXME: assumption here is that the servo is always centered. Perhaps the servo should keep track of it's location?
        if (direction == "left"):
            self.moveServo(self.servoList[0], self.servoList[0].center, self.servoList[0].min)
        if (direction == "right"):
            self.moveServo(self.servoList[0], self.servoList[0].center, self.servoList[0].max)
        if (direction == "top"):
            self.moveServo(self.servoList[1], self.servoList[1].center, self.servoList[1].min)
        if (direction == "bottom"):
            self.moveServo(self.servoList[1], self.servoList[1].center, self.servoList[1].max)
