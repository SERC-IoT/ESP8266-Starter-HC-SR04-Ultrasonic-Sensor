# micropython script that measures distance in mm.
import utime
import hcsr04

# define pins
TRIGGER_PIN = const(4)
ECHO_PIN = const(5)

# setup sensor
sensor = hcsr04.HCSR04(TRIGGER_PIN, ECHO_PIN)

while True:
    distance = sensor.distance_mm()
    print("Distance: {:.1f} mm".format(distance), end='\r')
    utime.sleep_ms(500)
