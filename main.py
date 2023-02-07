#!/usr/bin/env python

import sys
import time

from weather_display import WeatherDisplay

def main():
    view = WeatherDisplay()

    try:
        while True:
            view.display()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Exiting\n")
        sys.exit(0)
    return True


main()
