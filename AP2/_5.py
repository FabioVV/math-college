import numpy as np

results = [7.8 , 5.0 , 3.1 , 4.8 , 4.4 , 5.4 , 8.5 , 5.9 , 5.9 , 3.1 , 5.6 , 3.7 , 6.6 , 8.4 , 4.3 , 5.3 , 3.2 , 7.6 , 4.2 , 8.3 , 2.3 , 6.4]


media = np.mean(results)
dp = np.std(results)

intervalo_menos = media - dp
intervalo_mais =  media + dp

outlier_abaixo = []
outlier_acima = []


for x in range(len(results)):
    if results[x] < intervalo_menos:
        outlier_abaixo.append(results[x])

    elif results[x] > intervalo_mais:
        outlier_acima.append(results[x])


print(f"{len(outlier_abaixo)} alunos ficaram abaixo do intervalo media - dp")
print(f"{len(outlier_acima)} alunos ficaram acima do intervalo media + dp")