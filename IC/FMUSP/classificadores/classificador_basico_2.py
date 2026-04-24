## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que determina um classificador básico para imagens de PD e CR, usando as features:
## exponential_glcm_DifferenceEntropy 
## lbp-2D_firstorder_InterquartileRange

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arff
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import os

## Configurando os arquivos a serem manipulados: 
file_pd = 'radiomics_PD.arff'
file_cr = 'radiomics_CR.arff'

features = [
    'exponential_glcm_DifferenceEntropy',
    'lbp-2D_firstorder_InterquartileRange'
]

output_dir = "resultados_duas_features"
os.makedirs(output_dir, exist_ok=True)

def load_arff(file):
    with open(file, 'r') as f:
        data = arff.load(f)
    df = pd.DataFrame(data['data'], columns=[attr[0] for attr in data['attributes']])
    return df

def load_data():
    df_pd = load_arff(file_pd)
    df_cr = load_arff(file_cr)

    df_pd['target'] = 0
    df_cr['target'] = 1

    df = pd.concat([df_pd, df_cr], ignore_index=True)

    # manter só colunas numéricas
    df = df.select_dtypes(include=[np.number])

    return df

df = load_data()

X = df[features]
y = df['target']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Configurando a árvode de decisão
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_scaled, y)

y_pred = clf.predict(X_scaled)

# Resultados
print("\n=== RELATÓRIO DE CLASSIFICAÇÃO ===")
print(classification_report(y, y_pred, target_names=['PD', 'CR']))

cm = confusion_matrix(y, y_pred)

# Plotando os resultados
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(1, 3, figsize=(20, 6))

# Plot 1 - Dispersão 2D das Features
df_plot = pd.DataFrame(X_scaled, columns=features)
df_plot['Grupo'] = y.replace({0: 'PD', 1: 'CR'})

sns.scatterplot(
    data=df_plot,
    x=features[0],
    y=features[1],
    hue='Grupo',
    palette='viridis',
    ax=ax[0]
)

ax[0].set_title("Distribuição 2D das Features", fontweight='bold')

# Plot 2 - Matriz de confusão
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['PD', 'CR'])
disp.plot(ax=ax[1], cmap='viridis', colorbar=False)
ax[1].set_title("Matriz de Confusão", fontweight='bold')

# Plot 3 - Árvore de decisão
plot_tree(
    clf,
    feature_names=features,
    class_names=['PD', 'CR'],
    filled=True,
    ax=ax[2]
)
ax[2].set_title("Árvore de Decisão", fontweight='bold')

plt.tight_layout()

# salvando os resultados
save_path = os.path.join(output_dir, "resultado_duas_features.png")
plt.savefig(save_path, dpi=300)
print(f"\nFigura salva em: {save_path}")

plt.show()