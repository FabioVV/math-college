import pandas as pd

dfs = pd.read_excel("./Sales.xlsx", sheet_name="Plan1")
#display(dfs)

len_table = len(dfs)

faturamento = dfs['Valor Final'].sum()

#fpl = dfs[['ID Loja', 'Valor Final']].groupby("ID Loja").sum()
#display(fpl)

fpp = dfs[['ID Loja', 'Produto', "Valor Final"]].groupby(["ID Loja","Produto"]).sum()
print(fpp)

_result = dfs[['ID Loja', 'Produto', "Valor Final"]].groupby(["ID Loja","Produto"]).sum()
print(_result)
