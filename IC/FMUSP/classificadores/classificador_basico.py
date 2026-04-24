## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que determina um classificador básico para imagens de PD e CR, usando a feature de exponential_glcm_DifferenceEntropy

## Importando as Bibliotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arff
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import os

## Configurando os arquivos a serem manipulados: 
output_dir = "resultados_classificador_unico"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_pd = 'radiomics_PD.arff'
file_cr = 'radiomics_CR.arff'
feature_alvo = 'exponential_glcm_DifferenceEntropy'

def load_data():
    try:
        with open(file_pd, 'r') as f:
            data_pd = arff.load(f)

        with open(file_cr, 'r') as f:
            data_cr = arff.load(f)

        df_pd = pd.DataFrame(data_pd['data'], columns=[attr[0] for attr in data_pd['attributes']])
        df_pd['target'] = 0

        df_cr = pd.DataFrame(data_cr['data'], columns=[attr[0] for attr in data_cr['attributes']])
        df_cr['target'] = 1

        return pd.concat([df_pd, df_cr], ignore_index=True)

    except Exception as e:
        print("Erro ao carregar arquivos:", e)
        return None

## Execução do Processo
df_total = load_data()

if df_total is not None:
    # Separando a feature e o alvo
    # Importante: Mesmo sendo apenas uma feature, precisamos normalizar (Z-score), para manter a consistência com suas análises anteriores
    X_raw = df_total[[feature_alvo]]
    y = df_total['target']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_raw)
    
    # Criando um DataFrame auxiliar para facilitar a plotagem
    df_analise = pd.DataFrame(X_scaled, columns=[feature_alvo])
    df_analise['Grupo'] = y.replace({0: 'PD', 1: 'CR'})

    # Treino do Classificador (Decision Stump - Árvore de profundidade 1)
    clf = DecisionTreeClassifier(max_depth=1)
    clf.fit(X_scaled, y)
    
    # Encontrando o limiar (threshold)
    threshold = clf.tree_.threshold[0]
    
    # Predições
    y_pred = clf.predict(X_scaled)

    # Exibição de Resultados no Terminal
    print(f"\n--- Análise para a Feature: {feature_alvo} ---")
    print(f"Limiar de decisão encontrado (Z-score): {threshold:.4f}")
    print("\nRelatório de Desempenho:")
    print(classification_report(y, y_pred, target_names=['PD', 'CR']))

    # Visualização Gráfica
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico 01 -  Distribuição e Limiar
    sns.stripplot(data=df_analise, x=feature_alvo, y='Grupo', hue='Grupo', 
                  ax=ax[0], palette='viridis', alpha=0.5, jitter=0.2)
    ax[0].axvline(threshold, color='red', linestyle='--', label=f'Threshold: {threshold:.2f}')
    ax[0].set_title(f'Distribuição de {feature_alvo}', fontweight='bold')
    ax[0].legend()

    # Gráfico 2 - Matriz de Confusão
    cm = confusion_matrix(y, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['PD', 'CR'])
    disp.plot(ax=ax[1], cmap='viridis', colorbar=False)
    ax[1].set_title('Matriz de Confusão', fontweight='bold')

    plt.tight_layout()
    
    # Salvando os resultados em uma pasta
    save_path = os.path.join(output_dir, "resultado_classificacao_entropia.png")
    plt.savefig(save_path, dpi=300)
    print(f"\nGráfico salvo em: {save_path}")
    
    plt.show()
