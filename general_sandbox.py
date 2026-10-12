#general sndbox for unwielding code 

#code for caclulating exit velocity of the earth and minimal orbital speed


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
F_grav = F_grav_calc(Grav_Const, Mass2,Dist_excl_Planet)
print("exit velocity is:",exit_velocity,"m/s")
print("Force of gravity enacted upon the spacecraft is:",F_grav,"Newtons")

def minimal_orbital_speed_calc(Grav_Const,Dist_excl_Planet):
    import math
    Mass1 = planet_earth.Mass1
    Radius_astronomical_object = planet_earth.Radius_astronomical_object
    Radius_Total = Radius_astronomical_object + Dist_excl_Planet
    minimal_orbital_speed = math.sqrt(2*Grav_Const*Mass1/Radius_Total)
    return minimal_orbital_speed
minimal_orbital_speed = minimal_orbital_speed_calc(Grav_Const,Dist_excl_Planet)

def e_kin_calc(Mass2,v):
    e_kin = 0.5*Mass2*v**2
    return e_kin

e_kin = e_kin_calc(Mass2,v)



print("minimal orbital speed is:",minimal_orbital_speed,"m/s")
print("Kinetic energy of spacecraft is:",e_kin,"Joules")