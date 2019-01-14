# Connor Luckett
# Metar v1.0
# weather.py
# Last updated 12/30/17

# This file will get weather from the Aviation Weather REST API

# The list of airports will be stored here until a GUI is written

# Needed packages
import requests as r


def get_condition(airport_identifier):
    """Gets the condition of airport"""

    try:
        data = r.get("https://avwx.rest/api/metar/" + airport_identifier.lower()).json()  # All weather data
        condition = data['Flight-Rules']  # Just the condition

    # Network exceptions
    except (r.exceptions.HTTPError, r.exceptions.ConnectionError, r.exceptions.Timeout, r.exceptions.RequestException):
        condition = "NONE"
        print("Bad request. Please try again.")

    # If the airport does NOT exist
    except KeyError:
        condition = "NONE"
        print("Airport could not be found. Please try again.")

    return condition
