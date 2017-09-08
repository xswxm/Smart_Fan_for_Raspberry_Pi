#!/usr/bin/python2
#coding:utf8
'''
Author: xswxm
Blog: xswxm.com

This script is designed to manage your Raspberry Pi's fan according to the CPU temperature changes.

'''

import pigpio
import os, time

# Parse command line arguments
import argparse
parser = argparse.ArgumentParser(description='Manage your Raspberry Pi Fan intelligently!')
parser.add_argument('-d', '--duty_cycle_init', type=int, 
  help='Initial duty cycle out of 100. default=40', default=40)
parser.add_argument('-f', '--frequency', type=int, 
  help='PWM frequency. default=50', default=50)
parser.add_argument('-i', '--interval', type=int, 
  help='The interval of each CPU temperature check (in seconds). default=5', default=5)
parser.add_argument('-p', '--pin', type=int, 
  help='Pin number of the Fan. default=24', default=24)
parser.add_argument('-s', '--step', type=float, 
  help='Speed change of the fan out of 100 percent. default=6', default=6)
parser.add_argument('-t', '--temp_limit', type=int, 
  help='Fan will be turned on once the temperature is higher than this value (in celsius). default=50', default=50)
args = parser.parse_args()

duty_cycle = 0
duty_cycle_init = args.duty_cycle_init
frequency = args.frequency
interval = args.interval
pin = args.pin
step = float(args.step)/1000
temp = 0    # Initialize temperature
temp_limit = args.temp_limit * 1000

pi = pigpio.pi()
pi.set_PWM_frequency(pin, frequency)
pi.set_PWM_range(pin, 100)    # Set range to 100

try:
  while True:
    # Acquire CPU temperature
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
      temp = int(file.read())
    # Turn on the fan if temp is larger than the limit value
    if temp > temp_limit:
      duty_cycle = duty_cycle_init+(temp-temp_limit)*step
      if duty_cycle > 100: duty_cycle = 100
    # Turn off the fan if temp is smaller than the value
    elif  temp < temp_limit:
      duty_cycle = 0
    pi.set_PWM_dutycycle(pin, duty_cycle)
    # Sleep for few seconds
    time.sleep(interval)
except KeyboardInterrupt:
  pi.set_servo_pulsewidth(pin, 0)
