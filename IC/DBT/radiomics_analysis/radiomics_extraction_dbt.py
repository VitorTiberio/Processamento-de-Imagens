## Autor: Vitor Augusto Tibério - Engenharia Elétrica - EESC/USP
## Aluno de Iniciação Científica - LAVI - Orientador: Prof. Dr. Marcelo Andrade da Costa Vieira
## Extração Radiômica em DBT usando PyRadiomics
## Ultima alteração: 07/07/2026

## Importando as Bibliotecas
import os
import time
import logging
import six
import arff
import numpy as np
import pandas as pd
import SimpleITK as sitk
import radiomics
from radiomics import featureextractor

## Configurando o PyRadiomics
radiomics.setVerbosity(logging.ERROR)
settings = {}
settings['binWidth'] = 25
settings['resampledPixelSpacing'] = None
settings['interpolator'] = sitk.sitkBSpline
settings['sigma'] = [2, 3, 4]
settings['force2D'] = False ## a extração será realizada em DBT
settings['geometryTolerance'] = 10 ## tolerância para pequenas inconsistências geométricas

extractor = featureextractor.RadiomicsFeatureExtractor(**settings)

## Ativa todos os tipos de imagem: Original, Wavelet, LoG etc.
extractor.enableAllImageTypes()
extractor.disableAllFeatures()

## Ativa todas as features das classes abaixo
## Para DBT, usar shape em vez de shape2D
extractor.enableFeaturesByName(
    firstorder=[],
    glcm=[],
    glszm=[],
    gldm=[],
    glrlm=[],
    ngtdm=[],
    shape=[]
)

## Definindo Diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

## Pasta contendo os volumes DBT e as máscaras
dbt_path = os.path.join(BASE_DIR, "dbt")
mask_path = os.path.join(BASE_DIR, "masks")

## Exemplo esperado:
## dbt/
##   caso_001.nii.gz
## masks/
##   caso_001_mask.nii.gz

files = [
    f for f in os.listdir(dbt_path)
    if f.lower().endswith((".nii", ".nii.gz", ".nrrd", ".mha", ".mhd"))
]

features = []

## Loop principal
for file in files:
    print(f"Processando: {file}")
    t = time.time()

    image_file = os.path.join(dbt_path, file)

    ## Nome da máscara correspondente
    base_name = file.replace(".nii.gz", "").replace(".nii", "").replace(".nrrd", "").replace(".mha", "").replace(".mhd", "")
    mask_file = os.path.join(mask_path, base_name + "_mask.nii.gz")

    if not os.path.exists(mask_file):
        print(f"Máscara não encontrada para {file}")
        continue

    ## Lendo imagem DBT e máscara
    image = sitk.ReadImage(image_file)
    mask = sitk.ReadImage(mask_file)

    ## Conferência geométrica básica
    if image.GetSize() != mask.GetSize():
        print(f"Imagem e máscara têm tamanhos diferentes em {file}")
        print("Imagem:", image.GetSize())
        print("Máscara:", mask.GetSize())
        continue

    ## Garantindo que a máscara seja binária
    mask_np = sitk.GetArrayFromImage(mask)
    mask_np = (mask_np > 0).astype(np.uint8)

    mask_bin = sitk.GetImageFromArray(mask_np)
    mask_bin.CopyInformation(mask)

    ## Aplicando extração radiômica
    try:
        featureVector = extractor.execute(image, mask_bin)
    except Exception as e:
        print(f"Erro no PyRadiomics ({file}): {e}")
        continue

    ## Removendo diagnostics
    clean_features = {}

    for key, value in six.iteritems(featureVector):
        if not key.startswith("diagnostics_"):
            clean_features[key] = value

    clean_features["name"] = file

    features.append(clean_features)

    print(f"Finalizado em {time.time() - t:.2f}s")

## Salvando CSV
output_csv = os.path.join(RESULTS_DIR, "radiomics_dbt.csv")

if len(features) == 0:
    raise RuntimeError("Nenhuma feature foi extraída.")

df = pd.DataFrame(features)
df.to_csv(output_csv, index=False)

## Exportando para ARFF
output_arff = os.path.join(RESULTS_DIR, "radiomics_dbt.arff")

features_arff = {
    'relation': 'pyradiomics_dbt',
    'attributes': [
        (key, 'REAL') if not isinstance(value, str) else (key, 'STRING')
        for key, value in six.iteritems(features[0])
    ],
    'data': [
        [
            value.item() if hasattr(value, "item") else value
            for _, value in feature.items()
        ]
        for feature in features
    ],
}

with open(output_arff, "w", encoding="utf8") as f:
    arff.dump(
        f.name,
        features_arff['data'],
        relation=features_arff['relation'],
        names=[name for name, _ in features_arff['attributes']]
    )

print("Extração radiômica em DBT finalizada com sucesso!")
print(f"CSV salvo em: {output_csv}")
print(f"ARFF salvo em: {output_arff}")
