# Como realizar a transformada de Fourier utilizando Python ? # 
---

## Afinal, o que é a transformada de Fourier de uma Imagem ? ## 

A transformada de Fourier de uma função amostrada finita é uma função contínua, periódica e infinita. No domínio da frequência, o espectro se repete em infinitos períodos. O cálculo da transformada é feito em apenas um período.

Como ela é, em geral, complexa, pode ser expressa na forma polar:

$$
F(u,v)=|F(u,v)|\,e^{j\phi(u,v)}
$$

onde:

- $|F(u,v)|$ é a magnitude (espectro de Fourier);
- $\phi(u,v)$ é o ângulo de fase.

sendo a magnitude (espectro de Fourier ou espectro de frequência):

$$
|F(u,v)|=\sqrt{R^2(u,v)+I^2(u,v)}
$$

em que:

- $R(u,v)$ é a parte real da transformada;
- $I(u,v)$ é a parte imaginária da transformada.

e o ângulo de fase:

$$
\phi(u,v)=\arctan\left(\frac{I(u,v)}{R(u,v)}\right)
$$

- $R(u,v)$: parte real de $F(u,v)$;
- $I(u,v)$: parte imaginária de $F(u,v)$.

As componentes do espectro de frequências determinam as amplitudes das senóides que se combinam para formar a imagem resultante. Uma grande amplitude em determinada frequência, implica em maior proeminência, na imagem, de uma senóide nessa frequência. O contrário também é válido. As componentes de fase são menos intuitivas, mas são tão importantes quanto o espectro de frequências. A fase é uma medida do deslocamento das várias senóides em relação à sua origem - é um arranjo de ângulos que apresentam grande parte das informações sobre a localização dos objetos discerníveis na imagem. 

---

## Introdução à Transformada de Fourier Utilizando Python ## 

Funções de tranformada de Fourier utilizam algoritmos como Fast Fourier Transform (FFT) para o cálculo. Em python, a biblioteca Numpy fornece uma função pronta para a transformação considerando uma imagem (2D) np.fft.fft2. Também oferece uma função para o deslocamento np.fft.fftshift - deixando o espectro centralizado (menores frequências no centro do espectro). Elas podem ser implementadas da seguinte forma: 
```python
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift)+1.)
```
A função de transformada retorna uma matriz com números complexos, assim como esperado. Para cálculo da magnitude, a função np.abs, em caso de números complexos  a+bj , retorna o resultado conforme:

$$
\sqrt{(a^2 + b^2)}
$$

Como as amplitudes do espectro variam em um range muito grande e não equalizado, é necessário ajustar o contraste para que seja possível visualizar em um plot. Por esse motivo, faz-se uma transformação logarítma.

> [!CAUTION]
> * Essa transformação é aplicada apenas para efeito de visualização. **NÃO** aplique a transformada de Fourier inversa na amplitude do sinal! (veremos isso em breve...)
> * Soma-se um valor pequeno, por exemplo "1", às magnitudes encontradas, tal como no exemplo, pois intensidades de valor 0 gerariam erro quando o log fosse calculado.

--- 

## Exemplo 01 - Cálculo da Transformada de Fourier de Múltiplas Figuras ## 

Um exemplo prático de um código para calcular a transformada de Fourier de Várias Figuras é: 
```python
def calcula_fourier(img):
  f = np.fft.fft2(img)
  f_shift = np.fft.fftshift(f)
  magnitude = 20*np.log(np.abs(f_shift)+1.)
  return f_shift, magnitude

def plota_imagem(img1, img2):
  plt.figure(figsize=(10,10))
  plt.subplot(1,2,1)
  plt.imshow(img1, cmap='gray')
  plt.subplot(1,2,2)
  plt.imshow(img2, cmap='gray')
  plt.show()

## --- Carregnado as Imagens --- ##
circulo = cv.imread('circulo.tif', cv.IMREAD_UNCHANGED)
faixa_horizontal = cv.imread('faixahorizontal.tif', cv.IMREAD_UNCHANGED)
faixa_vertical = cv.imread('faixavertical.tif', cv.IMREAD_UNCHANGED)
losango = cv.imread('losango.tif', cv.IMREAD_UNCHANGED)
quadrado = cv.imread('quadrado.tif', cv.IMREAD_UNCHANGED)
retangulo_vertical = cv.imread('retangulovertical.tif', cv.IMREAD_UNCHANGED)
retangulo_horizontal = cv.imread('retangulohorizontal.tif', cv.IMREAD_UNCHANGED)
vret_sim = cv.imread('vret_sim.tif', cv.IMREAD_UNCHANGED)
hret_sim = cv.imread('hret_sim.tif', cv.IMREAD_UNCHANGED)
parallelogram = cv.imread('parallelogram.tif', cv.IMREAD_UNCHANGED)
parallelogram_2 = cv.imread('parallelogram_2.tif', cv.IMREAD_UNCHANGED)

## --- Calculando a transformada de Fourier --- ##
fft_circulo, magnitude_circulo = calcula_fourier(circulo)
fft_faixa_horizontal, magnitude_faixa_horizontal = calcula_fourier(faixa_horizontal)
fft_faixa_vertical, magnitude_faixa_vertical = calcula_fourier(faixa_vertical)
fft_losango, magnitude_losango = calcula_fourier(losango)
fft_quadrado, magnitude_quadrado = calcula_fourier(quadrado)
fft_retangulo_vertical, magnitude_retangulo_vertical = calcula_fourier(retangulo_vertical)
fft_retangulo_horizontal, magnitude_retangulo_horizontal = calcula_fourier(retangulo_horizontal)
fft_vret_sim, magnitude_vret_sim = calcula_fourier(vret_sim)
fft_hret_sim, magnitude_hret_sim = calcula_fourier(hret_sim)
fft_parallelogram, magnitude_parallelogram = calcula_fourier(parallelogram)
fft_parallelogram_2, magnitude_parallelogram_2 = calcula_fourier(parallelogram_2)

## --- Plotando os resultados --- ##
plota_imagem(circulo, magnitude_circulo)
plota_imagem(faixa_horizontal, magnitude_faixa_horizontal)
plota_imagem(faixa_vertical, magnitude_faixa_vertical)
plota_imagem(losango, magnitude_losango)
plota_imagem(quadrado, magnitude_quadrado)
plota_imagem(retangulo_vertical, magnitude_retangulo_vertical)
plota_imagem(retangulo_horizontal, magnitude_retangulo_horizontal)
plota_imagem(vret_sim, magnitude_vret_sim)
plota_imagem(hret_sim, magnitude_hret_sim)
plota_imagem(parallelogram, magnitude_parallelogram)
plota_imagem(parallelogram_2, magnitude_parallelogram_2)
```

Para resolver esse mesmo exercício de uma maneira muito mais otimizada (sem termos que ficar nesse "hardcoding"), podemos resolvê-lo da seguinte forma: 
```python
## Definindo as Funções ## 
def calcula_fourier(img):
  f = np.fft.fft2(img)
  f_shift = np.fft.fftshift(f)
  magnitude = 20*np.log(np.abs(f_shift)+1.)
  return f_shift, magnitude

def plota_imagem(img1, img2):
  plt.figure(figsize=(10,10))
  plt.subplot(1,2,1)
  plt.imshow(img1, cmap='gray')
  plt.subplot(1,2,2)
  plt.imshow(img2, cmap='gray')
  plt.show()

## Código Principal ##

imagens = ['circulo.tif', 'faixahorizontal.tif', 'faixavertical.tif', 'losango.tif', 'quadrado.tif', 'retangulovertical.tif', 'retangulohorizontal.tif', 'vret_sim.tif', 'hret_sim.tif', 'parallelogram.tif', 'parallelogram_2.tif']

for imagem in imagens:
  img = cv.imread(imagem, cv.IMREAD_UNCHANGED)
  fft, magnitude = calcula_fourier(img)
  plota_imagem(img, magnitude)
```

Muito mais simples, né ? =) 

---

## Como calcular a Transformada Inversa de Fourier ? (IFFT) ## 

Tibério, beleza, já calculei a transformada de fourier da minha imagem e apliquei algum filtro nela no domínio da frequência. O que eu preciso fazer com o resultado agora ? Precisa obter a imagem no espaço novamente =) 

Para isso, usamos a IFFT! 
