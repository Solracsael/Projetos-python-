import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do arquivo Excel
file_path = "Dados_de_Controle_Estatistico.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Selecionar apenas as colunas relevantes
df = df[["Data", "Diâmetro (mm)"]]

# Garantir que a coluna "Data" esteja no formato correto
df["Data"] = pd.to_datetime(df["Data"], errors="coerce")

# Definição dos limites de especificação
LSE = 50.02  # Limite Superior de Especificação
LIE = 49.98  # Limite Inferior de Especificação

# Estatísticas do processo
media_processo = df["Diâmetro (mm)"].mean()
desvio_padrao = df["Diâmetro (mm)"].std()

# Cálculo dos índices Cp e Cpk
Cp = (LSE - LIE) / (6 * desvio_padrao)
Cpk = min((LSE - media_processo) / (3 * desvio_padrao), (media_processo - LIE) / (3 * desvio_padrao))

# Exibir resultados
print(f"Média do processo: {media_processo:.5f} mm")
print(f"Desvio padrão: {desvio_padrao:.5f} mm")
print(f"Índice Cp: {Cp:.2f}")
print(f"Índice Cpk: {Cpk:.2f}")

# Verificação dos limites
def verificar_limites(Cp, Cpk):
    if Cp < 1:
        print("⚠️ O processo NÃO atende aos requisitos de qualidade (Cp < 1).")
    else:
        print("✅ O processo pode atender aos requisitos (Cp >= 1).")

    if Cpk < 1:
        print("⚠️ O processo está descentralizado e pode precisar de ajustes (Cpk < 1).")
    else:
        print("✅ O processo está bem centralizado (Cpk >= 1).")

verificar_limites(Cp, Cpk)

# Função para gerar gráficos
def plotar_graficos(df):
    # Histograma dos diâmetros
    plt.figure(figsize=(10, 5))
    plt.hist(df["Diâmetro (mm)"], bins=30, color='blue', edgecolor='black', alpha=0.7)
    plt.axvline(LIE, color='red', linestyle='dashed', linewidth=2, label="LIE (49.98 mm)")
    plt.axvline(LSE, color='red', linestyle='dashed', linewidth=2, label="LSE (50.02 mm)")
    plt.title("Distribuição dos Diâmetros")
    plt.xlabel("Diâmetro (mm)")
    plt.ylabel("Frequência")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico de Variação ao Longo do Tempo
    plt.figure(figsize=(12, 6))
    plt.plot(df["Data"], df["Diâmetro (mm)"], marker='o', linestyle='-', color='purple')
    plt.axhline(LIE, color='red', linestyle='dashed', linewidth=2, label="LIE (49.98 mm)")
    plt.axhline(LSE, color='red', linestyle='dashed', linewidth=2, label="LSE (50.02 mm)")
    plt.title("Variação dos Diâmetros ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Diâmetro (mm)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

plotar_graficos(df)

# Cálculo das Cartas de Controle X̄ e R
subgrupos = df.groupby("Data")["Diâmetro (mm)"]

# Médias e Amplitudes por subgrupo
medias = subgrupos.mean()
amplitudes = subgrupos.max() - subgrupos.min()

# Cálculo dos Limites de Controle (LCS e LCI)
X_bar = medias.mean()
R_bar = amplitudes.mean()

# Constantes para cartas de controle (A2, D3, D4 para subgrupos de tamanho 3)
A2 = 1.023  # Obtido em tabelas de controle estatístico
D3 = 0       # Obtido em tabelas de controle estatístico
D4 = 2.574   # Obtido em tabelas de controle estatístico

LCS_Xbar = X_bar + A2 * R_bar
LCI_Xbar = X_bar - A2 * R_bar
LCS_R = D4 * R_bar
LCI_R = D3 * R_bar

# Carta X̄ (Médias)
plt.figure(figsize=(12, 6))
plt.plot(medias, marker='o', linestyle='-', color='blue', label="Médias")
plt.axhline(X_bar, color='green', linestyle='dashed', linewidth=2, label="Média Geral")
plt.axhline(LCS_Xbar, color='red', linestyle='dashed', linewidth=2, label="LCS")
plt.axhline(LCI_Xbar, color='red', linestyle='dashed', linewidth=2, label="LCI")
plt.title("Carta de Controle X̄ (Médias)")
plt.xlabel("Data")
plt.ylabel("Média do Diâmetro")
plt.legend()
plt.grid(True)
plt.show()

# Carta R (Amplitude)
plt.figure(figsize=(12, 6))
plt.plot(amplitudes, marker='o', linestyle='-', color='red', label="Amplitude")
plt.axhline(R_bar, color='black', linestyle='dashed', linewidth=2, label="Média da Amplitude")
plt.axhline(LCS_R, color='red', linestyle='dashed', linewidth=2, label="LCS")
plt.axhline(LCI_R, color='red', linestyle='dashed', linewidth=2, label="LCI")
plt.title("Carta de Controle R (Amplitude)")
plt.xlabel("Data")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
