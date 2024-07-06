# Two-Ray Reflection Model

The two-rays ground-reflection model is a multipath radio propagation model which predicts the path losses between a transmitting antenna and a receiving antenna when they are in line of sight (LOS). Generally, the two antenna each have different height. The received signal having two components, the LOS component and the reflection component formed predominantly by a single ground reflected wave.

# Two-Ray Reflection Model: Overview
The two-ray reflection model is a method used to predict the received power of a signal in wireless communication. It considers two primary paths for the signal to travel from the transmitter to the receiver: a direct line-of-sight path and a reflected path, typically off the ground.

# Key Components and Assumptions
Direct Path: The direct line-of-sight (LOS) path between the transmitter and receiver.
Reflected Path: The path where the signal reflects off a surface (e.g., ground) before reaching the receiver.
Reflection Coefficient (Γ): For a perfect ground, Γ=−1.

# Assumptions:
The ground is a perfect conductor.
The heights of the transmitter and receiver antennas are much smaller compared to the distance between them.
The signal frequency is high enough to consider the phase difference between the direct and reflected paths.
Mathematical Model
The received power 𝑃𝑟 is the result of combining the contributions from both the direct and reflected paths. The electric field strength at the receiver is a combination of the fields from these two paths.
Parameters 
𝑃𝑡: Transmitted power.
𝐺𝑡: Transmitter antenna gain.
𝐺𝑟: Receiver antenna gain.
𝑑: Distance between transmitter and receiver.
ℎ𝑡: Height of the transmitter antenna.
ℎ𝑟: Height of the receiver antenna.
𝑓: Frequency of the signal.
𝑐: Speed of light (approximately 3×10^8 m/s).
𝜆: Wavelength (c/f).
Received Power Calculation
The received power 
𝑃𝑟 is given by:

𝑃𝑟 = 𝑃𝑡𝐺𝑡𝐺𝑟ℎ𝑡ℎ𝑟/𝑑^4


  
