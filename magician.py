import time
import os
import pickle
import logging
import os.path
import feeder.feeder
import camera.camera
from box import box
from recogniser import recogniser, point
from legoPlatform import legoPlatform
from camera import camera

logger = logging.getLogger(__name__)


class Magician:

    top_left = point.Point(110, 45)
    lower_right = point.Point(430, 340)
    lock_file = 'magician.pickles'
    image_file = 'picture.png'

    def __init__(self):
        self.box = box.Box()
        self.platform = legoPlatform.legoPlatform()
        self.platform.initialise()

    def run(self):
        while True:
            if os.path.isfile(Magician.lock_file):

                feeder.feeder.spin()
                time.sleep(3)
                camera.make_picture(Magician.image_file)
                lego_block = None

                try:
                    lego_block = recogniser.find_single_block(Magician.image_file, Magician.top_left, Magician.lower_right)
                except Exception:
                    # Probably 2 blocks
                    self.platform.tilt(box.Box.garbage_direction)

                print "lego_block=%s" % lego_block

                if lego_block is not None:
                    data = pickle.load(open(Magician.lock_file, "rb"))
                    color = data['color']
                    shape = data['shape']
                    dimension = data['dimension']
                    sort = data['sort']

                    self.box.set_preferences(color, shape, dimension, sort)
                    direction = self.box.offer(lego_block)
                    self.platform.tilt(direction)
                    time.sleep(0.5)
                    self.platform.recenter()
            else:
                self.box.reset()
                self.platform.recenter()

            time.sleep(1)


if __name__ == "__main__":
    Magician().run()
