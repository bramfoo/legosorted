import time
import os
import pickle
import threading
import flask
import logging
import os.path
import json
from box import box
from legoPlatform import legoPlatform
from recogniser import recogniser
from camera import camera
from flask import Flask, Response

logger = logging.getLogger(__name__)


class Magician:

    lock_file = 'magician.pickles'

    def __init__(self):
        pass

    def run(self):
        while True:
            if os.path.isfile(Magician.lock_file):
                data = pickle.load(open(Magician.lock_file, "rb"))
                color = data['color']
                shape = data['shape']

                if color is not None and shape is not None:
                    print "looking for %s %s" % (color, shape)
                    #     spin
                    #     wait
                    #     take picture
                    #     analyze picture
                    #     tilt platform
                elif color is not None:
                    print "looking for color: %s" % color
                elif shape is not None:
                    print "looking for shape: %s" % shape
                else:
                    print "no choice, sort on color"

            time.sleep(1)


if __name__ == "__main__":
    Magician().run()
