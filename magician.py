import time
import os
import pickle
import threading
import flask
import logging
import os.path
import json
import feeder.feeder
import camera.camera
from box import box
from recogniser import recogniser, point
from legoPlatform import legoPlatform, direction
from recogniser import recogniser
from camera import camera
from flask import Flask, Response

logger = logging.getLogger(__name__)


class Magician:

    top_left = point.Point(110, 45)
    lower_right = point.Point(430, 340)
    lock_file = 'magician.pickles'
    image_file = 'picture.png'

    def __init__(self):
        self.box = box.Box()
        self.platform = legoPlatform.legoPlatform()

    def run(self):
        while True:
            if os.path.isfile(Magician.lock_file):

                feeder.feeder.spin()
                time.sleep(3)
                camera.make_picture(Magician.image_file)
                lego_block = recogniser.find_single_block(Magician.image_file, Magician.top_left, Magician.lower_right)

                if lego_block is not None:
                    data = pickle.load(open(Magician.lock_file, "rb"))
                    color = data['color']
                    shape = data['shape']

                    if color is not None and shape is not None:
                        print "looking for %s %s" % (color, shape)
                    elif color is not None:
                        print "looking for color: %s" % color
                    elif shape is not None:
                        print "looking for shape: %s" % shape
                    else:
                        print "no choice, sort on color"

                    # TODO self.platform.tilt(direction.Direction.left)
            else:
                self.box.reset()

            time.sleep(1)


if __name__ == "__main__":
    Magician().run()
