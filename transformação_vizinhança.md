# Transformação por Vizinhança #

Em relação às transformações por Vizinhança, iremos trabalhar com três tipos: 
1) Transformação por Convolução;
2) Transformação por Filtros Lineares;
3) Transformação por Máscara de Nitidez.

Antes de tratarmos especificamente sobre cada tipo de transformação por vizinhança, vamos entender do que a mesma se trata. Então um operador local (por vizinhança) combina a intensidade de um certo número de pixels para computar o valor da nova intensidade da Imagem de Saída, como demonstra a imagem abaixo: 

![Definição de Operador Local](./images_teoria/def_transf_vizinhanca.png)

Onde T[f(x,y)] é a operação sobre todos os píxels dentro da janela S centrada em f(x,y). 

É importante também relembrar a definição de convolução e correlação cruzada, definidas abaixo: 

$$f(x) * h(x) = \int_{-\infty}^{+\infty} f(m)h(x - m)dm$$

$$f(x) \star h(x) = \int_{-\infty}^{+\infty} f(m)h(x + m)dm$$

## Filtros no Domínio do Espaço ##

## Filtragem Espacial - Passa Baixa ## 

## Filtragem Espacial - Passa Alta ##

## Aplicação de Filtros passa-alta para aumento da nitidez (aguçamento) de imagens ## 

## Máscaras Isotrópicas ## 





