import numpy as np
#B2:Exercise 2.10

a_1=15.8
a_2=18.3
a_3=0.714
a_4=23.2
#Part A of this Exercise
print('Part A')
A=int(input('What is the Mass number(A):\n' ))
Z=int(input('\nWhat is the Atomic number(Z):\n' ))
#Testing even/odd on the mass number
if (A % 2) == 0:
    A_even=True
    A_odd=False
else:
    A_odd=True
    A_even=False
#Testing even/odd on the atomic number
if (Z % 2)==0:
    Z_even=True
    Z_odd=False
else:
    Z_odd=True
    Z_even=False
#Assigning the value of a_5
if A_odd==True:
    a_5=0
elif Z_even==True:
    a_5=12.0
else:
    a_5=-12.0

Be=a_1*A-a_2*A**(2/3)-a_3*(Z**2)/(A**(1/3))-a_4*((A-2*Z)**2)/A+a_5/(A**(1/2))
print('\nThe Binding Energy is: {}MeV'.format(Be))

#Part B of this Exercise
Be_A=Be/A
print('\nPart B')
print('\nThe Binding Energy per nucleon is: {}MeV'.format(Be_A))


#Part C of this Exercise
print('\nPart C-Mass where the Binding Energy is maximized for a Atomic Number')
Z=int(input('\nWhat is the Atomic number(Z):\n'))
A=np.arange(Z,3*Z+1,1)
Be_m=0
Be_mm=[]
for i in A:
#Testing even/odd on the mass number
    if (i % 2) == 0:
        i_even=True
        i_odd=False
    else:
        i_odd=True
        i_even=False
#Testing even/odd on the atomic number
    if (Z % 2)==0:
        Z_even=True
        Z_odd=False
    else:
        Z_odd=True
        Z_even=False
    #Assigning the value of a_5
    if i_odd==True:
         a_5=0
    elif Z_even==True:
         a_5=12.0
    else:
         a_5=-12.0
    Be_i=a_1*i-a_2*i**(2/3)-a_3*(Z**2)/(i**(1/3))-a_4*((i-2*Z)**2)/i+a_5/(i**(1/2))
    Be_i=(Be_i/i)
    if Be_i>Be_m:
        Be_m=Be_i
        A=i


print('\nThe maximum binding energy per nucleon is: {}MeV'.format(Be_m))
print('This occurs at the mass number: {} amu'.format(A))

#Part D of this Exercise
print('\nPart D-Finding Maximized BE for each Z-value')
Be_mz=[-100]
z=np.arange(1,101,1)
A_tm=[]

for Z2 in z:
    #Finidng the Value of A where Binding Energy is maximized
    A_z=np.arange(Z2,3*Z2+1,1)
    Be_m=0
    for i3 in A_z:
        #Testing even/odd on the mass number
        if (i3 % 2) == 0:
            i3_even=True
            i3_odd=False
        else:
            i3_odd=True
            i3_even=False
        #Testing even/odd on the atomic number
        if (Z2 % 2)==0:
            Z2_even=True
            Z2_odd=False
        else:
            Z2_odd=True
            Z2_even=False
        #Assigning the value of a_5
        if i3_odd==True:
             a_5=0
        elif Z2_even==True:
             a_5=12.0
        else:
             a_5=-12.0
        Be_i3=a_1*i3-a_2*i3**(2/3)-a_3*(Z2**2)/(i3**(1/3))-a_4*((i3-2*Z2)**2)/i3+a_5/(i3**(1/2))
        Be_i3=(Be_i3/i3)
        if Be_i3>Be_m:
            Be_m=Be_i3
            A_z=i3
#Testing even/odd on the atomic number
    if (Z2 % 2)==0:
        Z2_even=True
        Z2_odd=False
    else:
        Z2_odd=True
        Z2_even=False
    A2=np.arange(Z2,Z2*3+1,1)

    for i2 in A2:
        Be_mz=0
        if (i2 % 2)==0:
            i2_odd=False
        else:
            i2_odd=True
    #Assigning the value of a_5
        if i2_odd==True:
            a_5=0

        elif Z2_even==True:
            a_5=12.0

        else:
            a_5=-12.0

        Be_i2=a_1*i2-a_2*i2**(2/3)-a_3*(Z2**2)/(i2**(1/3))-a_4*((i2-2*Z2)**2)/i2+a_5/(i2**(1/2))
        Be_i2=(Be_i2/i2)
        Be_mm.append(Be_i2)

    #this gives the highest binding energy out of all Z-values
        if Be_i2>=max(Be_mm):
            A_m2=i2
            Zmax=Z2
    Be_max=max(Be_mm)
    print('Atomic Number: {}'.format(Z2))
    print('The Binding Energy is Maximized at a mass Value of: {} amu'.format(A_z))
    #print('The Binding Energy is a maximum at a mass of {} amu'.format(A_mz))
print('\nThe overall maximum binding energy per nucleon is: {}MeV'.format(Be_max))
print('This occurs at an atomic number of: {}'.format(Zmax))
