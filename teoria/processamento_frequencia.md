# 📘 Discretização de Sistemas 📘 #
> Este resumo contém informações referentes a processamento de Imagens no Domínio da Frequência. Aqui, teremos o desenvolvimento da teoria de filtros passa alta e baixa, assim como rejeita e passa banda.

# Filtragem sem alteração de fase # 

O filtro H(u,v) deve multiplicar a matriz complexa F(u,v) para garantir que a fase não seja alterada no processo de filtragem. Esse tipo de filtro é chamado de *zero-phase shift filters* 

# Filtos Passa-Baixa # 

O filtro passa-baixa retira (ou atenua) as ondas senoidas de alta frequência espacial (acima da frequência de corte $D_0$, definida na construção do filtro). Logo, será mantido somente as ondas senoidas de baixa-frequência espacial, ou sejam que estão abaixo da frequência de corte pré definida. 

>[!CAUTION]
>Não há aumento da amplitude de nenhuma onda senoidal no espectro de Fourier da Imagem.

Os filtros passa-baixa podem ser de vários tipos. Entre eles, podemos citar os filtros: Ideal, Butterworth e Gaussiano. 

## Filtro Passa-Baixa Ideal ## 

Definimos o filtro Passa-Baixa Ideal como: 

$$
H(u,v) =
\begin{cases}
1, & \text{se } D(u,v) \le D_0 \\
0, & \text{se } D(u,v) > D_0
\end{cases}
$$

Neste caso, todas as ondas senoidas de frequência acima da frequência de corte ($D_0$) são retiradas da imagem, enquanto as ondas de frequência mais baixas que $D_0$ não são alteradas. 

## Filtro Passa-Baixa Butterworth ## 

O filtro passa-baixa de Butterworth é definido por: 

$$
H(u,v) = \frac{1}{1 + \left[ \frac{D(u,v)}{D_0} \right]^{2n}}
$$

No caso, a frequência de corte $D_0$ define o valor onde a amplitude da onda é reduzida em 50%. Vale ressaltar também que as ondas de alta-frequência são cada vez mais atenuadas na imagem a medida que são maiores que $D_0$, ou seja, o filtro possui uma transição mais suave que o filtro ideal. 

O valor de **n** determina a suavidade do filtro. 

## Filtro Passa-Baixa Gaussiano ## 

Define-se o filtro Passa-Baixa Gaussiano com a seguinte expressão: 

$$
H(u,v) = e^{-\frac{[D(u,v)]^2}{2D_0^2}}
$$

Nele, a frequência de corte ($D_0$) define o valor onde a amplitude da onda é reduzida em 60,7%. Como o Butterworh, as ondas de alta-frequência são cada vez mais atenuadas na imagem, a medida que são maiores que a frequência de corte, ou seja, esse filtro possui transição mais suave que o ideial (e tende a ser bem mais suave que o Butterworth também). 

# Filtro Passa-Alta # 

O filtro passa-alta retira (ou atenua) as ondas senoidas de baixa frequência espacial (abaixo da frequência de corte $D_0$, definida na construção do filtro). Logo, será mantido somente as ondas senoidas de alta-frequência espacial, ou sejam que estão acima da frequência de corte pré definida. 

>[!CAUTION]
>Não há aumento da amplitude de nenhuma onda senoidal no espectro de Fourier da Imagem.

Os filtros passa-alta podem ser de vários tipos. Entre eles, podemos citar os filtros: Ideal, Butterworth e Gaussiano, de maneira semelhante aos Filtros Passa-Baixa. 

## Filtro Passa-Alta Ideal ## 

$$
H(u,v) =
\begin{cases}
0, & \text{se } D(u,v) \le D_0 \\
1, & \text{se } D(u,v) > D_0
\end{cases}
$$

No caso do filtro passa-alta ideial, todas as ondas senoidais de frequência abaixo da frequência de corte são retiradas da imagem, sendo que somente as ondas de frequência mais altas que $D_0$ não são alteradas. 

## Filtro Passa-Alta Butterworth ## 

Define-se a função H(u,v) do filtro de Butterworth como: 

$$
H(u,v) = \frac{1}{1 + \left[ \frac{D_0}{D(u,v)} \right]^{2n}}
$$

Neste caso, a frequência de corte define o valor onde a amplitude da onda senoidal é reduzida em 50%. Ondas de baixa frequência são cada vez mais atenuadas na imagem a medida que são menores que $D_0$, ou seja, o filtro possui transição mais suave que o filtro ideal. Igual ao Butterworth do passa-baixa, o valor de **n** determina a "suavidade" do filtro. 

## Filtro Passa-Alta Gaussiano ## 

No caso do filtro Gaussiano, o mesmo é definido por: 

$$
H(u,v) = 1 - e^{-\frac{[D(u,v)]^2}{2D_0^2}}
$$

A frequência de corte define o valor onde a amplitude da onda senoidal é reduzida em 60,7%. As ondas de baixa frequência são cada vez mais atenuadas na imagem a medida que são menores que $D_0$, ou seja, o filtro possui, assim como o filtro de Butterworth, uma transição mais suave que o filtro ideal. Vale ressaltar que o filtro Gaussiano pode ser bem mais suave que o filtro Butterworth. 
