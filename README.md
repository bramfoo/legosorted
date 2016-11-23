# Lego. Sorted!

## What does it do?

It sorts Lego. At least, that's the idea :-)

It uses computer vision to analyse the brick(s) in front of the camera. Based on [size|shape|colour] it then tilts a platform driven by a two servos to drop it into the right box.

## Build/Run

```
$ git clone https://github.com/bramfoo/LegoSorted.git
$ pip install adafruit-pca9685 picamera
...
```

## To Do

The roadmap is as follows:

* ...

## Parts
* Raspberry Pi 3
* Raspberry Pi camera
* [Makeblock pan-tilt kit](http://www.makeblock.com/mini-pan-tilt-kit)
* [Adafruit 6-Channel 12-bit PWM/Servo Driver](https://www.adafruit.com/products/815)

## Dependencies
* [picamera](https://pypi.python.org/pypi/picamera)
* [Adafruit PCA9685 library](https://github.com/adafruit/Adafruit_Python_PCA9685.git), Python library to drive servos connected to the Adafruit 16-channel PWM board
* [OpenCV](http://opencv.org/)

## Links
The following sources of information were used/helpful

* [Adafruit 16-channel PWM instructions](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/), simple instructions on how to connect/use the PWM board
* [PiCamera docs](https://picamera.readthedocs.io/en/release-1.12/index.html), the PiCamera documentation
