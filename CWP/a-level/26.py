"""Computational Physics-Newman Problem 2.6)"""
import numpy as np
import scipy,math
from sympy import symbols, solve
pi=3.14159
M=1.9891*10**30
#m=
G=6.6738*10**-11

print('Part A')
print('Part B')

l1= float(input('What is the closest orbital distance to the sun?  '))
v1=float( input('At what speed is the mass traveling?  '))
v2=symbols('v2')
v2=solve(v2**2-((2*G*M)/(v1*l1))*v2-v1**2+((2*G*M)/l1),v2)
if v2[0]>0:
  v2=v2[0]
else: v2=v2[1]
l2=int((v1*l1)/v2)
print('The aphelion is: '+str(l2)+'m')
a=int((1/2)*(l1+l2))
print('The Semi-Major Axis is:  '+str(a)+'m')
print('The Velocity at the aphelion is:  '+str(int(v2))+'(m/s)')
b=(l1*l2)**(1/2)
T=((2*pi*a*b)/(l1*v1))
print('The Orbital period is:  '+str((T/(31104000)))+'yrs.')
e=((l2-l1)/(l2+l1))
print('The eccentricity of this orbit is:  '+str((e)))










