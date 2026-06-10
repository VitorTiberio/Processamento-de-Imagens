# Como realizar uma transformação ponto a ponto no domínio do espaço utilizando Python ? # 

## Transformação de Intensidades ## 

### 1. Transformação Linear ###

As técnicas de processamento no domínio espacial operam diretamente nos pixels da imagem. A expressão geral para a função de transformação nos níveis de cinza pode ser dada por:

$$
g(x,y) = T[f(x,y)]
$$

sendo:

- $f(x,y)$ a imagem de entrada;
- $g(x,y)$ a imagem de saída ou imagem processada;
- $T$ um operador aplicado sobre $f$.

Um exemplo de função de transformação é a **transformação linear**, dada por:

$$
g(x,y) = c \cdot f(x,y) + b
$$

onde:

- $c$ é uma constante responsável pelo ajuste de **contraste**;
- $b$ é uma constante responsável pelo ajuste de **brilho**.

> [!NOTE]
> Quando $c > 1$, o contraste da imagem aumenta.
>
> Quando $0 < c < 1$, o contraste da imagem diminui.
>
> Valores positivos de $b$ aumentam o brilho da imagem, enquanto valores negativos o reduzem.

Um exemplo de aplicação de uma transformação linear é quando queremos alargar um histograma para aumentar o contraste da imagem. No caso, temos: ]
```python
def plota_imagem(img, titulo):
  plt.figure(figsize=(5,5))
  plt.title(titulo)
  plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255)
  plt.show()
  plt.hist(img.flatten(),bins=100,density=False,range=(0,255))
  plt.show()
img = cv.imread('tiberio.png',cv.IMREAD_UNCHANGED)
img = img.astype(np.uint8)
plota_imagem(img, "Imagem Original")
A = img.min() # nível de cinza mínimo da imagem
B = img.max() # nível de cinza máximo da imagem
img_out = (img - A)*(255/(B-A))
plota(img_out, "Imagem pós alargamento de histograma")
```
--- 

### 2. Transformação Não-Linear ### 

Agora, iremos analisar algumas transformações não lineares. Um exemplo clássico é a **transformação logarítmica (log)**. Sua fórmula geral é dada por:

$$
g(x,y) = c \cdot \log\left(f(x,y) + 1\right)
$$

onde:

- $f(x,y)$ é a imagem de entrada;
- $g(x,y)$ é a imagem transformada;
- $c$ é uma constante de escala.

Essa transformação é frequentemente utilizada para expandir faixas de intensidade escuras da imagem e comprimir faixas mais claras, permitindo a visualização de detalhes em regiões de baixa intensidade.

> [!NOTE]
> A transformação logarítmica é amplamente empregada na visualização de espectros de Fourier, pois comprime a grande faixa dinâmica dos coeficientes de frequência.


<p align="center">
  <img src="images_teoria/transformacao_log.PNG" width="450">
</p>

<p align="center">
  <em>Figura 2: Exemplos de transformações ponto a ponto.</em><br>
  <em>Fonte: Gonzalez & Woods, Digital Image Processing (3rd ed.).</em>
</p>

---

Outro exemplo importante é a **transformação gamma**, dada por:

$$
g(x,y) = c \cdot f(x,y)^{\gamma}
$$

onde:

- $c$ é uma constante de escala;
- $\gamma$ (gamma) controla o formato da curva de transformação.

### Efeito do parâmetro $\gamma$

- Se $\gamma < 1$, regiões escuras da imagem são expandidas e tornam-se mais visíveis;
- Se $\gamma > 1$, regiões claras são favorecidas e regiões escuras são comprimidas;
- Se $\gamma = 1$, a transformação equivale à identidade.

> [!IMPORTANT]
> A correção gamma é amplamente utilizada em monitores, televisores, câmeras digitais e sistemas de exibição de imagens para compensar não linearidades dos dispositivos.

### Curvas para Diferentes Valores de Gamma

<p align="center">
  <img src="Processamento-deImagens/images_teoria/transformacao_gamma.PNG" width="450">
</p>

<p align="center">
  <em>Figura 3: Curvas para diferentes valores de γ.</em><br>
  <em>Fonte: Gonzalez & Woods, Digital Image Processing (3rd ed.).</em>
</p>

---

## Resumo

| Transformação | Equação | Aplicação |
|--------------|----------|------------|
| Logarítmica | $g(x,y)=c\log(f(x,y)+1)$ | Expansão de níveis escuros |
| Potência (Gamma) | $g(x,y)=c f(x,y)^\gamma$ | Ajuste de brilho e contraste não linear |

> [!TIP]
> Em Processamento Digital de Imagens, a transformação logarítmica aparece frequentemente na visualização da Transformada de Fourier, enquanto a transformação gamma é amplamente utilizada em dispositivos de captura e exibição de imagens.
