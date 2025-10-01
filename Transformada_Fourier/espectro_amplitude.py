# Autor: Vitor Augusto Tibério - Estudante de Engenharia Elétrica (USP - São Carlos)

# Importando as Bibliotecas # 

import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

# Definindo as funções # 

def transformada_fourier(img):
  f = np.fft.fft2(img)
  fshift = np.fft.fftshift(f)
  magnitude_spectrum = 20*np.log(np.abs(fshift)+1.)
  return magnitude_spectrum

def plota_magnetude(img, magnitude_spectrum):
  plt.figure(figsize=(5,5))
  plt.subplot(1,2,1)
  plt.imshow(img,'gray')
  plt.subplot(1,2,2)
  plt.imshow(magnitude_spectrum,'gray')


## Carregando as Imagens ## 

circulo = cv.imread("circulo.tif",-1)
faixa_horizontal = cv.imread("faixahorizontal.tif",-1)
faixa_vertical = cv.imread("faixavertical.tif",-1)
losango = cv.imread("losango.tif",-1)
quadrado = cv.imread("quadrado.tif",-1)
retangulo_vertical = cv.imread("retangulovertical.tif",-1)
retangulo_horizontal = cv.imread("retangulohorizontal.tif",-1)
vret_sim = cv.imread("vret_sim.tif",-1)
hret_sim = cv.imread("hret_sim.tif",-1)
parallelogram = cv.imread("parallelogram.tif",-1)
parallelogram_2 = cv.imread("parallelogram_2.tif",-1)

## Calculando a transformada de Fourier das Imagens ##

tf_circulo = transformada_fourier(circulo)
tf_faixa_horizontal = transformada_fourier(faixa_horizontal)
tf_faixa_vertical = transformada_fourier(faixa_vertical)
tf_losango = transformada_fourier(losango)
tf_quadrado = transformada_fourier(quadrado)
tf_retangulo_vertical = transformada_fourier(retangulo_vertical)
tf_retangulo_horizontal = transformada_fourier(retangulo_horizontal)
tf_vret_sim = transformada_fourier(vret_sim)
tf_hret_sim = transformada_fourier(hret_sim)
tf_parallelogram = transformada_fourier(parallelogram)
tf_parallelogram_2 = transformada_fourier(parallelogram_2)

## Plotando a Magnetude das Imagens ## 

plota_magnetude(circulo, tf_circulo);
plota_magnetude(faixa_horizontal, tf_faixa_horizontal);
plota_magnetude(faixa_vertical, tf_faixa_vertical);
plota_magnetude(losango, tf_losango);
plota_magnetude(quadrado, tf_quadrado);
plota_magnetude(retangulo_vertical, tf_retangulo_vertical);
plota_magnetude(retangulo_horizontal, tf_retangulo_horizontal);
plota_magnetude(vret_sim, tf_vret_sim);
plota_magnetude(hret_sim, tf_hret_sim);
plota_magnetude(parallelogram, tf_parallelogram);
plota_magnetude(parallelogram_2, tf_parallelogram_2);