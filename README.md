Raspberry-Pi-Programs
=====================

Programs and Files for the Raspberry Pi

-------------
## Raspberry Pi Pinouts
![Pinouts](https://raw.githubusercontent.com/zinglax/Raspberry-Pi-Programs/master/Raspberry-Pi-GPIO-pinouts.png)

-------------
## Ultrasonic Sensor 
![Ultrasoinc sensor](https://raw.githubusercontent.com/zinglax/Raspberry-Pi-Programs/master/ultrasonic_sensor.jpg)
- Use with ultrasonic.py
  - When wired properly create an instance of UltraSonicSensor to get readings

-------------
## LED wiring
![LED wiring](https://raw.githubusercontent.com/zinglax/Raspberry-Pi-Programs/master/blink_LED.jpg)
- Use with led.py
  - When wired up, create an instance of LED for on, off, and blink functionality

-------------
## Endoscope (USB)
![Endoscope](https://raw.githubusercontent.com/zinglax/Raspberry-Pi-Programs/master/waterproof_endoscope.jpg)
- Use with endoscope.py
  - Create an Endoscope object and call takepic() to get a picture 

-------------
## twitterpi.py
- uses endoscope and Twython library to take a picture when a certain hashtag is tweated
- Your twitter handle is mentioned (@YOURNAME) in the tweet along with the picture so you can see how it turned out.

-------------
## Charlieplexing LEDs
- charlieplex_led.py
- can wire n^2-n leds where n is the number of gpio pins used
![charlieplex leds](https://raw.githubusercontent.com/zinglax/Raspberry-Pi-Programs/master/charlieplex_leds.png)

-------------
## Passive Infrared Sensor
![Passive Infrared Sensor](https://raw.githubusercontent.com/zinglax/Raspberry-Pi-Programs/master/passiveinfrared_sensor_wiring.jpg)
- Use with passiveinfrared.py

-------------
## RGB LED
- Use with RGBled.py
- Controls a rgb led
