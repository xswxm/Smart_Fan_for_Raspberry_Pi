#!/usr/bin/python2
#coding:utf8
'''
Author: xswxm
Blog: xswxm.com

This script is designed to manage your Raspberry Pi's fan according to the CPU temperature changes.

'''

import RPi.GPIO as GPIO
import os, time

# Parse command line arguments
import argparse
parser = argparse.ArgumentParser(description='Manage your Raspberry Pi Fan intelligently!')
parser.add_argument('-i', '--interval', type=int, 
    help='The interval of each CPU temperature check (in seconds). default=5', default=5)
parser.add_argument('-p', '--pin', type=int, 
    help='Pin number of the Fan. default=24', default=24)
parser.add_argument('-t', '--temp_limit', type=int, 
    help='Fan will be turned on once the temperature is higher than this value (in celsius). default=60', default=60)
args = parser.parse_args()

interval = args.interval
pin = args.pin
temp = 0
temp_limit = args.temp_limit * 1000

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

while True:
	# Acquire CPU temperature
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
        temp = int(file.read())
    # Turn on the fan if temp is larger than the limit value
    if temp > temp_limit:
        GPIO.output(pin, GPIO.HIGH)
    # Turn off the fan if temp is smaller than the value - 2000
    elif  temp < temp_limit-5000:
        GPIO.output(pin, GPIO.LOW)
    # Sleep for few seconds
    time.sleep(interval)
