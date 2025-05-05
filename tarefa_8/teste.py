import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

print("\n--- Parte 1: Análise Estatística ---")
df1 = pd.read_csv('california_housing_train.csv')

cols = ['median_income', 'median_house_value', 'housing_median_age']
for col in cols:
    print(f"\nAnálise para: {col}")
    print(f"Média: {df1[col].mean()}")
    print(f"Mediana: {df1[col].median()}")
    print(f"Moda: {df1[col].mode()[0]}")
    print(f"Desvio padrão: {df1[col].std()}")
    print(f"Mínimo: {df1[col].min()}")
    print(f"Máximo: {df1[col].max()}")

    Q1 = df1[col].quantile(0.25)
    Q2 = df1[col].quantile(0.50)
    Q3 = df1[col].quantile(0.75)
    IQR = Q3 - Q1

    print(f"Q1: {Q1}, Q2: {Q2}, Q3: {Q3}, IQR: {IQR}")

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df1[(df1[col] < lower_bound) | (df1[col] > upper_bound)]

    print(f"Número de outliers: {outliers.shape[0]}")

print("\n--- Parte 2: Tratamento de Valores Ausentes ---")
df2 = pd.read_csv('Economy_of_US_na.csv')

missing_cols = df2.columns[df2.isnull().any()]
print(f"\nColunas com valores ausentes: {missing_cols.tolist()}")

df2_fill_mean = df2.fillna(df2.mean(numeric_only=True))
print("\nDados preenchidos com média.")

df2_drop = df2.dropna(thresh=(df2.shape[1] - 2))
print(f"\nDados com linhas removidas (limite de 2 ausentes): {df2_drop.shape}")

print("\n--- Parte 3: Amostragem ---")
df3 = pd.read_csv('Nov2Temp.csv')

sample1 = df3.sample(frac=0.15, replace=False, random_state=42)
print(f"\nAmostra de 15% sem reposição: {sample1.shape}")

sample2 = df3.sample(frac=0.20, replace=True, random_state=42)
print(f"Amostra de 20% com reposição: {sample2.shape}")

print("""
Diferença prática:
- Sem reposição: cada linha só aparece uma vez, representando uma amostra mais fiel da diversidade.
- Com reposição: uma mesma linha pode aparecer mais de uma vez, útil para simulações ou algoritmos de ensemble como bagging.
""")

print("\n--- Parte 4: Discretização de Variáveis ---")
df4 = pd.read_csv('california_housing_train.csv')

quartis = df4['median_income'].quantile([0.25, 0.5, 0.75])
faixas = [df4['median_income'].min()-1, quartis[0.25], quartis[0.5], quartis[0.75], df4['median_income'].max()+1]
rotulos = ['Baixa renda', 'Média-baixa', 'Média-alta', 'Alta renda']

df4['faixa_renda'] = pd.cut(df4['median_income'], bins=faixas, labels=rotulos, include_lowest=True)

plt.figure(figsize=(8,5))
sns.countplot(data=df4, x='faixa_renda', palette='Set2')
plt.title("Distribuição de Renda (Discretizada)")
plt.xlabel("Faixa de Renda")
plt.ylabel("Número de Casas")
plt.tight_layout()
plt.show()
