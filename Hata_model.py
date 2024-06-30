import math

f = 900 * 10**6  # Frequency in Hz
hte = 50  # Height of transmitting antenna in meters
hre = 10  # Height of receiving antenna in meters
d = 2000  # Distance in meters

# Input size and city
s = input("Enter the size (medium/large): ").strip().lower()
city = input("Enter the city type (urban/suburban/rural): ").strip().lower()

# Calculate correction factor 'a'
if s == "medium":
    a = (1.1 * math.log10(f) - 0.7) * hre - (1.5 * math.log10(f) - 0.8)
elif s == "large":
    if f <= 300 * 10**6:
        a = 8.29 * (math.log10(1.54 * hre)**2) - 1.1
    else:
        a = 3.2 * (math.log10(11.75 * hre)**2) - 4.97
else:
    raise ValueError("Invalid size input. Please enter 'medium' or 'large'.")

# Calculate median path loss 'l'
l = 69.55 + 26.16 * math.log10(f) - 13.82 * math.log10(hte) - a + (44.9 - 6.55 * math.log10(hte)) * math.log10(d)

# Calculate path loss 'p' based on city type
if city == "urban":
    p = l
elif city == "suburban":
    p = l - 2 * (math.log10(f / 28)**2) - 5.4
elif city == "rural":
    p = l - 4.78 * (math.log10(f)**2) - 18.33 * math.log10(f) - 40.98
else:
    raise ValueError("Invalid city input. Please enter 'urban', 'suburban', or 'rural'.")

# Display results
print("Median Path Loss:", p)
print("Correction Factor:", a)
