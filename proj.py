import math
import matplotlib.pyplot as plt
import numpy as np

def force(V0x,V0y,b,g=9.81):
    v = np.sqrt(V0x**2+V0y**2)
    Fx = b*v*V0x
    Fy = (b*v*V0y)+g
    return Fx,Fy

def main(vi,theta,xpos,ypos,b,N):
    #here h is our time step, we have no set domain as we are trying to
    #model the entire path, and that path not be completed in a given
    #[a.b] domain, N determines how many steps we are taking
    h = 1e-4
    x = np.zeros(N)
    y = np.zeros(N)
    #setting intial positions
    x[0] = xpos
    y[0] = ypos
    vx = vi*np.cos((np.pi*theta)/180)
    vy = vi*np.sin((np.pi*theta)/180)
    inc = 0
    #runs at i = 1 beacuse x[0] and y[0] already have data
    for i in range(1,N):
        #begin with intial force and vx and vy velocities
        #each run updates the force
        Fx,Fy = force(vx,vy,b) 
        #updating both x-y positions according to eulers method
        x[i] = x[i-1] +(vx*h)
        y[i] = y[i-1] + (vy*h)
        #obtaining new vx and vy values
        vx = vx - (Fx*h)
        vy = vy - (Fy*h)
        inc +=1 #used for time keeping and testing
        #once y is negative or 0, the program must terminate regardless
        #how many N runs there are, essentially the entire path has been modeled
        if y[i] <= 0:
            break

 


    return x,y#,inc

theta = float(input('Enter angle: '))
v = float(input('Enter velocity: '))
b = float(input('Enter damping coeff: '))
x = float(input('Enter inital x cord:'))
y = float(input('Enter inital y cord:'))


xpos,ypos = main(v,theta,x,y,b,N=100000)
print(ypos.max())
plt.plot(xpos,ypos)
plt.grid()
plt.show()