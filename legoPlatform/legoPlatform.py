import logging  # General logging
import math
import time
import itertools
import Adafruit_PCA9685

from legoServo import legoServo

MOVE_DELAY = 0.01
RESET_DELAY = 0.005 # Resetting can be quicker, but not too quick to shake the whole setup
WAIT_DELAY = 0.25

SERVO_STEP_SIZE = 5

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
            servo.pos = 0

    # Helper function to move a servo to a specific direction
    def moveServos(self, positions, speed=MOVE_DELAY):
        # For each servo, calculate the steps required
        # Let's do it in at most 50 steps for each servo
        steps = list()
        for index, position in enumerate(positions):
            servo = self.servoList[index]
            logging.info('Moving servo {0} from position {1} to {2}'.format(servo, servo.pos, position))

            start = servo.degreesToPulse(servo.pos)
            end = servo.degreesToPulse(position)
            stepSize = int(math.ceil(float(end - start)/50))
            logging.info('Servo {0} PW is from {1} to {2}'.format(servo, start, end))

            if (stepSize == 0):
                steps.append([None] * 50)
            else:
                steps.append(range(start, end + stepSize, stepSize)) # Make it an 'inclusive' list
            logging.info('Servo {0} is using {1} steps: {2}'.format(servo, len(steps[index]), steps[index]))

        # Move the servos using the generated step lists
        for item in itertools.izip_longest(*steps):
            if (item[0] != None):
                self.pwm.set_pwm(self.servoList[0].channel, 0, item[0])
            if (item[1] != None):
                self.pwm.set_pwm(self.servoList[1].channel, 0, item[1])
            time.sleep(speed)

        # Save the new positions
        for index, position in enumerate(positions):
            self.servoList[index].pos = position

     # Recenter platform
    def recenter(self):
        logging.info('Recentering platform')
        self.moveServos([0, 0], RESET_DELAY)

    # Tilt the platform in any direction, between -90 and 90 degrees
    def tilt(self, direction):
        logging.info('Moving platform to {}'.format(direction))

        if (direction == "left"):
            self.moveServos([-90, 0])
        if (direction == "right"):
            self.moveServos([90, 0])
        if (direction == "up"):
            self.moveServos([0, -90])
        if (direction == "down"):
            self.moveServos([0, 90])