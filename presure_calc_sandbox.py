print("start")
import matplotlib.pyplot as plt
import math

#--values--
t = 0               #time                               second
s = 80000               #displacement                       meter
v = 0               #velocity                           m/s
a = 0               #acceleration                       m/s^2

F_res = 0           #Resulting force                    newton 
F_grav = 0          #gravitational force                newton
temp_grad = 0

#constants
dt = 0.05                                          #change in time                          seconds

G =  6.6743 * (10 ** -11)                            #Gravitational constant                  m^3/kg/s^2

p0 = 101325                                                 #refference pressure (sea level)            Pascals
refTemp = 288.15                                            #refference temperature (sea level)         Kelvin
R_universal = 8314.32                                       #universal gas constant                     J/(mol*K)
M_nill = 28.9644                                            #molar mass of dry air                      kg/mol
g = 9.80665                                                 #Earth-surface gravitational acceleration   m/s^2
R_specific = 287.0500676                                    #gas constant of dry air

class Earth:
    m = 5.9722*10**24                               #mass of earth
    R = 6371000                                     #radius of earth

class rocket:
    m = 1000                                        #mass of rocket
    C_D = 0.5                                       #drag coefficient of rocket
    A = 10                                          #forward facing area of rocket m^2

#functions
def F_grav_calc():                                          #Gravitational force
    r = Earth.R + s
    F_grav = -1 * (G * rocket.m * Earth.m / (r ** 2))
    return F_grav

def E_kin_calc():                                           #Kinetic Energy
    E_kin = 0.5 * rocket.m * (v**2)
    return E_kin

def alt_to_p():                                             #Calculating the air pressure
    h = s * 0.001
    if h <=100 and h > 0:
        if h <= 100 and h >= 90:
            temp_grad = 4.5
        elif h < 90 and h >= 80:
            temp_grad = 0
        elif h < 80 and h >= 56:
            temp_grad = -3.54
        elif h < 56 and h >= 50:
            temp_grad = 0
        elif h < 50 and h >= 20:
            temp_grad = 1.6667
        elif h < 20 and h >= 10:
            temp_grad = 0
        elif h < 10 and h >= 0:
            temp_grad = -7
    
        #pressure calculations(barometric formula)

        if temp_grad != 0: #gotta check this part
            p = p0*((refTemp/(refTemp + temp_grad*s))**(g*M_nill/(R_universal*temp_grad)))
        else:
            p = p0*math.exp(((-g)*M_nill*s)/(R_universal*288))
    else:
        p = 0

    return p

def alt_to_T():                                             #temperature according to altitude
    h = s * 0.001
    if h > 100:
        T = 0
    elif h < 100 and h >= 90:
        T = 183 + ((h - 90) * 4.5)
    elif h < 90 and h >= 80:
        T = 183
    elif h < 80 and h >= 56:
        T = 268 + ((h - 56) * -3.54)
    elif h < 56 and h >= 50:
        T = 268
    elif h < 50 and h >= 20:
        T = 218 + ((h - 20) * 1.67)
    elif h < 20 and h >= 10:
        T = 218
    elif h < 10 and h >= 0:
        T = 288 + h * -7
    else:
        T = 288

    return T

#simulation
x = []
y = []

for n in range(100):
    F_grav = F_grav_calc()
    p = alt_to_p()
    T = alt_to_T()
    Density = p / (R_specific * T)
    F_drag = -0.5 * Density * (v**2) * rocket.C_D * rocket.A
    F_res = F_grav + F_drag
    a = F_res / rocket.m
    v = v + a * dt
    s = s + v * dt
    if s < 0:
        s = 0    

    t = t + dt

    E_kin = E_kin_calc()

    x.append(t)
    y.append(s)
    

plt.plot(x, y)
plt.xlabel('time')
plt.ylabel('altitude')

plt.title('s/t')

plt.show()

print("end")
