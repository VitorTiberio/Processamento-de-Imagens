# Como realizar o processamento de imagens coloridas usando Python ? # 

## 1. Conversão entre RGB, HSV e CMY ## 

Nesse tópico, vamos abordar sobre a conversão entre os modelos de cores. O primeiro ponto extremamente importante é que o OpenCV, por padrão, carrega a imagem em BGR (Blue, Green, Red). 
Logo, quando trabalhamos com imagens coloridas, o primeiro passo é corrigir para RGB. Fazemos isso da seguinte maneira: 
```python
import cv2 as cv

img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED) ## Carrega a imagem. Ela vai estar no padrão BGR 
img_rgb = cv.cvtCOLOR(img, cv.COLOR_BGR2RGB) ## Converte a imagem de BGR para RGB
```
Como uma imagem RGB é composta em 3 diferentes canais, pode-se analisar cada um deles separadamente. Para separar cada canal, podemos fazer a seguinte manipulação: 
```python
img_r = img_rgb[:,:,0]
img_g = img_rgb[:,:,1]
img_b = img_rgb[:,:,2]
```
Preparando um plot para visualizar todos os canais, temos: 
```python
import matplotlib.pyplot as plt
import numpy as np

def plota_imagem_bloco(img, nome_img, canal_1, nome_canal_1, canal_2, nome_canal_2, canal_3, nome_canal_3):
  plt.figure(figsize=(20,60))
  plt.subplot(1,4,1)
  plt.title(nome_img)
  plt.imshow(img)
  plt.subplot(1,4,2)
  plt.title(nome_canal_1)
  plt.imshow(canal_1)
  plt.subplot(1,4,3)
  plt.title(nome_canal_2)
  plt.imshow(canal_2)
  plt.subplot(1,4,4)
  plt.title(nome_canal_3)
  plt.imshow(canal_3)

plota_imagem_bloco(img_rgb, "Imagem RGB Original", img_r, "Imagem do canal R", img_g, "Imagem do canal G", img_b, "Imagem do canal B")
```
De maneira semelhante, podemos plotar os canais R,G e B em escala de cinza, para facilitar a sua visualização. Fazemos isso da seguinte maneira: 
```python
def plota_imagem_bloco_gray(img, nome_img, canal_1, nome_canal_1, canal_2, nome_canal_2, canal_3, nome_canal_3):
  plt.figure(figsize=(20,60))
  plt.subplot(1,4,1)
  plt.title(nome_img)
  plt.imshow(img)
  plt.subplot(1,4,2)
  plt.title(nome_canal_1)
  plt.imshow(canal_1, cmap = 'gray')
  plt.subplot(1,4,3)
  plt.title(nome_canal_2)
  plt.imshow(canal_2, cmap = 'gray')
  plt.subplot(1,4,4)
  plt.title(nome_canal_3)
  plt.imshow(canal_3, cmap = 'gray')

plota_imagem_bloco_gray(img_rgb, "Imagem RGB Original", img_r, "Imagem do canal R", img_g, "Imagem do canal G", img_b, "Imagem do canal B")
```
--- 

Em relação a conversão para HSV, o processo é muito parecido, sendo executado da seguinte maneira: 
```python
img_hsv = cv.cvtColor(img_rgb, cv.COLOR_RGB2HSV)
img_h = img_hsv[:,:,0]
img_s = img_hsv[:,:,1]
img_v = img_hsv[:,:,2]
```
---

Agora, 
