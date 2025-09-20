# 📘 Transformada de Fourier em Imagens 📘 # 

A **Transformada de Fourier (TF)** é uma ferramenta matemática fundamental no processamento de sinais e imagens.  
Ela permite analisar uma função (ou imagem) no **domínio da frequência**, decompondo-a em componentes senoidais de diferentes frequências, amplitudes e fases.

---

## Conceitos Básicos

- Uma imagem pode ser vista como uma função bidimensional no **domínio espacial** *(x, y)*.  
- A Transformada de Fourier mapeia essa função para o **domínio da frequência** *(u, v)*.  
- O resultado é uma representação em que cada ponto do espectro indica **quanto de uma determinada frequência** está presente na imagem.

### Definições

- **Transformada de Fourier Contínua 2D:**

$$
F(u,v) = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f(x,y)\, e^{-j2\pi(ux+vy)} \,dx\,dy
$$

- **Transformada Discreta de Fourier (DFT) 2D:**

$$
F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y)\, e^{-j2\pi\left(\frac{ux}{M} + \frac{vy}{N}\right)}
$$

---

## Espectro de Fourier

- **Magnitude**: mostra a contribuição de cada frequência (energia das componentes).  
- **Fase**: contém informações estruturais e posicionais da imagem.  
- **Espectro de Potência**: módulo ao quadrado da transformada, usado para medir energia.  

> Em imagens, a fase é **mais importante que a magnitude** para preservar a estrutura visual.

---

## Propriedades Importantes

1. **Periodicidade e Simetria Conjugada**  
   - O espectro da DFT é periódico.  
   - Para imagens reais, existe simetria conjugada no espectro.  

2. **Translação**  
   - Multiplicar a imagem por \((-1)^{x+y}\) desloca a frequência zero para o centro do espectro (visualização comum em processamento de imagens).

3. **Separabilidade**  
   - A TF 2D pode ser computada aplicando-se a TF 1D primeiro nas linhas e depois nas colunas, otimizando o cálculo.

4. **Rotação**  
   - Uma rotação no espaço implica em uma rotação equivalente no espectro de frequências.

5. **Convolução**  
   - **No espaço**: convolução ↔ **na frequência**: multiplicação.  
   - **No espaço**: multiplicação ↔ **na frequência**: convolução.  

6. **Mudança de Escala**  
   - Reduzir a escala espacial da imagem expande o espectro em frequência, e vice-versa.

7. **Valor Médio (DC)**  
   - O valor \(F(0,0)\) corresponde à média dos níveis de cinza da imagem.

---

## Aplicações em Processamento de Imagens

- **Filtragem passa-baixa** → suavização, remoção de ruído.  
- **Filtragem passa-alta** → realce de bordas e detalhes.  
- **Compressão** → aproveita a concentração de energia em baixas frequências.  
- **Análise de textura** → estudo da distribuição de frequências em diferentes direções.  

---

## Implementação Prática

- **DFT**: custo computacional proporcional a \(N^2\).  
- **FFT (Fast Fourier Transform)**: algoritmo otimizado com custo \(N \log N\).  
- Em imagens digitais, a FFT é amplamente utilizada (ex.: `numpy.fft.fft2`, `cv2.dft`).  

---

## Observações sobre Visualização

- A magnitude do espectro é normalmente exibida em escala logarítmica, devido à grande faixa dinâmica.  
- Para melhor interpretação, o espectro costuma ser **centralizado** (baixas frequências no meio, altas nas bordas).  

---

## Exemplo em Python

```python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Carregar imagem em escala de cinza
img = cv.imread("imagem.png", cv.IMREAD_GRAYSCALE)

# Aplicar FFT 2D
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Magnitude em escala logarítmica
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

# Exibir resultados
plt.subplot(121), plt.imshow(img, cmap="gray")
plt.title("Imagem Original"), plt.axis("off")

plt.subplot(122), plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Espectro de Fourier"), plt.axis("off")

plt.show()

