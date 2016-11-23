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

    legoPlatform.reset()

    directions = ["left", "right", "top", "bottom"]
    for direction in directions:
        legoPlatform.tilt(direction)
        time.sleep(0.75)
        legoPlatform.reset()
        time.sleep(0.75)
