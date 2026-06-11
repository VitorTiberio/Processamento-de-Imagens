# Como realizar uma transformação por vizinhança em Python ? # 

## 1. Filtro Passa Baixa ## 

Antes de qualquer aplicação, é importante relembrarmos das principais características de um filtro passa baixa no domínio do espaço. Portanto, primeiramente, ele é implementado através de uma máscara que realiza a média da vizinhança e obedece essas duas condições: 
* Possui todos os pesos de seu Kernel positivos;
* A soma de todos os seus elementos tem que ser igual a 1.



## 2. Filtro Passa  Alta ## 
