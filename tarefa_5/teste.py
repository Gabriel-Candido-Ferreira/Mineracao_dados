import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

inicio = '2024-01-01'
fim = '2024-12-31'

petr4 = yf.download('PETR4.SA', start=inicio, end=fim, group_by='ticker', auto_adjust=True)
vale3 = yf.download('VALE3.SA', start=inicio, end=fim, group_by='ticker', auto_adjust=True)

if petr4.empty or vale3.empty:
    print("Erro: Dados não foram baixados corretamente.")
else:
    petr4_close = petr4.xs('Close', axis=1, level=1)['PETR4.SA']
    vale3_close = vale3.xs('Close', axis=1, level=1)['VALE3.SA']

    df = pd.DataFrame({
        'PETR4': petr4_close,
        'VALE3': vale3_close
    })

    df_monthly = df.resample('M').last()

    df_monthly['PETR4_Lucro'] = df_monthly['PETR4'].pct_change() * 100
    df_monthly['VALE3_Lucro'] = df_monthly['VALE3'].pct_change() * 100

    plt.figure(figsize=(10, 6))
    plt.plot(df_monthly.index, df_monthly['PETR4'], label='PETR4', color='blue')
    plt.plot(df_monthly.index, df_monthly['VALE3'], label='VALE3', color='green')
    plt.title('Comparativo de Preços de Fechamento - PETR4 vs VALE3 (2024)', fontsize=14)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Preço de Fechamento Ajustado (R$)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_comparativo.png")

    df_monthly.to_csv('comparativo_petr4_vale3_2024.csv')

    print(df_monthly[['PETR4_Lucro', 'VALE3_Lucro']])
