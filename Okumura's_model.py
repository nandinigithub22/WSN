import numpy as np

# Constants and parameters
d = 5000
hte = int(input("Value of hte : " ) )
hre = int(input("Value of hre : " ) )
eirp = 100
eirp_dB = 20 * np.log10(eirp)
amu = 43
garea = 9
f = 900 * 10**6
c = 3 * 10**8
gr = 1
gr_dB = 10 * np.log10(gr)

# Calculate ghte
if 30 < hte < 1000:
    ghte = 20 * np.log10(hte / 200)
else:
    raise ValueError('Invalid hte value. hte should be between 30 and 1000.')

# Calculate ghre
if hre <= 3:
    ghre = 10 * np.log10(hre / 3)
elif 3 < hre <= 10:
    ghre = 20 * np.log10(hre / 3)
else:
    raise ValueError('Okhumara model not used for hre values greater than 10.')

# Calculate lambda and free space path loss (lf)
lamda = c / f
lf = -10 * np.log10((lamda ** 2) / (16 * np.pi * np.pi * d * d))

print("Free space path loss:", lf)

# Calculate total mean loss (l)
l = lf + amu - ghte - ghre - garea
print("Total mean loss:", l)

# Calculate median received power (p)
p = eirp_dB - l + gr_dB
print("Median received power:", p)
