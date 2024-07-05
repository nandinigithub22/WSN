The knife-edge diffraction model is a classical method used in wireless communication to estimate signal attenuation caused by an obstacle, such as a building or a hill, which obstructs the direct line-of-sight path between the transmitter and receiver. This model approximates the obstacle as a "knife-edge" to simplify the complex problem of diffraction.

Key Concepts
Fresnel Zones: These are ellipsoidal regions around the line-of-sight path that define where diffraction and interference effects are significant. The first Fresnel zone is the most important for understanding diffraction.

Fresnel-Kirchhoff Diffraction Parameter (
𝑣
v): This parameter is a measure of the diffraction loss and is defined as:

![image](https://github.com/nandinigithub22/WSN/assets/172033432/bc7d32e6-f574-4844-be29-3250c702b97d)

h: Height of the obstacle above the line-of-sight path.
𝑑1 : Distance from the transmitter to the obstacle.
𝑑2 : Distance from the obstacle to the receiver.
𝜆 : Wavelength of the signal.
Diffraction Loss: The signal loss due to diffraction can be estimated using the Fresnel-Kirchhoff diffraction parameter. The loss increases with higher values of 𝑣.

Knife-Edge Diffraction Model
Calculating Diffraction Parameter 𝑣
Determine the Geometry:

Identify the distances 𝑑1 and 𝑑2.
Measure the height ℎ of the obstacle relative to the line-of-sight path.
Calculate the wavelength 
![image](https://github.com/nandinigithub22/WSN/assets/172033432/9cd5a52a-3054-4302-97ed-b569949edc49)

, where 
𝑐 is the speed of light and 
𝑓 is the frequency of the signal.
Compute 𝑣:

![image](https://github.com/nandinigithub22/WSN/assets/172033432/b01bc973-a3f2-4f47-a15a-8c59d7f5233f)

Calculating Diffraction Loss
The diffraction loss can be estimated using the Fresnel diffraction parameter 
F(v) can be approximated from empirical data or using mathematical approximations such as:

Approximate Loss Function:

![image](https://github.com/nandinigithub22/WSN/assets/172033432/599490d0-19c5-4223-a9a7-e2db91f683bc)

This formula provides a good approximation of the diffraction loss for 𝑣≥0.

