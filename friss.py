# it is used when there is clear los between transmitter and receiver withing transmiting range

import numpy as np
import matplotlib.pyplot as plt

# Constants
P_t = int(input("Enter value for P_t: "))
G_t = int(input("Enter value for G_t: "))
G_r = int(input("Enter value for G_r: "))
frequency = int(input("Enter value for f: "))
c = 3e8
d = int(input("Enter value for d: "))

# Calculate wavelength
lambda_ = c / frequency
p_r = P_t * G_t * G_r * (lambda_ / (4 * np.pi * d)) ** 2


print("Received Power :" , p_r)

# Define distance range
distances = np.linspace(1, 100)

# Calculate received power using Friis transmission equation
P_r = P_t * G_t * G_r * (lambda_ / (4 * np.pi * distances)) ** 2


# Plot received power vs distance
plt.figure(figsize=(10, 6))
plt.plot(distances, P_r, label='Received Power $P_r$', color='pink')
plt.xlabel('Distance (m)')
plt.ylabel('Received Power P_r(W)')
plt.title('Received Power P_r vs Distance')
plt.grid(True, which='both', linestyle='--', linewidth=0.8)
plt.legend()
plt.show()
