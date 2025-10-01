# Autor: Vitor Augusto Tibério - Engenharia Elétrica - USP/São Carlos

# Importanto as Bibliotecas # 
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

# Definindo as Funções ## 

def calcula_media(img):
  media = np.mean(img)
  return media

def transformada_fourier(img):
  f = np.fft.fft2(img)
  fshift = np.fft.fftshift(f)
  magnitude_spectrum = 20*np.log(np.abs(fshift)+1.)
  return fshift, magnitude_spectrum

def plota_magnetude(img, magnitude_spectrum):
  plt.figure(figsize=(5,5))
  plt.subplot(1,2,1)
  plt.imshow(img,'gray')
  plt.subplot(1,2,2)
  plt.imshow(magnitude_spectrum,'gray')

def plota_imagem(titulo, imagem):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  plt.title(f'{titulo}')
  plt.show()

def transformada_inversa(f):
  ifshift = np.fft.ifftshift(f)
  img = np.abs(np.fft.ifft2(ifshift))
  return img

# Carregando e Processando a Imagem ## 

img = cv.imread('pirate.tif', -1)
inv = cv.bitwise_not(img)
plota_imagem('Imagem Original', img)
plota_imagem('Imagem Invertida', inv)

# Calculado a Média das Imagens #

media_original = calcula_media(img)
media_inversa = calcula_media(inv)
diferenca = abs(media_original - media_inversa)
print(f'O valor da média original é {media_original}. O valor da média inversa é {media_inversa}. Com isso, A diferença entre as médias é {diferenca}')

## Calculando a Transformada de Fourier da Imagem ## 

tf_img, mag_tf_img = transformada_fourier(img)
tf_inv, mag_tf_inv = transformada_fourier(inv)

## Plotando a Magnetude das Imagens ## 

plota_magnetude(img, mag_tf_img);
plota_magnetude(img, mag_tf_inv);

## Pegando a diferença da magnetude das imagens e plotando ## 

diferenca_mag = mag_tf_img - mag_tf_inv
diferenca_mag = 20*np.log(np.abs(diferenca_mag)+1.)
plt.figure(figsize=(15,15))
plt.imshow(diferenca_mag,'gray')

## Cálculo da IFFT ## 

ifft_diferenca = transformada_inversa(diferenca_mag)
ifft_media = np.mean(ifft_diferenca)
ifft_maximo = np.max(ifft_diferenca)
ifft_minimo = np.min(ifft_diferenca)
print(f'O valor médio da imagem é {ifft_media}. O valor máximo da imagem é {ifft_maximo}. O valor mínimo da imagem é {ifft_minimo}.')