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
> Essa transformação é aplicada apenas para efeito de visualização. **NÃO** aplique a transformada de Fourier inversa na amplitude do sinal! (veremos isso em breve...)
> Soma-se um valor pequeno, por exemplo "1", às magnitudes encontradas, tal como no exemplo, pois intensidades de valor 0 gerariam erro quando o log fosse calculado.
