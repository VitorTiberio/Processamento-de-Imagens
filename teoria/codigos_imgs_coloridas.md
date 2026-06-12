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

Agora, quando queremos converter uma imagem para CMY, o OpenCV não realiza essa conversão diretamente. Devemos nos lembrar que a imagem em CMY é "ao contrário" da imagem RGB. Logo, CMY = 1 - RGB. Portanto, podemos realizar a seguinte manipulação para obter a imagem em CMY: 
```python
img_c = 255 - img_r
img_m = 255 - img_g
img_y = 255 - img_b
img_cmy = np.dstack((img_c, img_m, img_y))
```
Com a imagem em mãos, pode-se partir para os plots, como feito nos itens anteriores. 
---
## 2. Filtragem de Imagens Coloridas ## 

### 2.1 - Filtro Passa Baixa ### 
Vamos supor que queremos realizar o filtro de uma imagem RGB. No caso, a filtragem não pode ser realizada na imagem em RGB, uma vez que pode ocasionar a mudança de cor nas mesmas. O primeiro passo, SEMPRE, é converter a imagem para HSI, HSV ou HSL, realizando a filtragem sempre no canal acromático (ou seja, no canal I, V ou L). Isso não irá provocar a alteração da cor no processamento. Uma possível implementação pode ser consultada abaixo: 
```python
## Carregando a imagem que será processada ##
img = cv.imread("tiberio.png") ## carrega a imagem ruidosa
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)  ## converte a imagem ruidosa de BGR para RGB
## Filtragem com o ruído gaussiano da imagem original ##
img_blur = cv.blur(img_rgb, (7,7))
## Convertendo a imagem para HSV ##
img_hsv = cv.cvtColor(img_rgb, cv.COLOR_RGB2HSV) ## converte a imagem RGB para HSV
img_h = img_hsv[:,:,0] ## seleciona o canal H
img_s = img_hsv[:,:,1] ## seleciona o canal S
img_v = img_hsv[:,:,2] ## seleciona o canal V
plt.figure(figsize=(20,60))
plt.subplot(1,4,1)
plt.title("Imagem Original em HSV".format(img.shape))
plt.imshow(img_hsv)
plt.subplot(1,4,2)
plt.title("Canal H")
plt.imshow(img_h, "gray")
plt.subplot(1,4,3)
plt.title("Canal S")
plt.imshow(img_s, "gray")
plt.subplot(1,4,4)
plt.title("Canal V")
plt.imshow(img_v, "gray")
## Seleção do canal V (acromático) para aplicação do filtro ##
img_v_blur = cv.blur(img_v, (7,7))
plt.figure(figsize=(20,60))
plt.subplot(1,4,1)
plt.title("Imagem Original do canal V")
plt.imshow(img_v, "gray")
plt.subplot(1,4,2)
plt.title("Imagem filtrada do canal V")
plt.imshow(img_v_blur, "gray")
## Item 5 ##
img_hsv_filtrada = np.dstack((img_h, img_s, img_v_filtrada)) ## substitui o canal V pela imagem filtrada
img_rgb_final = cv.cvtColor(img_hsv_filtrada, cv.COLOR_HSV2RGB) ## converte a imagem HSV para RGB novamente
plt.figure(figsize=(20,60))
plt.subplot(1,4,1)
plt.title("Imagem Original")
plt.imshow(img_rgb)
plt.subplot(1,4,2)
plt.title("Imagem Filtrada")
plt.imshow(img_rgb_final)
```
---
### 2.2 - Filtro passa alta ###
```python
#kernel filtro passa-alta

filtro_pa = np.array(((-1,-1,-1),
                      (-1, 8,-1),
                      (-1,-1,-1)))

## -- Seu código começa AQUI -- ##
def plota_imagem(nome, imagem):
  plt.figure(figsize=(5,5))
  plt.title(nome)
  plt.imshow(imagem)
def plota_imagem_grayscale(nome, imagem):
  plt.figure(figsize=(5,5))
  plt.title(nome)
  plt.imshow(imagem, cmap = 'gray')
def plota_canais_grayscale(img, nome, canal_1, nome_canal_1, canal_2, nome_canal_2, canal_3, nome_canal_3):
  plt.figure(figsize=(60,60))
  plt.subplot(1,4,1)
  plt.title(nome)
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
def plota_histograma(img, bin):
  plt.figure(figsize=(5,5))
  plt.hist(img.flatten(),bins=bin,density=False,range=(0,255))
  plt.show()

img = cv.imread("rgb_stripes.bmp", cv.IMREAD_UNCHANGED) ## le a imagem original

## Transformando a imagem de BGR para RGB e selecionando os canais ## 
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_r = img_rgb[:,:,0]
img_g = img_rgb[:,:,1]
img_b = img_rgb[:,:,2]
plota_canais_grayscale(img_rgb, "Imagem Original", img_r, "Imagem do canal R", img_g, "Imagem do canal G", img_b, "Imagem do canal B")

## Convertendo a imagem RGB para HSV ## 
img_hsv = cv.cvtColor(img_rgb, cv.COLOR_RGB2HSV)
img_h = img_hsv[:,:,0]
img_s = img_hsv[:,:,1]
img_v = img_hsv[:,:,2]
plota_canais_grayscale(img_hsv, "Imagem HSV", img_h, "Imagem do canal H", img_s, "Imagem do canal S", img_v, "Imagem do canal V")

'''
O canal escolhido para aplicação do filtro passa alta é o canal H
'''
img_h_filtrada = cv.filter2D(img_h, -1, filtro_pa)
plota_imagem_grayscale("Imagem do canal H filtrada", img_h_filtrada)
plota_histograma(img_h_filtrada, 256)
'''
Um possível threshold é o 100
'''
threshold = 100
img_h_pa_bin = np.where(img_h_filtrada > threshold, 255, 0)
plt.figure(figsize=(5,5))
plt.title('Plota a imagem binarizada')
plt.imshow(img_h_pa_bin, "gray")
## Item 5 e 6##
img_h_pa_bin_mask = cv.bitwise_not(img_h_pa_bin)
img_hsv[:,:,2] = img_h_pa_bin_mask
img_rgb = cv.cvtColor(img_hsv, cv.COLOR_HSV2RGB)
plt.figure(figsize=(5,5))
plt.title('Plota a imagem final, com destaque nas bordas')
plt.imshow(img_rgb)
'''
O filtro que aplicamos em H para detectar as bordas tem que ser aplicado no canal V, uma vez que se for aplicada em outro canal, ocorrerá uma mudança na cor da imagem
'''
## -- Seu código termina AQUI -- ##


## -- Seu código termina AQUI -- ##
```
