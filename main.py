#!/usr/bin/env python

import sys
import time

from weather_display import WeatherDisplay
from weather_client import WeatherClient

def main():
    model = WeatherClient(latitude='38.96656', longitude='-77.361784')
    view = WeatherDisplay()

    try:
        while True:
            model.query_weather()
            view.display(model.data)
            time.sleep(60)
    except KeyboardInterrupt:
        print("Exiting\n")
        sys.exit(0)
    return True


main()
