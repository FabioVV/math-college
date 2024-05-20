

p1 = int(input("Quantas pessoas pagarão a excursão com desconto de 12,5%? -> "))
p2 = int(input("Quantas pessoas pagarão a excursão com desconto de 25%? -> "))
p3 = int(input("Quantas pessoas pagarão a excursão sem desconto -> "))

total_sem_desc = 1250.00

total_arrecadado_p1 = (12.5 / 100) * total_sem_desc
total_arrecadado_p2 = (25.00 / 100) * total_sem_desc
total_arrecadado_p3 = p3 * total_sem_desc

total_arrecadado = total_arrecadado_p1 + total_arrecadado_p2 + total_arrecadado_p3


print(f'R$ {total_arrecadado}')