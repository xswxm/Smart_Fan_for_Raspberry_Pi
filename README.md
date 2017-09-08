A script designed to manage your Raspberry Pi's fan according to the CPU temperature changes.

### Main
There are two different versions, the ordinary one named 'fan.py' does not support pwm feature so it can only turn on or turn off the fan.
The PWM version, which is 'fan_pwm.py', is functional with pwm adjustment.

### Problem
Both scripts works appropriately.
For the pwm version, you may have to increse its initial speed if the fan does not spin.
Based on the quality of your fan, it could make more noise when you are using the pwm version.

### Modify your ordinary fan with an appropriate transistor
<img src="https://github.com/xswxm/Smart_Fan_for_Raspberry_Pi/blob/master/demo.png?raw=true" 
alt="Demo" width="249" height="224" border="10" />

### Setting Up
Install additional modules
```sh
sudo apt-get update
sudo apt-get install python python-pip
# Install requirements
sudo apt-get install RPi.GPIO, pigpio
```

### How to Use (without PWM)
```sh
# Check help documents
sudo python fan.py -h
# Run with default settings
sudo python fan.py
# Run in the background
sudo nohup python fan.py &
# Check CPU temperature every 2 seconds abd turn on fan on pin 24 if temperature is higher than 50 celsius
sudo python fan.py -t 50 -i 2 -p 24
```

### How to Use (with PWM)
```sh
# Check help documents
sudo python fan_pwm.py -h
# Run with default settings
sudo python fan_pwm.py
# Run in the background
sudo nohup python fan_pwm.py &
# Check CPU temperature every 2 seconds abd turn on fan on pin 24 if temperature is higher than 50 celsius,
# and increse the fan speed by 10% when the temperature increses by 1 celisus
sudo python fan_pwm.py -t 50 -i 2 -p 24 -s 10
```

License
----
MIT
