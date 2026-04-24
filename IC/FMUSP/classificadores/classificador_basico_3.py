## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que determina um classificador básico para imagens de PD e CR, usando as features: 
# exponential_glcm_DifferenceEntropy
# lbp-2D_firstorder_InterquartileRange
# wavelet-H_gldm_DependenceVariance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arff
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from mpl_toolkits.mplot3d import Axes3D
import os

# Configurando os arquivos
file_pd = 'radiomics_PD.arff'
file_cr = 'radiomics_CR.arff'

features = [
    'exponential_glcm_DifferenceEntropy',
    'lbp-2D_firstorder_InterquartileRange',
    'wavelet-H_gldm_DependenceVariance'
]

output_dir = "resultados_tres_features"
os.makedirs(output_dir, exist_ok=True)

# Carregando os dados
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

    # manter apenas dados numéricos
    df = df.select_dtypes(include=[np.number])

    return df

df = load_data()
X = df[features]
y = df['target']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modelo da árvode de decisão
clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_scaled, y)

y_pred = clf.predict(X_scaled)

# Resultados encontrados
print("\n=== RELATÓRIO DE CLASSIFICAÇÃO ===")
print(classification_report(y, y_pred, target_names=['PD', 'CR']))

cm = confusion_matrix(y, y_pred)

# Visualizando os resultados
sns.set_theme(style="whitegrid")
fig = plt.figure(figsize=(20, 6))

# Plot 1 - Dispersão 3D
ax1 = fig.add_subplot(131, projection='3d')
df_plot = pd.DataFrame(X_scaled, columns=features)
df_plot['Grupo'] = y.replace({0: 'PD', 1: 'CR'})
colors = df_plot['Grupo'].map({'PD': 'blue', 'CR': 'green'})
ax1.scatter(
    df_plot[features[0]],
    df_plot[features[1]],
    df_plot[features[2]],
    c=colors
)
ax1.set_xlabel(features[0])
ax1.set_ylabel(features[1])
ax1.set_zlabel(features[2])
ax1.set_title("Distribuição 3D das Features")

# Plot 2 - Matriz de confusão
ax2 = fig.add_subplot(132)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['PD', 'CR'])
disp.plot(ax=ax2, cmap='viridis', colorbar=False)
ax2.set_title("Matriz de Confusão")

# Plot 3 - Árvore de decisão
ax3 = fig.add_subplot(133)
plot_tree(
    clf,
    feature_names=features,
    class_names=['PD', 'CR'],
    filled=True,
    ax=ax3
)
ax3.set_title("Árvore de Decisão")

plt.tight_layout()

# salvando os resultados
save_path = os.path.join(output_dir, "resultado_tres_features.png")
plt.savefig(save_path, dpi=300)
print(f"\nFigura salva em: {save_path}")

plt.show()