import logging

logger = logging.getLogger(__name__)

# These are good defaults
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

    def __str__(self):
        return "{0}[{1}]({2})".format(self.name, self.channel, self.pos)

    # http://stackoverflow.com/a/727779
    def __repr__(self):
        return self.__str__()
