# Molecular dynamics .... Detailed balance ....

from random import random
def detailedBalance(N1,beta):
    # N1 is the total number of ping-ping balls in the bin ...
    # beta is the ratio of the rates of transfer ....
    G1 = 6*10**3
    A, B = N1, 0
    pB = beta/(1+beta)
    pA = 1/(1+beta)
    tAB, tBA = pB, pA
    # probability of choosing A is pA
    # probability of choosing B is pB
    # probability of transfer from A to B is tAB
    # probability of transfer from B to A is tBA
    # the equations make sure that pA*tAB = pB*tBA
    for k in range(1,G1+1):
        choosingAtoB = random()
        if choosingAtoB <= pA:
            transferAtoB = random()
            if transferAtoB <= tAB and A>0:
                A = A - 1
                B = B + 1 
        else:
            transferBtoA = random()
            if transferBtoA <= tBA and B>0:
                A = A + 1
                B = B - 1
        print(k," trial ->",A,B)
detailedBalance(150,2)