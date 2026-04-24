## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem)
## Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código que treina o modelo a ser usado para a interface de classificação de imagens
## Modelo baseado nas 4 features do classificador (classificador_basico_4.py)

## Importando as Bilbiotecas ## 
import pandas as pd
import numpy as np
import arff
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import joblib

# Features usadas no classificador de melhor acurária (PD vs CR)
features = [
    'exponential_glcm_DifferenceEntropy',
    'lbp-2D_firstorder_InterquartileRange',
    'wavelet-H_gldm_DependenceVariance',
    'exponential_glrlm_ShortRunEmphasis'
]

## Carregando os dados para treinamento ##
def load_arff(file):
    with open(file, 'r') as f:
        data = arff.load(f)
    df = pd.DataFrame(data['data'], columns=[attr[0] for attr in data['attributes']])
    return df

df_pd = load_arff('radiomics_PD.arff')
df_cr = load_arff('radiomics_CR.arff')

df_pd['target'] = 0
df_cr['target'] = 1

df = pd.concat([df_pd, df_cr], ignore_index=True)
df = df.select_dtypes(include=[np.number])

X = df[features]
y = df['target']

## Treinando o modelo ##
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_scaled, y)

## salvando o modelo e o scaler para uso posterior na interface
joblib.dump(clf, "modelo_PD_CR.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Modelo e scaler salvos!")
