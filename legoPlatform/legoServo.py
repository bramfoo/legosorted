import logging
import math

logger = logging.getLogger(__name__)

# These are suggested defaults
SERVO_MIN = 150  # Min pulse length out of 4096
SERVO_MAX = 600  # Max pulse length out of 4096

class legoServo(object):

    def __init__(self, name, channel, center, rotation_min=SERVO_MIN, rotation_max=SERVO_MAX):
        self.name = name
        self.channel = channel
        self.center = center
        self.min = rotation_min
        self.max = rotation_max
        self.pos = None # We do not know our starting position
        logger.debug('Creating servo at channel {0} with pulse lengths between ({1}, {2})'.format(channel, rotation_min, rotation_max))

    @property
    def pos(self):
        """Position of servo"""
        return self._pos

    @pos.setter
    def pos(self, value):
        logging.debug('Servo ' + self.name + ' position now ' + str(value))
        self._pos = value

    # -90 is min, 0 is center, 90 is max
    def degreesToPulse(self, value):
        # Distinguish between pos and neg as defined center may not be halfway between min/max
        if (value < 0):
            result = int(math.ceil(self.center + (float(value)/90) * (self.center - self.min)))
            logging.debug(str(value) + ' degrees is ' + str(result) + ' PW')
            return result
        else:
            result = int(math.ceil((float(value) / 90) * (self.max - self.center) + self.center))
            logging.debug(str(value) + ' degrees is ' + str(result) + ' PW')
            return result


    def __str__(self):
        return "{0}[{1}]({2})".format(self.name, self.channel, self.pos)

    # http://stackoverflow.com/a/727779
    def __repr__(self):
        return self.__str__()
