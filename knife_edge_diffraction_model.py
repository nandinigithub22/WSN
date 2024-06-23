import numpy as np
import matplotlib.pyplot as plt

l = 1/3
d1 = 1000
d2 = 1000
h1 = 32

print("case 1")
# case 1
v1 = h1 * np.sqrt(2 * (d1 + d2) / (l * d1 * d2))
print('Fresnel diffraction parameter 1')
print(v1)

if v1 < -1:
    g1 = 0
elif -1 <= v1 <= 0:
    g1 = 20 * np.log10(0.5 - 0.62 * v1)
elif 0 <= v1 <= 1:
    g1 = 20 * np.log10(0.5 * np.exp(-0.95 * v1))
elif 1 <= v1 <= 2.4:
    g1 = 20 * np.log10(0.4 - np.sqrt(0.1184 - (0.38 - 0.1 * v1)**2))
elif v1 > 2.4:
    g1 = 20 * np.log10(0.225 / v1)

print("Gain 1 (in dB)")
print(g1)

print("case 2")
h2 = 12
# case 2
v2 = h2 * np.sqrt(2 * (d1 + d2) / (l * d1 * d2))
print("Fresnel diffraction parameter 2")
print(v2)

if v2 < -1:
    g2 = 0
elif -1 <= v2 <= 0:
    g2 = 20 * np.log10(0.5 - 0.62 * v2)
elif 0 <= v2 <= 1:
    g2 = 20 * np.log10(0.5 * np.exp(-0.95 * v2))
elif 1 <= v2 <= 2.4:
    g2 = 20 * np.log10(0.4 - np.sqrt(0.1184 - (0.38 - 0.1 * v2)**2))
elif v2 > 2.4:
    g2 = 20 * np.log10(0.225 / v2)

print("Gain 2 (in dB)")
print(g2)

print("case 3")
h3 = -13
# case 3
v3 = h3 * np.sqrt(2 * (d1 + d2) / (l * d1 * d2))
print("Fresnel diffraction parameter 3")
print(v3)

if v3 < -1:
    g3 = 0
elif -1 <= v3 <= 0:
    g3 = 20 * np.log10(0.5 - 0.62 * v3)
elif 0 <= v3 <= 1:
    g3 = 20 * np.log10(0.5 * np.exp(-0.95 * v3))
elif 1 <= v3 <= 2.4:
    g3 = 20 * np.log10(0.4 - np.sqrt(0.1184 - (0.38 - 0.1 * v3)**2))
elif v1 > 2.4:
    g3 = 20 * np.log10(0.225 / v3)

print("Gain 3 (in dB)")
print(g3)

v = np.arange(-3, 5.1, 0.1)
g = np.zeros_like(v)

for i in range(len(v)):
    if v[i] < -1:
        g[i] = 0
    elif -1 <= v[i] <= 0:
        g[i] = 20 * np.log10(0.5 - 0.62 * v[i])
    elif 0 <= v[i] <= 1:
        g[i] = 20 * np.log10(0.5 * np.exp(-0.95 * v[i]))
    elif 1 <= v[i] <= 2.4:
        g[i] = 20 * np.log10(0.4 - np.sqrt(0.1184 - (0.38 - 0.1 * v[i])**2))
    elif v[i] > 2.4:
        g[i] = 20 * np.log10(0.225 / v[i])

plt.figure()
plt.plot(v, g)
plt.title('Knife Edge Diffraction Gain')
plt.xlabel('Fresnel Diffraction Parameter')
plt.ylabel('Gain (dB)')
plt.grid(True)
plt.show()
