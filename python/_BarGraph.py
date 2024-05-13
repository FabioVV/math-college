import matplotlib.pyplot as plt


# gráfico de barras
# Veiculos que passaram pelo pedágio na última hora

veiculos = ["caminhão","ônibus","carro","moto"]
quantidade = [100,60,160,150]
colors = ["#FF1493","yellow","#00008B","#7CFC00"]


plt.subplots(figsize=(8,3))
plt.bar(veiculos, quantidade, color=colors)

plt.title("Veiculos que passaram pelo pedágio", color="blue")
plt.ylim([0,180])

for i, val in enumerate(quantidade):
  texto = f"{val} veiculos"
  y_coord = val + 2
  x_coord = i - 0.3
  plt.text(x=x_coord, y=y_coord, s=texto, fontsize=9)

plt.savefig("bar_graph.png")
plt.show()
