# -*- coding: utf-8 -*-
"""atividade_02_em.ipynb

*O eixo de entrada de um compressor será acionado por um redutor com engrenagens. Será utilizado um acoplamento elástico para acoplar o eixo de saída do redutor com o eixo de entrada do equipamento. O equipamento operará a **72 rpm** e necessitará da potência **29,4 kW**, de maneira continua, no seu eixo de saída. O projeto exige que o redutor transmita a potência entre dois eixos paralelos e seja alimentado por um motor elétrico de indução trifásico.*
Escolha um elemento de transmissão flexível (polia/correia ou corrente de rolos) e o dimensione considerando um fator de segurança igual a 1,8, de forma a atender as mesmas condições (rotação, torque etc.) do último par de engrenagens da atividade 1.</font>
"""

from numpy import log as ln, sqrt, sin, cos, tan, radians, pi, sqrt, ceil, arcsin
import pandas as pd

#parte do trabalho 1*****
Pe = 30000                      #W
ωp = 1180                       #rpm
ωp_conv = (1180*2*pi)/60        #rpm  escolhido no motor elétrico (entrada) - rad/s
Ps = 29400                      #W
ωc = 72                         #rpm  
ωc_conv = (72*2*pi)/60          #rpm (saída) -> rad/s
mg = 4

#parte do trabalho 2*****
ω_mot = ωp/mg                 #rpm  p/ rad/s
𝜔_mov_p = ωc                  #rpm p/ rad/s
t_trab = 12*60*16*5*52*20    
fs = 1.8
H_nom = Pe*fs
print("ω_mot =", ω_mot, "rad/s, ω_mov =", ω_mov_p, "rad/s")

"""
ESPECIFICAÇÕES PARA O SISTEMA:<br> 
 Correia Plana A – 3;<br> 
 Material: poliamida;<br> 
 Espessura, t: 3,3 mm;<br> 
 Largura: b: 250,0 mm;<br> 
 Fator de Atrito, f: 0,8;<br> 
 Peso Específico, γ: 11400 N/m³;<br> 
 Tração Permissível, Fa: 18000,0 N/m;<br> 
 Fator de Segurança, fs: 1,8;<br> 
 Fator de Serviço, Ks, para choques leves: 1,25.<br> 
 Fator de Correção de Velocidade, Cv: 1.
"""

γ = 11400
b = 0.25
t = 33*10**-3
f = 0.8
Fa = 18000
g = 9.81
Ks = 1.25
Cv = 1

"""CONSIDERAÇÕES:<br> 
 Diâmetro para polia motora, d: 110,0 mm;<br> 
 Distância entre centros, C: 650,0 mm;<br> 
 Fator de Correção de Polia, Cp: 0,7.<br> 

"""

Cp = 0.7
D_mot = 110/1000   #mm p m
D_mov = D_mot*mg   #m
DistCent = 650/1000      #mm p m
print("D_mot =", D_mot, "D_mov =", D_mov)

theta_D_mot = pi - (2*sin((D_mot-D_mov)/(2*DistCent)))
theta_D_mov = pi - (2*sin((D_mot-D_mov)/(2*DistCent)))
print("theta_D_mot =", theta_D_mot, "rad, theta_D_mov", theta_D_mov, "rad")

Lp = sqrt(4*DistCent**2 - (D_mov + D_mot)**2) + (D_mov*theta_D_mot - D_mot*theta_D_mov)/2
print ("Lp =", Lp, "m")

φ = f

V = (D_mot*pi*ω_mot)/60
print("V =", V)

ω = 12 * γ * b * t
print("Peso = ", ω, "N/m")

Fc = (ω/g)*V**2
print("Tensão centrífuga = ", Fc, "N")

#potencia de projeto
Hd = H_nom*Ks*fs
print("Hd =", Hd, "W")

T = (H_nom*Ks*fs)/(2*pi*ω_mot)
print("Torque necessário = ", T, "N.m")

#F1a - F2 = deltaF21
deltaF21 = (2*T)/D_mot
F1a = b*Fa*Cp*Cv
print("F1a - F2 =", deltaF21, "N, F1a = ", F1a, "N")

F2 = F1a - (2*T)/D_mot
print("F2 =", F2, "N")

#tração inicial necessária do sistema
Fi = (F1a + F2)/2 - Fc
print("Fi =", Fi, "N")

#evolção da fricção
fi = (1/φ)*ln((F1a-Fc)/(F2-Fc))
print("fi =", fi)

if fi < f:
  print("o prof vai ficar feliz!")
else:
  print("refaça suas contas! :c")