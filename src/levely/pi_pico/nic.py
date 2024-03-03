import machine
import time

# Define the pin numbers for the traffic lights
YELLOW_PIN = 1
YELLOW_PIN2 = 4
YELLOW_PIN3 = 7
YELLOW_PIN4 = 10

# Initialize the GPIO pins
yellow_led = machine.Pin(YELLOW_PIN, machine.Pin.OUT)
yellow_led2 = machine.Pin(YELLOW_PIN2, machine.Pin.OUT)
yellow_led3 = machine.Pin(YELLOW_PIN3, machine.Pin.OUT)
yellow_led4 = machine.Pin(YELLOW_PIN4, machine.Pin.OUT)

# Function to control the traffic lights
def run_traffic_lights():
        # Yellow light
        yellow_led.on()
        yellow_led2.on()
        yellow_led3.on()
        yellow_led4.on()
        time.sleep(1)  # Wait for 1 seconds

        yellow_led.off()
        yellow_led2.off()
        yellow_led3.off()
        yellow_led4.off()
        time.sleep(1)  # Wait for 1 seconds

# Run the traffic lights
while True:    
        run_traffic_lights()

