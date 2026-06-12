# Como realizar o processamento de imagens coloridas usando Python ? # 

## 1. Conversão entre RGB, HSV e CMY ## 

Nesse tópico, vamos abordar sobre a conversão entre os modelos de cores. O primeiro ponto extremamente importante é que o OpenCV, por padrão, carrega a imagem em BGR (Blue, Green, Red). 
Logo, quando trabalhamos com imagens coloridas, o primeiro passo é corrigir para RGB. Fazemos isso da seguinte maneira: 
```python
import cv2 as cv

img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED) ## Carrega a imagem. Ela vai estar no padrão BGR 
img_rgb = cv.cvtCOLOR(img, cv.COLOR_BGR2RGB) ## Converte a imagem de BGR para RGB
```
