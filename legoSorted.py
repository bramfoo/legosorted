import logging  # General logging
import time

from legoPlatform.legoPlatform import legoPlatform
from legoPlatform.direction import Direction


# General config
logFile = "lego.log"

########
### MAIN
########
if __name__=="__main__":
    # Log file for reference
    logging.basicConfig(filename=logFile, filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Logging started...')

    # Create the platform
    legoPlatform = legoPlatform()

    legoPlatform.initialise()

    directions = {'l':Direction.left, 'r':Direction.right, 'u':Direction.up, 'd':Direction.down, 'lu':Direction.left_up, 'ld':Direction.left_down, 'ru': Direction.right_up, 'rd':Direction.right_down}

    print ('Direction options: ' + str([e.name for e in directions.values()]))

    while True:
        direction = raw_input('Direction? ')
        try:
            logging.info('Input \'' + str(direction) + '\'; selecting direction ' + str(directions[direction]))
            legoPlatform.tilt(directions[direction])
            time.sleep(0.5)
            legoPlatform.recenter()
        except KeyError, e:
            print('Unknown direction ' + '\'' + str(direction) + '\'')
