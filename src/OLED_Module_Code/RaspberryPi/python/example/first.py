import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import RPi.GPIO as GPIO
import spidev
import logging  
import time
import traceback
from waveshare_OLED import OLED_1in5_rgb
from PIL import Image,ImageDraw,ImageFont
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

# Inicializace OLED displeje
def init_display():
    disp = OLED_1in5_rgb.OLED_1in5_rgb()
    disp.Init()
    disp.clear()
    return disp

# Zobrazení obrázku na OLED displeji
def show_image(disp):
    try:
        picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
        hpk = Image.open(os.path.join(picdir, 'hpk.bmp'))
        Himage = Image.new('RGB', (disp.width, disp.height), 0)
        Himage.paste(hpk, (0, 0))
        Himage = Himage.rotate(0)
        disp.ShowImage(disp.getbuffer(Himage))
    except Exception as e:
        logging.error(e)

# Hlavní program
if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG)

        # Nastavení zpoždění (minimální zpoždění pro nejvyšší rychlost motoru)
        delay = 0.002

        # Inicializace OLED displeje
        disp = init_display()

        # Zobrazení obrázku na OLED displeji
        show_image(disp)

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
        while i<1000:
            step_forward(delay)
            i += 1
        i=0
        while i<140:
            step_back2(delay)
            i += 1
        i=0
        while i<1000:
            step_forward(delay)
            i += 1
        i=0
        while i<1000:
            step_back(delay)
            i += 1
        i=0
        while i<140:
            step_forward2(delay)
            i += 1
        i=0
        while i<1500:
            step_back(delay)
            i += 1
        i=0
        #while i<120:
        #    step_back2(delay)
        #    i += 1
        #i=0
        disp.clear()
        GPIO.cleanup()
    except KeyboardInterrupt:
        # Ukončení programu při stisku klávesy Ctrl+C
        logging.info("ctrl + c:")
        disp.clear()
        GPIO.cleanup()
