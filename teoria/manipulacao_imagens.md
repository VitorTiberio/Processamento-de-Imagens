# Manipulação de Imagens usando Python # 

## 1. Como ler uma imagem ? ## 

Para realizar a leitura de uma imagem usando o Python, utilizamos a bilbioteca OpenCV. Vamos supor que temos uma imagem 'tiberio.png' e queremos fazer a leitura da mesma. 

Para isso, fazemos: 

```python
import cv2 as cv

img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED)
```

Ao invés do IMREAD_UNCHANGED, pode-se ler a imagem com o índice -1. 

```python
img = cv.imread('tiberio.png', -1)
```

## 2. Como realizar o plot de uma imagem ? ## 

Para realizar o plot de uma imagem, utiliza-se a biblioteca do matplotlib. 

```python
## Importando as Bibliotecas ##

import matplotlib.pyplot as plt
import cv2 as cv

## Definindo as Funções ##

def plota_imagem(img, titulo):
'''
Função que plota uma imagem. Recebe como parâmetros:
img = imagem a ser plotada;
titulo = título do plot.
'''
  plt.figure(figsize=(5,5))
  plt.title(titulo)
  plt.imshow(img, cmap='gray')
  plt.show()

## Código Principal ##

img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED)
plota_imagem(img, "Imagem do Tibério")
```

## 3. Como extrair as dimensões de uma imagem ? ## 

Para encontrar as dimensões de uma imagem, utilizamos a função "np.shape", da biblioteca Numpy. Uma possível maneira de implementá-la é: 

```python
M, N = np.shape(img)
```

No caso, o valor de M recebe uma dimensão (no eixo x) e o N a outra (no eixo y). Podemos adicionar esse resultado dentro do título no plot, se necessário. Isso pode ser implementado da seguinte forma: 

```python
## Importando as Bibliotecas ##

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

## Definindo as Funções ##

def plota_imagem(img, titulo, M, N):
'''
Função que plota uma imagem. Recebe como parâmetros:
img = imagem a ser plotada;
titulo = título do plot;
M = tamanho da imagem no eixo x;
N = tamanho da imagem no eixo y.
'''
  plt.figure(figsize=(5,5))
  plt.title(f"{titulo} shape({M},{N})")
  plt.imshow(img, cmap='gray')
  plt.show()

## Código Principal ##

img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED)
M, N = np.shape(img)
plota_imagem(img, "Imagem do Tibério", M, N)
```

## 4. Exclusão e Inversão de Ordem das Linhas/Colunas da Imagem ## 

IMPLEMENTAR

## 5. Como alterar a resolução espacial de uma imagem ? ## 

Para alterarmos a resolução espacial de uma imagem, deve-se utilizar a função "cv.resize". Uma possível implementação pode ser encontrada no código abaixo: 

```python
## Importando as Bibliotecas ## 
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

## Definindo as funções ##
def redimensionar(img, largura, altura):
'''
Função que realiza o redimensionamento da imagem.
img = imagem que será redimensionada;
largura e altura = tamanho para a qual a imagem será redimensionada. 
'''
  img_red = cv.resize(img, (largura, altura))
  plt.figure(figsize=(5,5))
  plt.title(f'Imagem de dimensões: {largura}x{altura}')
  plt.imshow(img_red, 'gray')
  plt.show()

## Código Principal ##

img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED)
redimensionar(img,280,280)
redimensionar(img,200,200)
redimensionar(img,125,125)
redimensionar(img,100,100)
redimensionar(img,50,50)
```

## 6. Como visualizar o histograma de uma imagem ? ## 

Para a visualização do histograma de uma imagem, devemos utilizar a função "plt.hist". No caso, a mesma pode ser implementada da seguinte forma: 

```python
def plota_histograma(bin, img):
'''
Função que realiza o plot do histograma de uma imagem.
img = imagem na qual o histograma será plotado;
bin = número bin.
'''
  plt.hist(img.flatten(),bins=bin,density=False,range=(0,255))
  plt.show()
```
Em um código completo, essa função poderia ser aplicada da seguite forma: 
```python
img = cv.imread("paisagem.tif")
img_cinza = cv.imread("paisagem.tif", cv.IMREAD_UNCHANGED)
plota_imagem(img, "Imagem Original") ## função presente em tópico anterior
plota_histograma(50, img)
plota_histograma(100, img)
```

## 7. Como equalizar o histograma de uma imagem ? ## 

Para realizar a equalização de um histograma, pode-se utilizar a função "cv.equalizeHist". Geralmente isso é feito quando o histograma está muito "empelotado", fazendo com que a distribuição dos níveis de cinza seja mais uniforme. 

Essa técnica pode ser implementada da seguinte maneira: 

```python
## Definindo as funções ## 
def plota(imagem, nome):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  plt.show()
  plt.hist(imagem.flatten(),bins=100,density=False,range=(0,255))
  plt.show()

## Código Principal ## 
img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED)
img = img.astype(np.uint8)
img_out = cv.equalizeHist(img)
plota(img, 'Imagem Original')
plota(img_out, 'Imagem Equalizada')
```

## 8. Binarização de Imagens ## 

Em relação a binarização, existe algumas formas na qual ela pode ser implementada. O primeiro método é através da análise do histograma da imagem, uma vez que através dele, pode-se definir um ponto de threshold para a binarização. Com esse limiar definido, podemos fazer um loop para avaliar todos os valores presentes na imagem e definir se esse valor deve ser substituido por zero (caso fique abaixo do ponto de threshold) ou por um, caso fique acima. Desta maneira, implementamos da seguinte forma: 

```python
## Importando as Bibliotecas ##

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

## Definindo as Funções ##

def plota_imagem(img, nome):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  plt.show()
  plt.hist(imagem.flatten(),bins=100,density=False,range=(0,255))
  plt.show()

## Programa Principal ##

img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED) ## Lê a imagem 
img = img.astype(np.uint8)
img_bin = cv.imread('tiberio.png, cv.IMREAD_UNCHANGED) ## Lê a imagem 
img_bin = img_bin.astype(np.uint8)
plota(img, 'Imagem Original') ## Plota a imagem original e o seu respectivo histograma
## Analisando o Hist. obtido, temos que o vale ocorre próximo ao bit n = 140.
M, N = np.shape(img_bin) ## Pega as dimensões da imagem (M,N)
limiar = 140 ## define o valor de limiar (definido pelo histograma)
for i in range M:
  for j in range N:
    if img_bin[i][j] >= limiar:
      img_bin[i][j] = 1
    else:
      img_bin[i][j] = 0

plota(img_bin, 'Imagem Binarizada (regular)')
```
Note que pelo fato da imagem ser binarizada, a mesma deve assumir valores de 0 ou 1. 
Outra maneira que podemos realizar essa análise (de uma forma MUITO mais simples) é utilizando a função "cv.threshold", através do método Otsu. No caso, sua aplicação seria: 
```python
th_value, img_bin_otsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plota(img_bin_otsu, 'Imagem Binarizada (Otsu)')
print(f'O valor encontrado pelo Otsu é: {th_value}')
```
