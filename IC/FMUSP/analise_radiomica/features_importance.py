## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que verifica a importância das features para distinção de pacientes PD e CR

## Importando as Bibliotecas 
import pandas as pd
import numpy as np
import arff  # liac-arff
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import shap

## Definindo as funções

def load_arff(file_path):
    with open(file_path, 'r') as f:
        dataset = arff.load(f)

    df = pd.DataFrame(
        dataset['data'],
        columns=[attr[0] for attr in dataset['attributes']]
    )

    return df

# Carregando os arquivos ARFF com os dados dos pacientes PD e CR:
df_pd = load_arff("radiomics_PD.arff")
df_cr = load_arff("radiomics_CR.arff")
df_pd["label"] = 0  # PD
df_cr["label"] = 1  # CR
df = pd.concat([df_pd, df_cr], ignore_index=True)

# Separação de Features e Target
X = df.drop(columns=["label"])
X = X.select_dtypes(include=[np.number])  # mantém só numéricas
y = df["label"]

# Pré-processamento dos dados
X = X.fillna(X.mean())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Seleção das top 10 features que mais realizam a distinção entre os grupos
selector = SelectKBest(score_func=f_classif, k=10)
X_new = selector.fit_transform(X_scaled, y)

selected_features = X.columns[selector.get_support()]
scores = selector.scores_[selector.get_support()]

feature_ranking = pd.DataFrame({
    "Feature": selected_features,
    "Score": scores
}).sort_values(by="Score", ascending=False)

print("\nTop 10 features mais relevantes:\n")
print(feature_ranking.to_string(index=False))

# Treinando o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled[:, selector.get_support()], y)

# Dataset final com nomes
X_selected = pd.DataFrame(
    X_scaled[:, selector.get_support()],
    columns=selected_features
)

# Garantir tipo numérico puro
X_selected = X_selected.astype(float)

