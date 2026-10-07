#for the pressure calculation function
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


def Air_Density_calc(T,Pressure):
    rho = Pressure/(T*287.0500676) # 287.0500676 J/(kg*K) is the specific gas constant for dry air
    return rho

