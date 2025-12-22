# Processamento de Imagens usando MATLAB

## Visão Geral
Este repositório contém um **resumo introdutório das principais funções de processamento de imagens em MATLAB**, seguindo o fluxo clássico de algoritmos de visão computacional. O objetivo é servir como referência rápida para estudos e projetos iniciais na área.

---

## Fluxo Básico de Processamento
Um algoritmo típico de processamento de imagens pode ser dividido em:
**Importação → Pré-processamento → Segmentação → Pós-processamento → Análise/Classificação**.

---

## Importação e Visualização
A etapa inicial consiste em carregar e visualizar as imagens. A função `imread` é utilizada para importar a imagem para o workspace, enquanto `imshow` permite sua visualização. Para comparação entre imagens ou entre diferentes etapas do processamento, podem ser usadas `imshowpair` e `montage`, que exibem duas ou múltiplas imagens simultaneamente.

---

## Pré-processamento
O pré-processamento tem como objetivo melhorar a qualidade da imagem e facilitar as etapas seguintes. A função `im2gray` converte imagens RGB para escala de cinza. A análise da distribuição de intensidades pode ser feita com `imhist`, enquanto `imadjust` é empregada para melhorar o contraste. Para filtragem e redução de ruído, filtros predefinidos são criados com `fspecial` e aplicados à imagem por meio de `imfilter`.

---

## Segmentação
A segmentação busca separar objetos de interesse do fundo da imagem. Uma abordagem simples e comum é a binarização, realizada com `imbinarize`, que converte a imagem em escala de cinza em uma imagem binária.

---

## Processamento Morfológico
Após a segmentação, operações morfológicas são usadas para refinar os resultados. A função `strel` define o elemento estruturante. A operação de abertura (`imopen`) é utilizada para remover pequenos ruídos, enquanto a operação de fechamento (`imclose`) preenche lacunas e conecta regiões próximas.

---

## Processamento em Lote de Imagens
Para trabalhar com grandes conjuntos de dados, `imageDatastore` permite organizar coleções de imagens de forma eficiente, e `readimage` possibilita a leitura individual de cada imagem do conjunto.

---

## Considerações Finais
As funções apresentadas formam a **base do processamento digital de imagens em MATLAB**, sendo amplamente aplicadas em visão computacional, reconhecimento de padrões e análise de imagens em engenharia.
