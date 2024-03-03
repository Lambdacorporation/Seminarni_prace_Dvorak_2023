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
        GPIO.cleanup()

    except KeyboardInterrupt:
        # Ukončení programu při stisku klávesy Ctrl+C
        logging.info("ctrl + c:")
        disp.clear()
        GPIO.cleanup()
