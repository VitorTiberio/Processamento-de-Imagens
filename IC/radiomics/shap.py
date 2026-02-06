## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem) - Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código para geração do gráfico de Shap do projeto do FMUSP

## Dependências: pip install pandas numpy scikit-learn shap liac-arff openpyxl

## Importando as bilbiotecas

import pandas as pd
import numpy as np
import arff
import shap
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

## Definindo o caminho dos arquivos
ARFF_PATH = r"C:\Users\adm\Desktop\tratamento\resultados\radiomics_recortes_limpos.arff"
EXCEL_PATH = r"C:\Users\adm\Desktop\tratamento\controle_imagens_fmusp.xlsx"

## Lendo o arquivo ARFF
with open(ARFF_PATH, 'r', encoding="utf8") as f:
    arff_data = arff.load(f)

columns = [attr[0] for attr in arff_data['attributes']]
df = pd.DataFrame(arff_data['data'], columns=columns)

## Lendo a planilha de controle das imagens 
controle_df = pd.read_excel(EXCEL_PATH)

# coluna com ID da imagem --> coluna 0
# coluna com status (CR / PD) --> coluna 5

# Exemplo de nomes (MUDAR DE ACORDO COM A PLANILHA!!!):
# controle_df.columns --> confirir no print(controle_df.columns)

ID_COL = controle_df.columns[0]     # "ID" da imagem
STATUS_COL = controle_df.columns[5] # Status do tratamento --> CR (Regressão da Doença) e PD (Progressão da Doença)

# Extrair o ID da imagem do arquivo

def extract_id(name):
    # Procura padrão IDxxxx
    match = re.search(r'ID(\d+)', name)
    if match:
        return int(match.group(1))
    return None

df["img_id"] = df["name"].apply(extract_id)

## Casa os dados com a planilha

controle_df["img_id"] = controle_df[ID_COL].astype(int)

df = df.merge(
    controle_df[[ "img_id", STATUS_COL ]],
    on="img_id",
    how="inner"
)

## Desenvolve um target binário para o tratamento --> CR = 0 | PD = 1
df[STATUS_COL] = df[STATUS_COL].astype(str).str.strip().str.upper()

df["target"] = df[STATUS_COL].map({
    "CR": 0,
    "PD": 1
})

# Remover casos sem rótulo válido
df = df.dropna(subset=["target"])

print("\nDistribuição das classes:")
print(df["target"].value_counts())

# Treinando o modelo

y = df["target"]
X = df.drop(columns=["target", "img_id", "name", STATUS_COL], errors='ignore')
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=500,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

## Gráfico de Shap global --> Diferenciação das features que mais impactam na diferença entre os casos. 

## Seleciona as 20 features que mais fazem diferenças. Alterar em max_display caso queiremos mais features. 

plt.figure()
shap.summary_plot(
    shap_values[1],  # classe PD (1)
    X_test,
    plot_type="bar",
    max_display=20
)
plt.title("Top features - diferenciação PD vs CR")
plt.show()

# Shap de distribuição --> quais features mais impactaram na diferenciação entre ambos 

plt.figure()
shap.summary_plot(
    shap_values[1],
    X_test,
    max_display=20
)
plt.title("SHAP distribution - PD vs CR")
plt.show()
