# for the force calculation function
rho = 1
Cd = 0.98
Area = 5
v = 23
def Drag_calc(rho,Cd,Area,v):
    Drag = 0.5*rho*(v**2)*Cd*Area
    return Drag

