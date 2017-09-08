A script designed to manage your Raspberry Pi's fan according to the CPU temperature changes.

### Main
There are two different versions, the ordinary one named 'fan.py' does not support pwm feature so it can only turn on or turn off the fan.
The PWM version, which is 'fan_pwm.py', is functional with pwm adjustment.

### Problem
Both scripts works appropriately.
For the pwm version, you may have to increse its initial speed if the fan does not spin.
Based on the quality of your fan, it could make more noise when you are using the pwm version.

### Modification
You may have to modify your ordinary fan with an transistor. It can be found in some old electronic devices.
I used an '1AM' NPN transistor so the circuit could be the following diagram. If you are using a PNP transistor, the circuit may be a little different to mine.

<img src="https://github.com/xswxm/Smart_Fan_for_Raspberry_Pi/blob/master/demo.png?raw=true" 
alt="Demo" width="249" height="224" border="10" />

### Setting Up
```sh
sudo apt-get update
sudo apt-get install python python-pip
# Install requirements
sudo pip install rpi.gpio
sudo apt-get install pigpio python-pigpio
```

### How to Use (without PWM)
```sh
# Check help documents
python fan.py -h
# Run with default settings
python fan.py
# Run in the background
nohup python fan.py &
# Check CPU temperature every 2 seconds abd turn on fan on pin 24 if temperature is higher than 50 celsius
python fan.py -t 50 -i 2 -p 24
```

### How to Use (with PWM)
```sh
# Enable pigpio service
sudo pigpiod
# Check help documents
python fan_pwm.py -h
# Run with default settings
python fan_pwm.py
# Run in the background
nohup python fan_pwm.py &
# Check CPU temperature every 2 seconds abd turn on fan on pin 24 if temperature is higher than 50 celsius,
# and increse the fan speed by 10% when the temperature increses by 1 celisus
python fan_pwm.py -t 50 -i 2 -p 24 -s 10
```

License
----
MIT
