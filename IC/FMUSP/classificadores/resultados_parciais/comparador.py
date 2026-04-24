## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que compara os resultados obtidos com 3 e 4 features no classificador

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arff
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay, accuracy_score
import os

# Configurando os arquivos
file_pd = 'radiomics_PD.arff'
file_cr = 'radiomics_CR.arff'

features_3 = [
    'exponential_glcm_DifferenceEntropy',
    'lbp-2D_firstorder_InterquartileRange',
    'wavelet-H_gldm_DependenceVariance'
]

features_4 = features_3 + [
    'exponential_glrlm_ShortRunEmphasis'
]

output_dir = "comparacao_3_vs_4_features"
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

# Modelo da Árvore de Decisão
def train_and_evaluate(features, nome):
    X = df[features]
    y = df['target']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clf = DecisionTreeClassifier(max_depth=4, random_state=42)
    clf.fit(X_scaled, y)

    y_pred = clf.predict(X_scaled)

    acc = accuracy_score(y, y_pred)
    cm = confusion_matrix(y, y_pred)

    print(f"\n===== RESULTADOS: {nome} =====")
    print(f"Acurácia: {acc:.4f}")
    print(classification_report(y, y_pred, target_names=['PD', 'CR']))

    return clf, cm, acc

# Executando o modelo
clf3, cm3, acc3 = train_and_evaluate(features_3, "3 FEATURES")
clf4, cm4, acc4 = train_and_evaluate(features_4, "4 FEATURES")

# Visulizando os dados
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# Plotando a matriz com 3 features
disp3 = ConfusionMatrixDisplay(confusion_matrix=cm3, display_labels=['PD', 'CR'])
disp3.plot(ax=ax[0,0], cmap='viridis', colorbar=False)
ax[0,0].set_title(f"3 Features (Acc={acc3:.2f})")

# plotando a árvore de 3 features
plot_tree(
    clf3,
    feature_names=features_3,
    class_names=['PD', 'CR'],
    filled=True,
    ax=ax[0,1]
)
ax[0,1].set_title("Árvore - 3 Features")

# plotando a matriz com 4 features
disp4 = ConfusionMatrixDisplay(confusion_matrix=cm4, display_labels=['PD', 'CR'])
disp4.plot(ax=ax[1,0], cmap='viridis', colorbar=False)
ax[1,0].set_title(f"4 Features (Acc={acc4:.2f})")

# plotando a árvore com 4 features
plot_tree(
    clf4,
    feature_names=features_4,
    class_names=['PD', 'CR'],
    filled=True,
    ax=ax[1,1]
)
ax[1,1].set_title("Árvore - 4 Features")

plt.tight_layout()

# salvando os resultados
save_path = os.path.join(output_dir, "comparacao_modelos.png")
plt.savefig(save_path, dpi=300)
print(f"\nFigura salva em: {save_path}")

plt.show()
