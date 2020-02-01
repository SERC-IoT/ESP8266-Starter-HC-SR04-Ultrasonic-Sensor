# HC-SR04 Ultrasonic Distance Sensor

Code for getting started with a HC-SR04 Ultrasonic distance sensor and an ESP based development board (like Wemos D1 mini).

![sensor](assets/hc-sr04-sensor.jpg)

Detailed description of how the sensor works can be found here: https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/

<br>

![mcu breadboard and sensor](assets/wemos-d1-hc-sr04.jpg)

<br>

## Files and Folders

| File/Folder | Description |
|--- | --- |
| arduino/ | Arduino sketches |
| arduino/hc-sr04-distance-sensor/ | Arduino sketch that uses builtin functions only. |
| micropython/ | Scripts written in micropython for measuring distance. |
|  |  |

<br>

## Branches

**master**: main branch. currently not using other branches.

<br>

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/hc-sr04-sensor-circuit-diagram_schem.svg)

#### Components Needed
* HC-SR04 Ultrasonic sensor
* 330 ohm resister x2
* connecting wires
* ESP development board (e.g. Wemos D1 mini)


<br />

![breadboard diagram](assets/hc-sr04-sensor-circuit-diagram_bb.svg)

<br />

### Default Pin Wiring

| Pin No. | Function | Device Connection |
| --- | --- | --- |
| 5V | 5V | HC-SR04 VCC 5V |
| D2 | GPIO 4 (SDA) | HC-SR04 Trig |
| D1 | GPIO 5 (SCL) | HC-SR04 Echo |
| G | GND | GND |

![pin diagram](assets/Wemos-D1-Mini.png)

<br>

## References

* Arduino tutorial: https://www.instructables.com/id/Distance-Measurement-Using-HC-SR04-Via-NodeMCU/
* Arduino tutorial: https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/
* Micropython library: https://github.com/rsc1975/micropython-hcsr04
