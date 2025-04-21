import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Carregar a base de dados
df = pd.read_csv("pandas.read_csv.csv", sep=';')  

# 2. Calcular medidas estatísticas para salario e nota_avaliacao
variaveis = ['salario', 'nota_avaliacao']

for var in variaveis:
    print(f"\n--- Estatísticas para {var} ---")
    print(f"Média: {df[var].mean()}")
    print(f"Mediana: {df[var].median()}")
    print(f"Moda: {df[var].mode()[0]}")
    print(f"Desvio padrão: {df[var].std()}")
    print(f"Mínimo: {df[var].min()}")
    print(f"Máximo: {df[var].max()}")
    
    q1 = df[var].quantile(0.25)
    q2 = df[var].quantile(0.5)
    q3 = df[var].quantile(0.75)
    iqr = q3 - q1
    
    print(f"Q1 (25%): {q1}")
    print(f"Q2 (50% / Mediana): {q2}")
    print(f"Q3 (75%): {q3}")
    print(f"Intervalo Interquartil (IQR): {iqr}")

# 3. Visualizações
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=df[['salario', 'nota_avaliacao']])
plt.title('Boxplot - Salário e Nota de Avaliação')

plt.subplot(1, 2, 2)
plt.hist(df['idade'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma - Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')

plt.tight_layout()
plt.savefig("grafico.png")


# 4. Identificar os valores considerados outliers para o salário com base no IQR
q1 = df['salario'].quantile(0.25)
q3 = df['salario'].quantile(0.75)
iqr = q3 - q1

# Limites inferior e superior para o salário
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Identificar outliers
outliers_salario = df[(df['salario'] < limite_inferior) | (df['salario'] > limite_superior)]

# 5. Listar os nomes das pessoas com salário fora dos limites
print("\n--- Pessoas com salário fora dos limites definidos ---")
print(outliers_salario['nome'])  


# 6. Dividir os dados em dois grupos por país
grupo_a = df[df['pais'] == 'Brasil']['salario']
grupo_b = df[df['pais'] == 'EUA']['salario']
grupo_a.to_csv('grupo_brasil.csv', index=False)  
grupo_b.to_csv('grupo_eua.csv', index=False) 
# 7. Aplicar t-teste independente para comparar o salário médio entre os dois países
t_stat, p_value = stats.ttest_ind(grupo_a, grupo_b)

# 8. Interpretar o valor-p (p-value)
print(f"\nValor-p do t-teste: {p_value}")

if p_value < 0.05:
    print("Rejeitamos H₀: Há diferença significativa entre os salários dos dois países.")
else:
    print("Não rejeitamos H₀: Não há diferença significativa entre os salários dos dois países.")
