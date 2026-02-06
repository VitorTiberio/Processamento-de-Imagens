## Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI (Laboratório Avançado de Visão e Imagem) - Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Código adaptado do trabalho de doutorado do Lucas Exposto
## Ultima alteração: 05/02/2026

## Importando as Bibliotecas 
import os 
import time
import logging

import numpy as np
import cv2
import six
import arff

import SimpleITK as sitk
import radiomics
from radiomics import featureextractor
import pandas as pd 

## Configurando o PyRadiomics

## Parâmetros iguais ao que foram usados na tese do Lucas:

##binWidth = 25 --> discretização da intensidade
##sem reamostragem --> preserva resolução original
##BSpline --> interpolação suave
##sigma --> filtros LoG 
##force2D = True --> força a análise 2d
##geometryTolerance --> tolerância para pequenas inconsistências geométricas

radiomics.setVerbosity(logging.ERROR)

settings = {}
settings['binWidth'] = 25
settings['resampledPixelSpacing'] = None
settings['interpolator'] = sitk.sitkBSpline
settings['sigma'] = [2, 3, 4]
settings['force2D'] = True
settings['geometryTolerance'] = 10

extractor = featureextractor.RadiomicsFeatureExtractor(**settings)

extractor.enableAllImageTypes()

extractor.disableAllFeatures()

## Ativa todas as Features das classes abaixo: 
extractor.enableFeaturesByName(
    firstorder=[],
    glcm=[],
    glszm=[],
    gldm=[],
    glrlm=[],
    ngtdm=[],
    shape2D=[]
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)
recortes_path = os.path.join(BASE_DIR, "recortes_limpos")

## Controle de Arquivo --> Pasta que contém os recortes limpos (sem marcadores)
files = [f for f in os.listdir(recortes_path) if f.lower().endswith(".png")]

features = []

## Loop principal do código: 
for file in files:
    print(f"Processando: {file}")
    t = time.time()

    img_path = os.path.join(recortes_path, file)

    ## Lendo os recortes (em PNG)
    image_np = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if image_np is None:
        print(f"Erro ao ler {file}")
        continue

    image_1 = sitk.GetImageFromArray(image_np)

    # Considerei a ROI para os píxeis diferentes de zero. SE A IMAGEM TIVER RUIDOSA TEM QUE ALTERAR AQUIII!!!
    mask_np = (image_np > 0).astype(np.uint8)
    label_1 = sitk.GetImageFromArray(mask_np)

    # Aplicando a extração radiômica
    try:
        featureVector = extractor.execute(image_1, label_1)
    except Exception as e:
        print(f"Erro no PyRadiomics ({file}): {e}")
        continue

    #  Remoção de diagnostics --> Não é análise radiômica, suja os dados que foram obtidos. 

    clean_features = {}
    for key, value in six.iteritems(featureVector):
        if not key.startswith("diagnostics_"):
            clean_features[key] = value

    # Relacionando com o caso compatível
    clean_features["name"] = file

    features.append(clean_features)

    print(f"Finalizado em {time.time() - t:.2f}s")

output_csv = os.path.join(RESULTS_DIR, "radiomics_recortes_limpos.csv")
if len(features) == 0:
    raise RuntimeError("Não econtramos nenhuma feature! ")
df = pd.DataFrame(features)
df.to_csv(output_csv, index = False)
# Exportando para ARFF
if len(features) == 0:
    raise RuntimeError("Nenhuma feature foi extraída.")

features_arff = {
    'relation': 'pyradiomics_recortes_limpos',
    'attributes': [
        (key, 'REAL') for key, _ in six.iteritems(features[0])
    ],
    'data': [
        [
            value.item() if not isinstance(value, str) else value
            for _, value in feature.items()
        ]
        for feature in features
    ],
}

with open("radiomics_recortes_limpos.arff", "w", encoding="utf8") as f:
    arff.dump(
        f.name,
        features_arff['data'],
        relation=features_arff['relation'],
        names=[name for name, _ in features_arff['attributes']]
    )

print("Extração finalizada com sucesso!")
