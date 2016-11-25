import logging  # General logging
import time

from legoPlatform import legoPlatform


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
    directions = {"l":"left", "r":"right",  "u":"up", "d":"down"}

    print ('Direction options: ' + str(directions))


    while True:
        direction = raw_input('Direction? ')
        try:
            logging.info('Input \'' + str(direction) + '\'; selecting direction ' + directions[direction])
            legoPlatform.tilt(directions[direction])
            legoPlatform.recenter()
        except KeyError, e:
            print('Unknown direction ' + '\'' + str(direction) + '\'')
