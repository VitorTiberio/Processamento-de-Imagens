# Como realizar o processamento de imanges no domínio da frequência ? # 
---
A filtragem no domínio da frequência consiste em modificar a transformada de Fourier de uma imagem e depois calcular a transformada inversa para obter o resultado processado.

O grau de dificuldade na construção dos filtros diminui quando se trabalha no domínio da frequência, entretanto, a proximidade dos períodos na convolução pode causar o erro de wraparound (efeito de borda). Para solucionar esse problema, é necessário fazer um padding na imagem (lembrando que algoritmos DFT tendem a executar mais rapidamente arranjos de tamanho par, ou seja, normalmente se utiliza o dobro das dimensões M e N da imagem). A fim de preservar informações sobre as bordas, normalmente utiliza-se do padding simétrico, e não o padding com zeros. 

Para realizar esse preenchimento, a função np.fft.ff2 oferece, por meio do parâmetro s, a opção de preenchimento (padding), sendo (Mf,Nf) normalmente igual a (2M, 2N) tal que M e N representam as dimensões da imagem, como demonstrado abaixo: 

```python
f = np.fft.fft2(img,s=(Mf,Nf))
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift)+1.)
```

>[!CAUTION]
>Note as novas dimensões do espectro de frequência. Após a transformada inversa, será necessário recortar a imagem, resultando na imagem com as dimensões originais M e N, descartando as informações adjacentes.

--- 

## Filtro passa-baixa e passa alta no domínio da frequência ## 

Bordas e outras transições abruptas de intensidade (como o ruído) em uma imagem contribuem significativamente para o conteúdo de alta frequência de sua transformada de Fourier. Dessa forma, a suavização (borramento) é obtida no domínio da frequência pela atenuação das altas frequências, utilizando o filtros passa-baixa. 

Os filtros podem ser projetados de forma a apresentar transições mais abruptas ou mais suavizadas. Consideraremos apenas os filtros radialmente simétricos (deslocamento de fase zero) sendo D0 o raio a partir da origem e n a ordem do filtro, temos três "modelos" possíveis de filtos. 

---

### 1. Filtro Ideal ###

O filtro ideal possui uma transição abrupta entre a região de passagem e a de rejeição.

$$
H_{LP_{\text{Ideal}}}(u,v) =
\begin{cases}
1, & \text{se } D(u,v) \leq D_0 \\
0, & \text{se } D(u,v) > D_0
\end{cases}
$$

onde:

- $D(u,v)$ é a distância entre o ponto $(u,v)$ e o centro do espectro;
- $D_0$ é a frequência de corte.

> [!NOTE]
> O filtro ideal produz uma transição instantânea na frequência, podendo gerar o efeito de **ringing (Fenômeno de Gibbs)** na imagem filtrada.

---

### 2. Filtro Passa-Baixa Butterworth ###

O filtro Butterworth apresenta uma transição suave entre a banda de passagem e a banda de rejeição.

$$
H_{LP_{\text{Butterworth}}}(u,v) =
\frac{1}{1+\left[\frac{D(u,v)}{D_0}\right]^{2n}}
$$

onde:

- $D(u,v)$ é a distância ao centro da frequência;
- $D_0$ é a frequência de corte;
- $n$ é a ordem do filtro.

> [!TIP]
> Quanto maior o valor de $n$, mais a resposta do filtro se aproxima do filtro ideal.

---

### 3. Filtro Passa-Baixa Gaussiano ###

O filtro Gaussiano possui uma resposta completamente suave, eliminando praticamente o efeito de ringing.

$$
H_{LP_{\text{Gaussiano}}}(u,v) =
e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

onde:

- $D(u,v)$ é a distância ao centro da frequência;
- $D_0$ é a frequência de corte.

> [!IMPORTANT]
> O filtro Gaussiano é amplamente utilizado em Processamento Digital de Imagens devido à sua transição suave e à ausência de oscilações na imagem filtrada.

--- 

## Como determinar a frequência de corte de uma imagem com base em uma digitalização de X DPI ? ## 

Vamos supor que queremos calcular a frequência de corte a partir de uma digitalização realizada, por exemplo, de 300 DPI. O primeiro passo é realizar a conversão da resolução para o tamanho físico de um pixel. 

Sabemos que: 

$$
1 polegada = 25,4mm
$$

Logo, para uma resolução de 300 DPI:

$$
\Delta{x} = \frac{25,4}{300} = 0,08467 mm/pixel
$$

Ou seja, 

$$
\Delta{x} = 0,08467 mm/pixel
$$

Com esse dado, conseguimos calcular a frequência de Nyquist (maior frequência espacial que pode ser representada): 

$$
f_{n} = \frac{1}{2\Delta{x}}
$$

$$
f_{n} = \frac{1}{2 \times 0,08467} = 5,91 ciclos/mm
$$

Agora, imagine uma situação em que você está fazendo um exercício e o enunciado te fala: "utilize uma frequência de corte de 2 ciclos/mm". O que eu faço agora, Tibério ? 

Quando você está nessa situação, devemos aplicá-la da seguinte forma: 

$$
D_{0} = f_{c} \times (Mf\Delta{x})
$$

Onde: 
* fc é a frequência de corte desejada (ciclos/mm);
* Delta_x é o valor que calculamos anteriormente (25,4/DPI);
* Mf = tamanho da imagem (ou da imagem com padding) na direção considerada

Uma maneira de calcularmos D0 através do Python é pela função abaixo: 

```python
def calcula_fcorte(DPI, fc_mm, Mf, Nf):
  pixels_por_mm = DPI/25.4
  fc_pixel = fc_mm / pixels_por_mm ## frequencia de corte em ciclos/pixel
  D0 = (fc_pixel )*min(Mf, Nf)
  return D0
```

--- 

# Aplicação dos Filtros em Python # 

Agora, com toda a bagagem teórica que vimos até agora, podemos realizar o processamento das imagens no domínio da frequência. 

Primeiramente, vamos definir uma função "universal", que será responsável por calcular a transformada de fourier (com padding) das nossas imagens. A mesma pode ser consultada abaixo: 

```python
def calcula_transformada_fourier(img):
  '''
  Função que calcula a transformada de Fourier de uma imagem.
  img = imagem a ser processada.
  '''
  M, N = np.shape(img) ## M,N = dimensões da imagem original
  Mf = 2*M ## dobra as dimensões da imagem original
  Nf = 2*N
  f = np.fft.fft2(img,s=(Mf,Nf)) ## calcula a fft considerando o padding
  fshift = np.fft.fftshift(f) ## faz o shift na fft
  magnitude_spectrum = 20*np.log(np.abs(fshift)+1.) ## calcula o espectro de frequências (magnitude), para plot
  return Mf, Nf, fshift, magnitude_spectrum ## devolve o tamanho Mf, Nf (pós padding), fshift (para cálculo da inversa posteriormente) e o espectro de frequências
```

Outra função que usamos bastante é a função de plot das imagens, definida abaixo: 
```python
def plota_imagem(img, titulo):
  '''
  Função que plota a imagem.
  img = imagem que receberá o plot;
  titulo = titulo que será colocado no plot.
  '''
  plt.figure(figsize=(5,5))
  plt.title(titulo)
  plt.imshow(img, cmap='gray')
  plt.show()
```

Um pequeno lembrete de como devemos implementar o código "principal" para calcular a Transformada de Fourier de uma Imagem =) 

```python
img = cv.imread('towerbridge.tif', cv.IMREAD_UNCHANGED) ## Carrega a imagem "towerbridge.tif"
Mf, Nf, fshift, magnitude = calcula_transformada_fourier(img) ## calcula a transformada de fourier
plota_imagem(img, "Imagem Original") ## Plota a Imagem Original
plota_imagem(magnitude, "Espectro de Frequência") ## Plota a Imagem no domínio da frequência
```

--- 

### Implementação do Filtro Passa Baixa Ideal ### 

Considerando um filtro que possui uma frequência de corte igual a 1,5 ciclos/mm e considerando que a imagem foi digitalizada em 300 DPI, temos: 

```python
def passa_baixa_ideal(Mf, Nf, fshift, fcorte):
  '''
  Função que realiza a filtragem da Imagem Original com um Filtro Passa Baixa Ideal.
  A Saída dessa função é a imagem filtrada e o filtro utilizado.
  Mf, Nf = dimensões da imagem pós padding;
  fshift = transformada de fourier da imagem original;
  fcorte = frequência de corte a ser colocada no filtro.
  '''
  cx = Nf//2
  cy = Mf//2
  D0 = fcorte
  filtro = np.zeros((Mf,Nf))
  for i in range(Mf):
    for j in range(Nf):
      if np.sqrt((i-cx)**2 + (j-cy)**2) <= D0:
        filtro[i,j] = 1
      else:
        filtro[i,j] = 0
  fshift_filtrado = fshift*filtro
  f_ishift = np.fft.ifftshift(fshift_filtrado)
  img_back = np.fft.ifft2(f_ishift)
  img_back = np.abs(img_back)
  img_back = img_back[0:(Mf//2), 0:(Nf//2)]
  return img_back, filtro

## Código Principal ##
img = cv.imread('towerbridge.tif', cv.IMREAD_UNCHANGED) ## Carrega a imagem "towerbridge.tif"
Mf, Nf, fshift, magnitude = calcula_transformada_fourier(img) ## Calcula a transformada de Fouerier da Imagem
plota_imagem(img, "Imagem Original") ## Plota a Imagem Original
plota_imagem(magnitude, "Espectro de Frequência") ## Plota a Imagem no domínio da frequência
D0 = calcula_fcorte(300, 1.5, Mf, Nf) ## Calcula a frequência de corte -- trabalhando nessa função
fshift_filtrado, filtro_pb_ideal = passa_baixa_ideal(Mf, Nf, fshift, D0) ## aplica o filtro passa baixa ideal no domínio da frequência
plota_imagem(filtro_pb_ideal, "Filtro Ideal") ## Plota o Filtro Ideal
plota_imagem(fshift_filtrado, "Imagem Filtrada - Filtro Passa Baixa Ideal") ## Plota a imagem filtrada com o filtro passa baixa ideal
```

---

### Implementação do Filtro Passa Baixa Butterworth ### 

```python
def filtragem_frequencia_pb_butterworth(Mf, Nf, fshift, fcorte, ordem):
  '''
  Função que realiza a filtragem da Imagem Original com um Filtro Passa Baixa do tipo Butterworth.
  A Saída dessa função é a imagem filtrada e o filtro utilizado para tal.
  Mf, Nf = dimensões da imagem pós padding;
  fshift = transformada de fourier da imagem original;
  fcorte = frequência de corte a ser colocada no filtro;
  ordem = ordem do filtro.
  '''
  cx = Nf//2 ## calcula o centro na coordenada "x"
  cy = Mf//2 ## calcula o centro na coordenada "y"
  D0 = fcorte ## define a frequência de corte (D0)
  filtro = np.zeros((Mf,Nf)) ## cria um filtro de zeros (matriz preenchida de zeros)
  for i in range(Mf):
    for j in range(Nf): ## percorre todos os elementos da matriz
      D = np.sqrt((i-cx)**2 + (j-cy)**2) ## definição do valor de D(u,v)
      filtro[i,j] = 1 / (1 + (D/D0)**(2*ordem)) ## definição do filtro de butterworth

  fshift_filtrado = fshift*filtro ## aplica o filtro (multiplicação na frequência é a convolução no tempo)
  f_ishift = np.fft.ifftshift(fshift_filtrado) ## aplica a IFFT Shift na FFT Shift
  img_back = np.fft.ifft2(f_ishift) ## aplica a ifft (retorna a imagem p/ o domínio do tempo)
  img_back = np.abs(img_back) ## pega os valores absolutos
  img_back = img_back[0:(Mf//2), 0:(Nf//2)] ## recorta a imagem do tamanho original (remove o padding)
  return img_back, filtro

## Código Principal ##

img = cv.imread('towerbridge.tif', cv.IMREAD_UNCHANGED) ## Carrega a imagem "towerbridge.tif"
Mf, Nf, fshift, magnitude = calcula_transformada_fourier(img) ## Calcula a transformada de Fouerier da Imagem
plota_imagem(img, "Imagem Original") ## Plota a Imagem Original
plota_imagem(magnitude, "Espectro de Frequência") ## Plota a Imagem no domínio da frequência
D0 = calcula_fcorte(300, 1.5, Mf, Nf) ## Calcula a frequência de corte
fshift_filtrado, filtro_pb_butterworth = filtragem_frequencia_pb_butterworth(Mf, Nf, fshift, D0, 2)
plota_imagem(filtro_pb_butterworth, "Filtro Butterworth")
plota_imagem(fshift_filtrado, "Imagem Filtrada - Filtro Butterworth")
```

--- 

### Implementação do Filtro Passa Baixa Gaussiano ### 

```python
def filtragem_frequencia_pb_gaussiano(Mf, Nf, fshift, fcorte):
  '''
  Função que realiza a filtragem da Imagem Original com um Filtro Passa Baixa Gaussiano.
  A Saída dessa função é a imagem filtrada e o filtro utilizado.
  Mf, Nf = dimensões da imagem pós padding;
  fshift = transformada de fourier da imagem original;
  fcorte = frequência de corte a ser colocada no filtro.
  '''
  cx = Nf//2
  cy = Mf//2
  D0 = fcorte
  filtro = np.zeros((Mf,Nf))
  for i in range(Mf):
    for j in range(Nf):
      D = np.sqrt((i-cy)**2 + (j-cx)**2)
      filtro[i,j] = np.exp(-(D**2)/(2*(D0**2))) ## definição do filtro passa baixa gaussiano
  fshift_filtrado = fshift*filtro
  f_ishift = np.fft.ifftshift(fshift_filtrado)
  img_back = np.fft.ifft2(f_ishift)
  img_back = np.abs(img_back)
  img_back = img_back[0:(Mf//2), 0:(Nf//2)]
  return img_back, filtro

## Código Principal ##
img = cv.imread('towerbridge.tif', cv.IMREAD_UNCHANGED) ## Carrega a imagem "towerbridge.tif"
Mf, Nf, fshift, magnitude = calcula_transformada_fourier(img) ## Calcula a transformada de Fouerier da Imagem
plota_imagem(img, "Imagem Original") ## Plota a Imagem Original
plota_imagem(magnitude, "Espectro de Frequência") ## Plota a Imagem no domínio da frequência
D0 = calcula_fcorte(300, 1.5, Mf, Nf) ## Calcula a frequência de corte
fshift_filtrado, filtro_pb_gaussiano = filtragem_frequencia_pb_gaussiano(Mf, Nf, fshift,D0)
plota_imagem(filtro_pb_gaussiano, "Filtro Gaussiano")
plota_imagem(fshift_filtrado, "Imagem Filtrada - Filtro Gaussiano")
```


