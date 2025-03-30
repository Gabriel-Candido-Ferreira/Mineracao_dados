import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

db_path = "C:/Users/gabri/Mineracao_dados/tarefa_4/shopping.sqlite"


conn = sqlite3.connect(db_path)

tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(tables_query, conn)
print(tables)

df = pd.read_sql_query("SELECT * FROM customer_shopping_data LIMIT 10;", conn)
print(df.head())

df_full = pd.read_sql_query("SELECT * FROM customer_shopping_data;", conn)

df_full['invoice_date'] = pd.to_datetime(df_full['invoice_date'], dayfirst=True, errors='coerce')
df_full['price'] = pd.to_numeric(df_full['price'], errors='coerce')

df_full['total_price'] = df_full['price'] * df_full['quantity']

info = df_full.describe(include='all')

analise_geral = {
    "Total de registros": [len(df_full)],
    "Gênero predominante": [df_full['gender'].value_counts().idxmax()],
    "Compras do gênero predominante": [df_full['gender'].value_counts().max()],
    "Idade média dos clientes": [round(df_full['age'].mean(), 1)],
    "Idade mínima": [df_full['age'].min()],
    "Idade máxima": [df_full['age'].max()],
    "Categorias únicas de produto": [df_full['category'].nunique()],
    "Categoria mais frequente": [df_full['category'].value_counts().idxmax()],
    "Método de pagamento mais usado": [df_full['payment_method'].value_counts().idxmax()],
    "Compras com o método mais usado": [df_full['payment_method'].value_counts().max()],
    "Shopping mais movimentado": [df_full['shopping_mall'].value_counts().idxmax()],
    "Compras no shopping mais movimentado": [df_full['shopping_mall'].value_counts().max()],
    "Preço médio dos produtos": [round(df_full['price'].mean(), 2)],
    "Quantidade média por compra": [round(df_full['quantity'].mean(), 1)],
    "Valor médio total por compra": [round(df_full['total_price'].mean(), 2)]
}

df_analise = pd.DataFrame(analise_geral)
df_analise.to_csv("analise_geral_compras.csv", index=False)
df_full.to_csv("dados_compras_processados.csv", index=False)

plt.figure(figsize=(10, 6))
sns.countplot(
    data=df_full,
    x='category',
    order=df_full['category'].value_counts().index,
    palette='Set2'
)
plt.title('Número de Compras por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Compras')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("grafico_compras_por_categoria.png", dpi=300)

plt.show()

