## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que determina um classificador básico para imagens de PD e CR, usando as features: 
# exponential_glcm_DifferenceEntropy
# lbp-2D_firstorder_InterquartileRange
# wavelet-H_gldm_DependenceVariance
# exponential_glrlm_ShortRunEmphasis

## Importando as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arff
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import os

# Preparando os arquivos
file_pd = 'radiomics_PD.arff'
file_cr = 'radiomics_CR.arff'

features = [
    'exponential_glcm_DifferenceEntropy',
    'lbp-2D_firstorder_InterquartileRange',
    'wavelet-H_gldm_DependenceVariance',
    'exponential_glrlm_ShortRunEmphasis'
]

output_dir = "resultados_quatro_features"
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

    # manter apenas numéricas
    df = df.select_dtypes(include=[np.number])

    return df

df = load_data()

X = df[features]
y = df['target']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Preparação do modelo da árvode de decisão
clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_scaled, y)

y_pred = clf.predict(X_scaled)

# Resultados encontrados
print("\n=== FEATURES UTILIZADAS ===")
for f in features:
    print(f"- {f}")

print("\n=== RELATÓRIO DE CLASSIFICAÇÃO ===")
print(classification_report(y, y_pred, target_names=['PD', 'CR']))

cm = confusion_matrix(y, y_pred)

# Visualização dos dadoss
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1 - Matriz de confusão (como estamos com 4 features, não conseguimos visualizar "fisicamente" o gráfico)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['PD', 'CR'])
disp.plot(ax=ax[0], cmap='viridis', colorbar=False)
ax[0].set_title("Matriz de Confusão", fontweight='bold')

# Plot 2 - Árvore de decisão
plot_tree(
    clf,
    feature_names=features,
    class_names=['PD', 'CR'],
    filled=True,
    ax=ax[1]
)
ax[1].set_title("Árvore de Decisão (4 features)", fontweight='bold')

plt.tight_layout()

# salvar os resultados 
save_path = os.path.join(output_dir, "resultado_quatro_features.png")
plt.savefig(save_path, dpi=300)
print(f"\nFigura salva em: {save_path}")

plt.show()