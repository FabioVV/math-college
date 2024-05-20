import matplotlib.pyplot as plt


estados = ["Minas Gerais","Espirto Santo","Amapá","Roraima", "Rondônia", "Pará", "Amazonas", "Tocantins", "Pernambuco"]
valores = [276.6,289.6,211.4,232.5, 233.8, 168.6, 173.9, 172.6, 183.8]
colors = ["black","yellow","green","red", "purple", "brown", "blue", "pink", "grey"]


plt.subplots(figsize=(8,3))
plt.bar(estados, valores, color=colors)

plt.title("Desenvolvimento humano nos estados Brasileiro", color="green", fontsize=14)
plt.ylim([0,400])

for i, val in enumerate(valores):
  texto = f"R$ {val:.2f}"
  y_coord = val + 2
  x_coord = i - 0.3
  plt.text(x=x_coord, y=y_coord, s=texto, fontsize=9)

plt.savefig("6.png")
plt.show()
