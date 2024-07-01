import numpy as np
import matplotlib.pyplot as plt

# Parameters
pt = 50
d = 10 * 10**3
ht = int(input("Value of ht : " ) )
hr = int(input("Value of hr : " ) )
f = 900 * 10**6
c = 3 * 10**8
Eo = 10**-3
do = 1000
Ae = 0.012
Lambda = c / f

# Gain
Gt = (4 * np.pi * Ae) / (Lambda * Lambda)

# Electric field
E = (2 * Eo * do * 2 * np.pi * ht * hr) / (Lambda * d * d)

# Received Power
Pr = (pt * Gt * Gt * ht * ht * hr * hr) / (d * d * d * d)

# Path loss
if d > np.sqrt(ht * hr):
    PL = 40 * np.log10(d) - (10 * np.log10(Gt) + 10 * np.log10(Gt) + 20 * np.log10(ht) + 20 * np.log10(hr))
else:
    PL = None

# Display results
print('Lambda:', Lambda)
print('Gain:', Gt)
print('Electric field:', E)
print('Received Power:', Pr)
print('Path loss:', PL)

# Plot graphs
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Varying distance from 1m to 100km
d1 = np.arange(1, 10001, 10)
Pr1 = (pt * Gt * Gt * ht * ht * hr * hr) / (d1**4)
axs[0].plot(d1, Pr1)
axs[0].set_title('Varying distance from 1m to 100km')
axs[0].set_xlabel('Distance (m)')
axs[0].set_ylabel('Received power')

# Varying ht from 1m to 100m
ht1 = np.arange(1, 101)
Pr2 = (pt * Gt * Gt * (ht1*2) * hr * hr) / (d*4)
axs[1].plot(ht1, Pr2)
axs[1].set_title('Varying ht from 1m to 100m')
axs[1].set_xlabel('Height of transmitting antenna (m)')
axs[1].set_ylabel('Received power')

# Varying hr from 1m to 100m
hr1 = np.arange(1, 101)
Pr3 = (pt * Gt * Gt * ht * ht * (hr1*2)) / (d*4)
axs[2].plot(hr1, Pr3)
axs[2].set_title('Varying hr from 1m to 100m')
axs[2].set_xlabel('Height of receiving antenna (m)')
axs[2].set_ylabel('Received power')

plt.tight_layout()
plt.show()
