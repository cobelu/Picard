# Picard
Pi Aviation Conditions Indicator

## About
The Pi Aviation Conditions Indicator (Picard) is a python program written for the Raspberry Pi by Connor Luckett. It displays aviation METAR data through a series of WS2801 LEDs. Remember, METARs are hourly weather updates and do not always accurately represent flying conditions. It is the pilot-in-command’s ultimate responsibility to judge if weather is suitable before taking-off.

Picard utilizes the Aviation Weather REST API from Michael duPont and Adafruit libraries. Please support both for their wonderful open-source code.

## Preparation
Picard calls on several packages which will need to be installed. This can be done by executing a few commands in the terminal:
*	sudo pip install adafruit-pureio
*	sudo pip install adafruit-gpio
*	sudo pip install adafruit-ws2801

After installation and joining a wireless network, the program will be ready to run.

## Wiring
The setup will require an external power supply. I used a 5v, 2A unit [1]. A screwed terminal block DC connector [2] will suffice for the prototyping stage. You will of course need a string of WS2801s [3], which can be separated or joined to the length desired. Each light will draw a maximum of 60 mA, so make sure to use a power supply which can support the total current drawn.

<Picture>

Do NOT forget to ground the Pi to the LED strip. The wiring is as follows:

## Notes
The program will run indefinitely until the power is cut or the program is terminated by pressing Ctrl + C. During initialization, all LEDs will show light blue. As data is fetched the LEDs are updated. The program updates every so often so as not to overload the API. Once updated, the update will be displayed on the console, and the color of the individual LED will change to match the condition:
*	VFR -> Green
*	MVFR -> Yellow
*	IFR -> Red
*	LIFR -> Purple
*	Request failure -> Blue

1. https://www.adafruit.com/product/276
2. https://www.adafruit.com/product/368 
3. https://www.amazon.com/WS2801-Individually-Addressable-Digital-Non-waterproof/dp/B0192VUDNG/ref=sr_1_1?s=apparel&ie=UTF8&qid=1515374206&sr=8-1&keywords=WS2801 
4. https://tutorials-raspberrypi.de/wp-content/uploads/2016/10/Raspberry-Pi-WS2801B-RGB-LED-Stripe-Schaltplatine.png
