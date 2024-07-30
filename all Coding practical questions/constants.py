# constants.py 

# Mathematical Constants
pi = 3.141592653589793
e = 2.718281828459045

# Physical Constants (in SI units)
speed_of_light = 299792458  # m/s
gravitational_constant = 6.67430e-11  # m^3 kg^-1 s^-2 
planck_constant = 6.62607015e-34  # J s

# ... add more constants as needed ...

import constants

# Access constants using dot notation
circumference = 2 * constants.pi * 5 
print(f"Circumference: {circumference:.2f}")

energy = constants.planck_constant * 5e14  # Frequency in Hz 
print(f"Energy: {energy:.2e} J")