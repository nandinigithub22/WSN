import numpy as np 
import matplotlib.pyplot as plt

# Constants
P_t = 1.0
G_t = 1.0
G_r = 1.0
frequency = 2.4e9
c = 3e8
d=1

# Calculate wavelength
lambda_ = c / frequency
p_r = P_t * G_t * G_r * (lambda_ / (4 * np.pi * d)) ** 2


print("Received Power :" , p_r)

# Define distance range
distances = np.linspace(1, 10) 

# Calculate received power using Friis transmission equation
P_r = P_t * G_t * G_r * (lambda_ / (4 * np.pi * distances)) ** 2


# Plot received power vs distance
plt.figure(figsize=(10, 6))
plt.plot(distances, P_r, label='Received Power $P_r$', color='brown')
plt.xlabel('Distance (m)')
plt.ylabel('Received Power P_r(W)')
plt.title('Received Power P_r vs Distance')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
