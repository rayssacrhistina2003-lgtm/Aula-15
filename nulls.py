import pandas as pd

dfNull = pd.read_csv(r"C:\Users\rayssa.christina\Downloads\funcionarios - Null.csv")


dfNullRemovido = dfNull.dropna(subset=['departamento', 'lucro']) #remove as linhas com valores nulos
dfNullPreenchidoTodos = dfNull.fillna("nenhum") #preenche as linhas vazias com um valor especifico
dfNullPreenchidoDepartamento = dfNull
dfNullPreenchidoDepartamento['departamento'] = dfNullPreenchidoDepartamento['departamento'].fillna("nenhum") #para so preencher 

print(dfNullPreenchidoTodos)
print("\n")
print(dfNullPreenchidoDepartamento)