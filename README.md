A script designed to manage your Raspberry Pi's fan according to the CPU temperature changes.

### Modify your ordinary fan with an appropriate transistor
<img src="https://github.com/xswxm/Smart_Fan_for_Raspberry_Pi/blob/master/demo.png?raw=true" 
alt="Demo" width="249" height="224" border="10" />

### Setting Up
Install additional modules
```sh
sudo apt-get update
sudo apt-get install python python-pip
```

### How to Use
```sh
# Check help documents
sudo python fan.py -h
# Run with default settings
sudo python fan.py
# Check CPU temperature every 2 seconds abd turn on fan on pin 24 if temperature is higher than 50 celsius
sudo python fan.py -t 50 -i 2 -p 24
```

License
----
MIT
