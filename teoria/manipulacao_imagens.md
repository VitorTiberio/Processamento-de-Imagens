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
