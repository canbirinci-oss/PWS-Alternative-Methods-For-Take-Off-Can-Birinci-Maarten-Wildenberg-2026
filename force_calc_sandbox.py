# for the force calculation function
# start of code concerning Speed calculations 
m = float(input("Input mass of craft in kg:"))
dt = float(input("Input dt in seconds:"))
v = 1 # plug in the code for the calculations of exit velocity of the earth and minimal orbital speed @general_sandbox
a= F/m
v = v + a
p = m*v

t = t + dt
s = s + v * dt

s = float(input("Input distance between spacecraft and planet surface in m:"))
Grav_Const = 6.6743*10**(-11)
Mass2 = float(input("Enter mass of spacecraft in kg:"))
Radius_Spacecraft = float(input("Input radius of Spacecraft in m:"))
Dist_excl_Planet = Radius_Spacecraft + s
class class_Planet_Earth:
    Mass1 = (5.9722*10**24)
    Radius_astronomical_object = 6371000 #in meters, right now I'm using the average, but later on we could also code the oblate spheroid

planet_earth = class_Planet_Earth

def exit_velocity_calc(Grav_Const): #at the moment this if only for Earth
    import math
    Mass1 = planet_earth.Mass1
    Radius_astronomical_object = planet_earth.Radius_astronomical_object
    exit_velocity = math.sqrt((2*Grav_Const*Mass1)/Radius_astronomical_object)
    return exit_velocity
exit_velocity = exit_velocity_calc(Grav_Const)

def F_grav_calc(Grav_Const, Mass2,Dist_excl_Planet): #at the moment this if only for Earth
    Mass1 = planet_earth.Mass1
    Radius_astronomical_object = planet_earth.Radius_astronomical_object
    Radius_Total = Radius_astronomical_object + Dist_excl_Planet
    F_grav = Grav_Const*Mass1*Mass2/(Radius_Total**2)
    return F_grav

# start of code concerning Drag calculations 
Cd = 0.98
Area = 5
v = 23
s = -50
  
def TempGrad_calc(s): # The Temperature Gradient calculation function. 
    h = s * 0.001
    if h <= 100 and h >= 90:
        TempGrad = 4.5
    elif h < 90 and h >= 80:
        TempGrad = 0
    elif h < 80 and h >= 56:
        TempGrad = -3.54
    elif h < 56 and h >= 50:
        TempGrad = 0
    elif h < 50 and h >= 20:
        TempGrad = 1.6667
    elif h < 20 and h >= 10:
        TempGrad = 0
    elif h < 10 and h >= 0:
        TempGrad = -7
    elif h < 0 :
        print("You're going the wrong way. You're supposed to go UP, NOT DOWN!!!")
        print("We're trying to reach orbit, not an early grave!!!! ")
    else:
        TempGrad = None
    return TempGrad



def Pressure_calc(TempGrad, s): # The Pressure calculation function.
    import math
    Pb = 101325 #Pascals
    refTemp = 288 #Kelvin (at sea level)
    #TempGrad return from TempGrad_calc()
    #h (height) return from main branch
    R_gas = 8314.32 #J/(mol*K)
    M_nill = 28.9644 #kg/mol
    G_nill = 9.80665 #m/s^2
    if TempGrad == 0: #gotta check this part
        Pressure = Pb*((refTemp/(refTemp + TempGrad*s))**(G_nill*M_nill/(R_gas*TempGrad)))
    else:
        Pressure = Pb*math.exp(((-G_nill)*M_nill*s)/(R_gas*TempGrad))
    return Pressure

def alt_to_temp(s):
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
    return(T)

TempGrad = TempGrad_calc(s)
T = alt_to_temp(s)
Pressure = Pressure_calc(TempGrad, s)

def Air_Density_calc(T,Pressure):
    rho = Pressure/(T*287.0500676) # 287.0500676 J/(kg*K) is the specific gas constant for dry air
    return rho

def Drag_calc(rho,Cd,Area,v):
    Drag = 0.5*rho*(v**2)*Cd*Area
    return Drag

