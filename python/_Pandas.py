import pandas as pd

table = pd.read_excel("./Sales.xlsx", sheet_name="Plan1")
# (change all of the print statements in this file to a display())
# When on jupyter notebook
# (Only work's there i think)

print(table.shape) # número de linhas e colunas

len_table = len(table)

faturamento = table['Valor Final'].sum()
print(f"faturamento total = R$ {faturamento:.2f}")

'''
Faturamento por loja
'''
print("Faturamento Por Loja")
FPL = table[["ID Loja","Valor Final"]]
table(FPL)

print("Agrupando por nome da loja (consta como id na tabela (???))")
FPL = table[["ID Loja","Valor Final"]].groupby("ID Loja").sum()
print(FPL)


print("Faturamento por produto")
FPP = table[['ID Loja', 'Produto', "Valor Final"]].groupby(["ID Loja","Produto"]).sum()
print(FPP)


'''
Possivel solução para aumentar o faturamento da empresa.
A loja Iguatemi Campinas vende uma bermuda denominada "Bermuda Liso" onde
o faturamento dessa bermuda foi de R$ 36581,00
As outras lojas não vendem essa bermuda e uma sugestão para aumentar o faturamento
é que todas as lojas passem a vender a bermuda denominada "Bermuda Liso"
'''
