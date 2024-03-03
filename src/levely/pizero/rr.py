import sys
import os
import RPi.GPIO as GPIO
import spidev
import logging  
import time
logging.basicConfig(level=logging.DEBUG)

# Nastavení pinů pro řadič UNL2003
IN1 = 17
IN2 = 18
IN3 = 23
IN4 = 22

# Nastavení pinů pro řadič ULN2003_2
IN5 = 16
IN6 = 7
IN7 = 5
IN8 = 6

# Nastavení režimu pinů GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)

# Funkce pro posun motoru vpravo o jeden krok
def step_forward(delay):
    GPIO.output(IN1, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN4, GPIO.LOW)

# Funkce pro posun motoru vlevo o jeden krok
def step_back(delay):
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN1, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN1, GPIO.LOW)
# Funkce pro posun motoru 2 vpravo o jeden krok
def step_forward2(delay):
    GPIO.output(IN5, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN5, GPIO.LOW)
    GPIO.output(IN6, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN8, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN8, GPIO.LOW)
# Funkce pro posun motoru 2 vlevo o jeden krok
def step_back2(delay):
    GPIO.output(IN8, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN8, GPIO.LOW)
    GPIO.output(IN7, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN6, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN5, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(IN5, GPIO.LOW)

# Hlavní program
if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG)

        # Nastavení zpoždění (minimální zpoždění pro nejvyšší rychlost motoru)
        delay = 0.002

        # Vynulování motoru
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN5, GPIO.LOW)
        GPIO.output(IN6, GPIO.LOW)
        GPIO.output(IN7, GPIO.LOW)
        GPIO.output(IN8, GPIO.LOW)
        i=0
        while i<130:
            step_forward2(delay)
            i += 1
    except KeyboardInterrupt:
        # Ukončení programu při stisku klávesy Ctrl+C
        logging.info("ctrl + c:")
        GPIO.cleanup()
