# Processamento Digital de Imagem - Anotações

## Métodos de Transformação Ponto a Ponto ## 

Quando estamos realizando transformações ponto a ponto, algumas informações sobre as imagens são extremamente importantes. Neste tópico, veremos transformaçõs utilizando: 

* Histograma;
* Transformações Lineares;
* Transformações Não-Lineares.

## Histogramas ##

O histograma de uma imagem em tons de cinza é uma função H(n) que produz o número de ocorrências de cada nível de cinza de uma imagem. No caso: 

$$
0 <= n <= L-1
$$

 Onde L é o tamanho da imagem. O histograma é de extrema importância para compreendermos a distribuição dos píxeis da imagem (ou seja, se uma imagem contém píxeis com um nível de cinza menor ou maior), além de ajudar na identificação de qual método de transformação (linear ou não), deverá ser aplicado para melhor visualização da imagem. 

 Vale ressaltar que o histograma não trás informações sobre a posição dos pixels, mas sim, somente a sua distruibuição (é uma função de distribuição de probabilidades). Abaixo, temos alguns exemplos de histogramas: 
[Exemplo de um Histograma](./images_teoria/histograma_1.png)
