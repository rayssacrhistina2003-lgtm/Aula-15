import pandas as pd 

dfNull = pd.read_csv(r"C:\Users\rayssa.christina\Downloads\funcionarios - Null.csv")


print(dfNull.info())


dfNull['data de nascimento'] = pd.to_datetime(dfNull['data de nascimento'])

#caso a data esteja em formato brasileiro use :
#dfTrocadoData['data de nascimento'] = pd.to_datetime(df['data de nascimento'], format= '%d/%m/%y')


print(dfNull.info())

print(dfNull)