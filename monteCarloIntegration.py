# Here I am implementing the Monte Carlo integration ...

# This function takes the integrand f (f:R x R->R), the constants c0, Lx, Ly
# and computes the area of the region {(x,y) : 
# -Lx<x<Lx, -Ly<y<Ly, f(x,y)<c0} ....

from random import random

def monteCarloIntegration(f,c, Lx, Ly):
    Nint, Ntotal = 0, 0
    area1, area2 = 0, 1
    while abs(area2-area1)>=10**(-6):
        offsetX = 2*Lx*random()
        offsetY = 2*Ly*random()
        Ntotal = Ntotal + 1
        area1 = 4*Lx*Ly*Nint/Ntotal
        flag = f(offsetX-Lx, offsetY-Ly) < c
        if flag:
            Nint = Nint + 1
            area2 = 4*Lx*Ly*Nint/Ntotal
    return area2

def circle(x, y): return x**2+y**2
pi = 3.141592
print("x**2+y**2<1")
for k in range(10,0,-1):
    # I am seeing how close I can get to pi = 3.141592....
    print(-k,"< x,y <",k,monteCarloIntegration(circle,1,k,k),pi)
print()
print("|x|+|y|<1")
def diamond(x,y): return abs(x)+abs(y)
for k in range(10,0,-1):
    # I am seeing how close I can get to the actual answer = 2
    print(-k,"< x,y <",k,monteCarloIntegration(diamond,1,k,k),2)
# some arbitrary shape
def someShape(x,y): return abs(x**5)+abs(y**7*x**2) + abs(2*x)
print()
print("Let us see what happens to an arbitrary shape as such")
for k in range(10,0,-1):
    print(-k,"< x,y <",k,monteCarloIntegration(someShape,5,k,k))

# Area decreases below a certain stencil (i.e. grid size)
# So I am writing a function below which automatically figures out
# this grid size ....

def adaptiveMCintegration(f,c):
    Lx, Ly = 10*c, 10*c
    N1 =  0
    A2, A3, A4 = 0, 0, 0
    while True:
        N1 = N1 + 1
        area = monteCarloIntegration(f,c,Lx,Ly)
        Lx = Lx - 0.01*c
        Ly = Ly - 0.01*c
        if N1 == 1: A1 = area
        elif N1 == 2:
            A2 = A1
            A1 = area
        elif N1 == 3:
            A3 = A2
            A2 = A1
            A1 = area
        else:
            A4 = A3
            A3 = A2
            A2 = A1
            A1 = area
            if A4>A3 and A3>A2 and A2>A1: break   
    return A4

print("Diamond area using Monte Carlo integration ....")
print(adaptiveMCintegration(diamond,4)) 