import matplotlib.pyplot as plt



# grafico de linhas
# Temperatura máxima e mínima em algun dias do mês
eixoxdias = [1 ,5, 10,15,20,25,30]
eixoytemmax = [28,29,25,32,34,36,31]
eixoytemmin = [21,22,17,23,23,24,20]
plt.plot(eixoxdias, eixoytemmax,
         label="Temperatura máxima",
         color = "#D2691E",
         linestyle = "--",
         linewidth = 2,
         marker = "o")
plt.plot(eixoxdias, eixoytemmin,
         label="Temperatura mínima",
         color = "#FF00FF",
         marker = "o")
plt.title("Temperatura Máxima e Mínima",
          fontsize = 20,
          color = "#DC143C",
          fontweight="bold",)
plt.xlabel("Datas")
plt.ylabel("Temperaturas")
plt.legend()
plt.grid()
plt.savefig("grafico de linhas.png")
plt.show()
