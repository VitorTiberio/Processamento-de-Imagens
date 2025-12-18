## Código para retirar as masks e recortes de imagens DICOM usando máscaras PNG com saída recortada no tamanho da lesão (bounding box da máscara) ##

## Autor: Vitor Augusto Tibério - Laboratório Avançado de Visão e Imagem (LAVI) - Escola de Engenharia de São Carlos (EESC)
## Universidade de São Paulo (USP) ##


## Importando as Bibliotecas ##
import os
import cv2 as cv
import numpy as np
import pydicom


## Função para leitura de DICOM ##
def ler_dicom(caminho_dcm):
    dcm = pydicom.dcmread(caminho_dcm)
    img = dcm.pixel_array.astype(np.float32)

    # Normalização para 8 bits
    img = cv.normalize(img, None, 0, 255, cv.NORM_MINMAX)
    img = img.astype(np.uint8)

    return img


## Função para criar máscara binária a partir do PNG ##
## Apenas pixels com nível de cinza == 255 são considerados ##
def criar_mascara_binaria_255(caminho_png):
    mask = cv.imread(caminho_png, cv.IMREAD_GRAYSCALE)
    if mask is None:
        raise ValueError(f"Máscara não encontrada: {caminho_png}")

    mask_bin = np.zeros_like(mask, dtype=np.uint8)
    mask_bin[mask == 255] = 255

    return mask_bin


## Função para recortar imagem e máscara no tamanho da lesão ##
## Utiliza a bounding box dos pixels com valor 255 ##
def recortar_por_mascara(img, mask):
    coords = np.where(mask == 255)

    if coords[0].size == 0:
        raise ValueError("Máscara não possui pixels com valor 255")

    y_min, y_max = coords[0].min(), coords[0].max()
    x_min, x_max = coords[1].min(), coords[1].max()

    img_crop = img[y_min:y_max + 1, x_min:x_max + 1]
    mask_crop = mask[y_min:y_max + 1, x_min:x_max + 1]

    return img_crop, mask_crop


## Função para processar uma pasta ##
def processar_pasta(pasta_atual, pasta_masks, pasta_recortes):
    arquivos = os.listdir(pasta_atual)

    # Lista de DICOMs e dicionário de PNGs (máscaras)
    dcms = [f for f in arquivos if f.lower().endswith(".dcm")]
    pngs = {os.path.splitext(f)[0]: f for f in arquivos if f.lower().endswith(".png")}

    for dcm in dcms:
        nome_base = os.path.splitext(dcm)[0]

        # Verifica se existe máscara correspondente
        if nome_base not in pngs:
            print(f"Sem máscara para {dcm} — ignorado")
            continue

        caminho_dcm = os.path.join(pasta_atual, dcm)
        caminho_png = os.path.join(pasta_atual, pngs[nome_base])

        # Leitura da imagem DICOM e da máscara
        img = ler_dicom(caminho_dcm)
        mask = criar_mascara_binaria_255(caminho_png)

        # Verificação de compatibilidade
        if img.shape != mask.shape:
            print(f"Tamanho incompatível: {nome_base}")
            continue

        # Aplica a máscara na imagem
        recorte = cv.bitwise_and(img, img, mask=mask)

        # Recorte final no tamanho da lesão
        try:
            recorte_crop, mask_crop = recortar_por_mascara(recorte, mask)
        except ValueError as e:
            print(f"{nome_base}: {e}")
            continue

        # Nome do arquivo de saída
        nome_saida = f"{os.path.basename(pasta_atual)}_{nome_base}.png"

        # Salvando máscara e recorte
        cv.imwrite(os.path.join(pasta_masks, nome_saida), mask_crop)
        cv.imwrite(os.path.join(pasta_recortes, nome_saida), recorte_crop)

        print(f"Processado (recortado): {nome_saida}")


## Código principal ##
if __name__ == "__main__":

    pasta_raiz = r"C:\Users\lavi\Desktop\MMG_descompressed_teste"

    pasta_masks = os.path.join(pasta_raiz, "masks")         # pasta para armazenar as máscaras
    pasta_recortes = os.path.join(pasta_raiz, "recortes")   # pasta para armazenar os recortes

    os.makedirs(pasta_masks, exist_ok=True)
    os.makedirs(pasta_recortes, exist_ok=True)

    # Percorre todas as subpastas
    for root, dirs, files in os.walk(pasta_raiz):

        # Evita processar as pastas de saída
        if root in [pasta_masks, pasta_recortes]:
            continue

        processar_pasta(root, pasta_masks, pasta_recortes)
