#!/usr/bin/env python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from datetime import datetime

class WeatherDisplay(object):
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 64
        options.cols = 64
        options.gpio_slowdown = 4
        options.brightness = 10
        options.hardware_mapping = 'adafruit-hat'
        self.matrix = RGBMatrix(options = options)

        self.white = graphics.Color(255, 255, 255)
        self.gray = graphics.Color(150, 150, 150)
        self.red = graphics.Color(255, 0, 0)
        self.blue = graphics.Color(0, 0, 255)
        self.green = graphics.Color(0, 127, 0)
        self.yellow = graphics.Color(255, 255, 0)
        self.orange = graphics.Color(255, 165, 0)
        self.purple = graphics.Color(128, 0, 128)

        self.font_h1 = graphics.Font()
        self.font_h1.LoadFont('fonts/9x18.bdf')
        self.font_h2 = graphics.Font()
        self.font_h2.LoadFont('fonts/6x10.bdf')
        self.font_h3 = graphics.Font()
        self.font_h3.LoadFont('fonts/5x7.bdf')


    def display(self, data):
        self.matrix.Clear()
        self.display_weather(data['description'], data['curr_temp'], data['low_temp'], data['high_temp'])
        self.display_aqi(data['aqi'])
        self.display_datetime(datetime.now())

    def display_weather(self, desc, curr_temp, low_temp, high_temp):
        desc = desc.capitalize()
        curr_temp = f'{round(curr_temp)}°F'
        low_temp = f'{round(low_temp)}'
        high_temp = f'{round(high_temp)}'

        graphics.DrawText(self.matrix, self.font_h2, 2, 10, self.gray, desc)
        graphics.DrawText(self.matrix, self.font_h1, 15, 40, self.white, curr_temp)
        graphics.DrawText(self.matrix, self.font_h2, 18, 51, self.red, high_temp)
        graphics.DrawText(self.matrix, self.font_h2, 35, 51, self.blue, low_temp)

    def display_aqi(self, aqi):
        color = [self.green, self.yellow, self.orange, self.red, self.purple][aqi-1]
        text = ['Good', 'Fair', 'Moderate', 'Poor', 'Very poor'][aqi-1]
        graphics.DrawText(self.matrix, self.font_h2, 2, 21, color, f'AQI: {text}')

    def display_datetime(self, dt):
        time_str = dt.strftime('%-I:%M')
        date_str = dt.strftime('%-m/%-d')
        num_chars_width = 11
        num_chars_remaining = num_chars_width - len(time_str) - len(date_str)
        time_x = 1
        date_x = time_x + 6*len(time_str) + 6*num_chars_remaining

        graphics.DrawText(self.matrix, self.font_h3, time_x, 63, self.gray, time_str)
        graphics.DrawText(self.matrix, self.font_h3, date_x, 63, self.gray, date_str)
