The knife-edge diffraction model is a classical method used in wireless communication to estimate signal attenuation caused by an obstacle, such as a building or a hill, which obstructs the direct line-of-sight path between the transmitter and receiver. This model approximates the obstacle as a "knife-edge" to simplify the complex problem of diffraction.

Key Concepts
Fresnel Zones: These are ellipsoidal regions around the line-of-sight path that define where diffraction and interference effects are significant. The first Fresnel zone is the most important for understanding diffraction.

Fresnel-Kirchhoff Diffraction Parameter (
𝑣
v): This parameter is a measure of the diffraction loss and is defined as:

𝑣
=
ℎ
2
(
𝑑
1
+
𝑑
2
)
𝜆
𝑑
1
𝑑
2
v= 
λ 
d 
1
​
 d 
2
​
 
​
 
h 
2(d 
1
​
 +d 
2
​
 )
​
 
​
 
ℎ
h: Height of the obstacle above the line-of-sight path.
𝑑
1
d 
1
​
 : Distance from the transmitter to the obstacle.
𝑑
2
d 
2
​
 : Distance from the obstacle to the receiver.
𝜆
λ: Wavelength of the signal.
Diffraction Loss: The signal loss due to diffraction can be estimated using the Fresnel-Kirchhoff diffraction parameter. The loss increases with higher values of 
𝑣
v.

Knife-Edge Diffraction Model
Calculating Diffraction Parameter 
𝑣
v
Determine the Geometry:

Identify the distances 
𝑑
1
d 
1
​
  and 
𝑑
2
d 
2
​
 .
Measure the height 
ℎ
h of the obstacle relative to the line-of-sight path.
Calculate the wavelength 
𝜆
=
𝑐
𝑓
λ= 
f
c
​
 , where 
𝑐
c is the speed of light and 
𝑓
f is the frequency of the signal.
Compute 
𝑣
v:

𝑣
=
ℎ
2
(
𝑑
1
+
𝑑
2
)
𝜆
𝑑
1
𝑑
2
v= 
λ 
d 
1
​
 d 
2
​
 
​
 
h 
2(d 
1
​
 +d 
2
​
 )
​
 
​
 
Calculating Diffraction Loss
The diffraction loss can be estimated using the Fresnel diffraction parameter 
𝑣
v. The loss function 
𝐹
(
𝑣
)
F(v) can be approximated from empirical data or using mathematical approximations such as:

Approximate Loss Function:

𝐿
(
𝑑
𝐵
)
=
6.9
+
20
log
⁡
10
(
(
𝑣
−
0.1
)
2
+
1
+
𝑣
−
0.1
)
L(dB)=6.9+20log 
10
​
 ( 
(v−0.1) 
2
 +1
​
 +v−0.1)
This formula provides a good approximation of the diffraction loss for 
𝑣
≥
0
v≥0.

