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
