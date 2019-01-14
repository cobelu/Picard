identifier_list = ["KGYI", "KDUA", "KDFW", "KLAX", "KJFK"]

PIXEL_COUNT = len(identifier_list)

print(PIXEL_COUNT)

import weather

print(weather.get_condition("KGYI"))
