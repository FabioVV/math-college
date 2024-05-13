import matplotlib.pyplot as plt 
import numpy as np

idade = [30,31,34,34,37,37,42,42,45,45,46,46,48,50,52,54,54,54,80]

q1 = np.percentile(idade, 25, method="midpoint")
q3 = np.percentile(idade, 75, method="midpoint")

max = max(idade)
min = min(idade)

I = q3 + q1

mediana = np.median(idade)

# LI - LIMITE INFERIOR
# LS - LIMITE SUPERIOR
LI = q1 - 1.5 * I
LS = q3 + 1.5 * I
outlier = []

for i in range(len(idade)):
    if idade[i] > LS or idade[i] < LI:
        outlier.append(idade[i])

print(f"os outlier são {outlier}")
print(f"Q1 {q1}")
print(f"Q2 {q3}")
print(f"MÁXIMO =  {LS}")
print(f"MÍNIMO =  {LI}")
print(f"MEDIANA =  {mediana}")

plt.boxplot(idade, vert=False)
plt.show()