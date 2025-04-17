
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar o dataset CSV
df_csv = pd.read_csv("default_of_credit_card_clients__courseware_version_1_21_19_old.csv")

# Exercício 1: Criar listas com os nomes das características financeiras
bill_columns = ['BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6']
pay_columns  = ['PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6']

# Exercício 2: Usar .describe() nas características de valor da fatura
print("Resumo estatístico das faturas:")
print(df_csv[bill_columns].describe())

# Exercício 3: Histogramas das características de valor da fatura
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()
for idx, col in enumerate(bill_columns):
    axes[idx].hist(df_csv[col], bins=20, color='lightcoral', edgecolor='black')
    axes[idx].set_title(f'Histograma de {col}')
    axes[idx].set_xlabel('Valor da Fatura')
    axes[idx].set_ylabel('Frequência')
plt.tight_layout()
plt.show()

# Exercício 4: Resumo estatístico das características de pagamento
print("\nResumo estatístico dos pagamentos:")
print(df_csv[pay_columns].describe())

# Exercício 5: Histogramas das características de pagamento com xrot
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()
for idx, col in enumerate(pay_columns):
    axes[idx].hist(df_csv[col], bins=20, color='mediumseagreen', edgecolor='black')
    axes[idx].set_title(f'Histograma de {col}')
    axes[idx].set_xlabel('Valor do Pagamento')
    axes[idx].set_ylabel('Frequência')
    axes[idx].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

# Exercício 6: Contar valores iguais a zero
print("\nContagem de pagamentos iguais a zero:")
print((df_csv[pay_columns] == 0).sum())

# Exercício 7: Transformação log10 para pagamentos diferentes de zero
df_nonzero_payments = df_csv[pay_columns].replace(0, np.nan)
log_transformed = df_nonzero_payments.apply(np.log10)

# Histogramas log-transformados
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()
for idx, col in enumerate(pay_columns):
    axes[idx].hist(log_transformed[col].dropna(), bins=30, color='steelblue', edgecolor='black')
    axes[idx].set_title(f'Log10 de {col}')
    axes[idx].set_xlabel('log10(valor)')
    axes[idx].set_ylabel('Frequência')
plt.tight_layout()
plt.show()
