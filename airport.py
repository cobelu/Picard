# Connor Luckett
# Metar v1.0
# airport.py
# Last updated 12/30/17

import weather
import colors


class Airport:
    """An airport is located on a light strip. It has an identifier, a position on the LED strip, and a flight condition"""

    # Initialize
    def __init__(self, light_strip, identifier, position):
        self.light_strip = light_strip
        self.identifier = identifier  # Name of airport
        self.position = position  # Position of airport (LED number)
        self.condition = "NONE"  # Update color of LED after initializing airport
        self.color = colors.blue

    # Setters
    def set_condition(self):
        """Assigns current condition to airport"""
        self.condition = weather.get_condition(self.identifier)

    def set_color(self, color):
        """Sets the color of the airport"""
        self.color = color

    def update_airport(self):
        """Updates an airport condition and associated color"""
        self.set_condition()
        if self.condition == "VFR":
            self.set_color(colors.green)
        elif self.condition == "MVFR":
            self.set_color(colors.yellow)
        elif self.condition == "IFR":
            self.set_color(colors.red)
        elif self.condition == "LIFR":
            self.set_color(colors.purple)
        else:
            self.set_color(colors.blue)

    # Getters (not used)
    def get_condition(self):
        return self.condition

    def get_identifier(self):
        return self.identifier

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def to_string(self):
        return_string = str(self.identifier)
        return_string += ", Position: " + str(self.position)
        return_string += ", Condition: " + str(self.condition)
        return return_string
