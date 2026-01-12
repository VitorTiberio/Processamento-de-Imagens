import cv2
import numpy as np
import os
from pathlib import Path

# Configuração dos caminhos
folder_images = 'recortes'
folder_masks = 'masks'
folder_output = 'masks_atualizadas'

# Cria a pasta de saída se não existir
os.makedirs(folder_output, exist_ok=True)

# Parâmetros de ajuste
THRESHOLD_VAL = 248  # Sensibilidade para pegar o branco do marcador
FOLGA_PIXELS = 7     # Valor da "folga". Aumentar, se necessário!!!

# Lista todas as imagens na pasta de recortes
for filename in os.listdir(folder_images):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.tif')):
        
        # Caminhos completos
        img_path = os.path.join(folder_images, filename)
        mask_path = os.path.join(folder_masks, filename) # Assume mesmo nome
        
        if not os.path.exists(mask_path):
            print(f"Aviso: Máscara não encontrada para {filename}")
            continue

        # Carregar imagem e máscara
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        # Detectar marcadores (Threshold)
        _, markers = cv2.threshold(img, THRESHOLD_VAL, 255, cv2.THRESH_BINARY)

        # Criar a "folga" (Dilatação)
        # O kernel define o tamanho do "pincel" que vai engrossar a marcação
        kernel = np.ones((FOLGA_PIXELS, FOLGA_PIXELS), np.uint8)
        markers_com_folga = cv2.dilate(markers, kernel, iterations=1)

        # Aplicar na máscara original
        # Onde o marcador expandido existe, a máscara vira 0 (preto)
        updated_mask = mask.copy()
        updated_mask[markers_com_folga == 255] = 0

        # Salvar resultado
        save_path = os.path.join(folder_output, filename)
        cv2.imwrite(save_path, updated_mask)
        print(f"Processado: {filename}")

print("\nConcluído! As novas máscaras estão na pasta:", folder_output)