# Example to demonstrate LED fade in and out using the Pi5Neo class
# Author: Jacque Wilson
# Organization: Ohana Codes
# Date: 3 Oct 2024

import time
from pi5neo import Pi5Neo

# Initialize Pi5Neo with 10 LEDs
neo = Pi5Neo('/dev/spidev0.0', 10, 800)

def fade_in_out(neo, led_index, color, steps=50, delay=0.05):
    """
    Fade an LED in and out repeatedly.

    Parameters:
    - neo: The Pi5Neo instance.
    - led_index: Index of the LED to fade.
    - color: RGB tuple of the color to fade (R, G, B).
    - steps: Number of steps in the fade transition.
    - delay: Delay between each step (in seconds).
    """
    try:
        while True:
            # Fade in (from off to specified color)
            neo.fade_led(led_index, (0, 0, 0), color, steps, delay)

            # Fade out (from specified color to off)
            neo.fade_led(led_index, color, (0, 0, 0), steps, delay)
    
    except KeyboardInterrupt:
        # Turn off the LEDs on exit
        neo.clear_strip()
        neo.update_strip()

# Set up color to fade (e.g., blue)
color = (0, 0, 255)

# Fade the 3rd LED (index 2) in and out continuously
fade_in_out(neo, 2, color, steps=100, delay=0.02)
