import logging

logger = logging.getLogger(__name__)

# These are good defaults
SERVO_MIN = 150  # Min pulse length out of 4096
SERVO_MAX = 600  # Max pulse length out of 4096

class legoServo:

    def __init__(self, name, channel, rotation_min=SERVO_MIN, rotation_max=SERVO_MAX):
        self.name = name
        self.channel = channel
        self.min = rotation_min
        self.max = rotation_max
        self.center = (rotation_min + rotation_max)/2
        logger.debug('Creating servo at channel {0} with pulse lengths between ({1}, {2})'.format(channel, rotation_min, rotation_max))

    def __str__(self):
        return "{0}[{1}]".format(self.name, self.channel)

    # http://stackoverflow.com/a/727779
    def __repr__(self):
        return self.__str__()
