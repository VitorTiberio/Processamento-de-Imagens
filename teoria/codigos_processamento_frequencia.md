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

Os filtros podem ser projetados de forma a apresentar transições mais abruptas ou mais suavizadas. Consideraremos apenas os filtros radialmente simétricos (deslocamento de fase zero) sendo D0 o raio a partir da origem e n a ordem do filtro, temos três "modelos" possíveis de filtos. Entre eles: 
