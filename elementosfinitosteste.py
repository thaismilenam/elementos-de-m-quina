from numpy import sqrt, sin, cos, tan, radians, pi, sqrt, interp, log10, log, asarray, abs
import matplotlib.pyplot as plt
import pandas as pd

W=8
R1 = 5
R2 = 1

#PARTE 1
Mf1 = 0.0
x = 0.0
for x in range(0.0, 0.015):
    V1 = R1
    def momentofletor1(x):
        return R1*(x - 0.015)
    x=x+0.01
    print(Mf1)
print(V1)


#PARTE 2
Mf2 = 0.0
x = 0.0
for x in range(0.0, 0.111):
    V2 = R1 - W
    def momentofletor1(x):
        return R1*(x-0.015) - W*(x-0.058)
    x=x+0.01
    print(Mf2);
print(V2)

#PARTE 3
Mf3 = 0
x = 0
for x in range(0, 0.128):
    V3 = R1 + R2 - W
    def momentofletor1(x):
        return R1*(x-0.015) + R2*(x-0.111) - W*(x-0.058)
    x=x+0.01
    print(Mf3);
print(V3)




### RECALCULO DOS DIAMETROS

A = 0.938
b = -25759
kts = A*1.5**b


a = 0.10655                          #raiz a
r = 0.04                             # em pol (in)
qt = 1/(1+(a/sqrt(r)))               #sensibilidade ao entalhe flexão
print("qt flexão = ", qt)
                           #fator de concentrações de tensões teórico estático - flexão
kf = 1+(qt*(kt-1))                   #fator de concentrações de tensões em fagiga dinâmico - flexão
print("kf =", kf)

a = 0.0791                           #raiz a
r = 0.01                             # em pol (in)
qt = 1/(1+(a/sqrt(r)))               #sensibilidade ao entalhe torção
print("qt torção = ", qt)
kf = 1+(qt*(kts-1))                  #fator de concentrações de tensões em fagiga dinâmico - torção
print("kf =", kf)

#diametro das seções mais solicitadas

kfs = 1 + qt*(kts-1)
kfsm = kfs
Nf = 2.5
Ma = MB
Sf = Se
Tm = 0
print("kfsm", kfsm)
d = (((32*Nf)/pi)*((kfsm*(Ma/Sf))**2+((3/4)*(kfsm*(Tm/Sy)))**2)**(1/2)**(1/3))*25.4
print("diametro do ponto B =", d)

#diametro das seções mais solicitadas

kfs = 1 + qt*(kts-1)
kfsm = kfs
Nf = 2.5
Ma = ME
Sf = Se
Tm = (Tsai/1000)*5.7101
print("kfsm", kfsm)
d = (((32*Nf)/pi)*((kfsm*(Ma/Sf))**2+((3/4)*(kfsm*(Tm/Sy)))**2)**(1/2)**(1/3))*25.4
print("diametro do ponto E =", d)

#diametro das seções mais solicitadas

kfs = 1 + qt*(kts-1)
kfsm = kfs
Nf = 2.5
Ma = MF
Sf = Se
print("kfsm", kfsm)
d = (((32*Nf)/pi)*((kfsm*(Ma/Sf))**2+((3/4)*(kfsm*(Tm/Sy)))**2)**(1/2)**(1/3))*25.4
print("diametro do ponto F =", d)


#diametro das seções mais solicitadas

kfs = 1 + qt*(kts-1)
kfsm = kfs
Nf = 2.5
Ma = MG
Sf = Se
print("kfsm", kfsm)
d = (((32*Nf)/pi)*((kfsm*(Ma/Sf))**2+((3/4)*(kfsm*(Tm/Sy)))**2)**(1/2)**(1/3))*25.4
print("diametro do ponto G =", d)

print("Ponto crítico D")

a = 0.10655                         #raiz a
r = 0.01                            # em pol (in)
qt = 1/(1+(a/sqrt(r)))              #sensibilidade ao entalhe flexão
print("qt flexão = ", qt)
kf = 1+(qt*(kt-1))                  #fator de concentrações de tensões em fagiga dinâmico - flexão
print("kf =", kf)

a = 0.0791                         #raiz a
r = 0.01                            # em pol (in)
qt = 1/(1+(a/sqrt(r)))              #sensibilidade ao entalhe torção
print("qt torção = ", qt)
kfs = 1+(qt*(kts-1))                  #fator de concentrações de tensões em fagiga dinâmico - torção
print("kf =", kf)

#diametro das seções mais solicitadas

kfs = 1 + qt*(kts-1)
kfsm = kfs
Nf = 2.5
Ma = MD
Sf = Se
print("kfsm", kfsm)
d = (((32*Nf)/pi)*((kfsm*(Ma/Sf))**2+((3/4)*(kfsm*(Tm/Sy)))**2)**(1/2)**(1/3))*25.4
print("diametro do ponto D =", d)






#pontos de interesse
""""
ponto = [0.015, 0.025, 0.058, 0.096, 0.115, 0.125, 0.13]

if ponto in range(0.015,0.058):
    def cortante1(ponto):
        return print(ponto, R1)
    
if ponto in range(0.058,0.115):
    def cortante2(ponto):
        return print(ponto, R1 - W)

if ponto in range(0.115,2.0):
    def cortante2(ponto):
        return print(ponto, R1 - W + R2)
""""