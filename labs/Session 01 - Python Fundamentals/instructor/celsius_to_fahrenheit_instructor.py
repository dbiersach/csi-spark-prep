# celsius_to_fahrenheit_instructor.py

for celsius in range(-44, 109, 4):
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")
