import numpy as np
import statistics as sta


# Atividade 1
# media, mediana, moda, variancia e desvio padrão no Python
n = [18,21,24,29,30,32,40,49,50,56]
mediana = np.median(n)
media = np.mean(n)
moda = sta.mode(n)
var = np.var(n)
DP = np.std(n)
print(f"mediana = {mediana:.2f}")
print(f"media = {media:.2f}")
print(f"moda = {moda:.2f}")
print(f"variancia = {var:.2f}")
print(f"DP = {DP:.2f}")



# Atividade 2
# Pergunte a quantidade de números que um usuario quer
# calcular a média e o desvio padrão
lista = []
n = int(input("Quantos números tem a amostra? "))
for i in range(n):
  numero = float(input(f"Digite o {i+1} número "))
  lista.append(numero)
media = np.mean(lista)
DP = np.std(lista)
print(f"A media = {media}")
print(f"O DP = {DP:.4f}")



# Atleta A: 148 cm 170 cm 155 cm 131 cm
# Atleta B: 145 cm 151 cm 150 cm 152 cm
# Atleta C: 146 cm 151 cm 143 cm 160 cm

# a) Qual deles obteve melhor média
# b) Qual deles foi o mais regular
A = [148,170,155,131]
B = [145,151,150,152]
C = [146,151,143,160]
mediaA = np.mean(A)
mediaB = np.mean(B)
mediaC = np.mean(C)
print(f"media A = {mediaA}")
print(f"media B = {mediaB}")
print(f"media C = {mediaC}")
M = [mediaA,mediaB,mediaC]
maior = max(M)
print(maior)
DPA = np.std(A)
DPB = np.std(B)
DPC = np.std(C)
print(f"DP A = {DPA:.2f}")
print(f"DP B = {DPB:.2f}")
print(f"DP C = {DPC:.2f}")
ME = [DPA,DPB,DPC]
minimo = min(ME)
print(f"O menor desvio padrão = {minimo:.2f}")
