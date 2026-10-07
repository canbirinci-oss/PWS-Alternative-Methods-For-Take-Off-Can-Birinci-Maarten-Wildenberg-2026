# put the main code in here  
print('start')
import matplotlib.pyplot as plt

t = 0
dt = 0.01
v = 50
s = 0
a = 1
Area = 1
Cw = 0.98
Rspecific = 287.0500676

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

time=[]
distance=[]
for x in range(100):
  time.append(t)
  distance.append(s)
  t = t + dt
  s = s + v * dt
  v = v + a
  a = a - aLw
  aLw = Lw/m
  Lw = 0.5 * drho * Cw * Area * v**2
  T = alt_to_temp(s)
 

plt.plot(time, distance)
plt.xlabel('time(s)')
plt.ylabel('distance(m)')
plt.title('distance over time')
plt.show()

print('end')

#in dry air ;)