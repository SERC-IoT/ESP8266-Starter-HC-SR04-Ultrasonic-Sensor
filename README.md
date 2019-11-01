# HC-SR04 Ultrasonic Distance Sensor

Code for getting started with a HC-SR04 Ultrasonic distance sensor and an ESP based development board (like Wemos D1 mini).

![sensor](assets/hc-sr04-sensor.jpg)

[TODO description of how sensor works]

<br>

## Files and Folders

| File/Folder | Description |
|--- | --- |
| micropython/ | Scripts written in micropython for measuring distance. |
|  |  |

<br>

## Branches

**master**: main branch. currently not using other branches.

<br>

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/hc-sr04-sensor-circuit-diagram_schem.png)

#### Components Needed
* HC-SR04 Ultrasonic sensor
* 330 ohm resister x2
* connecting wires
* ESP development board (e.g. Wemos D1 mini)


<br />

![breadboard diagram](assets/hc-sr04-sensor-circuit-diagram_bb.png)

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

* Micropython library: https://github.com/rsc1975/micropython-hcsr04
