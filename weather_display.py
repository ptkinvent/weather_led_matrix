#!/usr/bin/env python

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image


class WeatherDisplay(object):
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 64
        options.cols = 64
        options.gpio_slowdown = 4
        options.brightness = 10
        options.hardware_mapping = 'adafruit-hat'
        self.matrix = RGBMatrix(options = options)


    def display(self):
        image_file = '/home/pi/Pictures/cat.png'
        image = Image.open(image_file)
        image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
        self.matrix.SetImage(image.convert('RGB'))
