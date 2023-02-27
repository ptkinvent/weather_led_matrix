# Weather LED Matrix #
This project is for displaying the weather forecast and AQI data on a 64x64 LED matrix in my room. The included Python
3.7.3 code runs on a Raspberry Pi on top of the [hzeller / rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library.

## Setup ##
1. Acquire and attach the following:
    - [Raspberry Pi](https://www.adafruit.com/product/4292)
    - [64x64 RGB LED Matrix](https://www.adafruit.com/product/3649)
    - [RGB Matrix Bonnet for Raspberry Pi](https://www.adafruit.com/product/3211)
    - [5V 4A power supply](https://www.adafruit.com/product/1466)
2. Clone and install [hzeller / rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library on the Raspberry Pi.
3. Acquire an API key from OpenWeatherMap and store it as an environment variable on the Raspberry Pi called `PRIVATE_API_KEY`
4. Run `sudo python3 main.py`
