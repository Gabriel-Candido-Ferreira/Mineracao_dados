import pandas as pd

df = pd.read_excel("ds_salaries.xlsx")

df.to_csv("ds_trans_salario.csv", sep=';', decimal=',', encoding='utf-8', index=False)

print(df)