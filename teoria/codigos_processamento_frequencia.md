# Como realizar o processamento de imanges no domínio da frequência ? # 
---
A filtragem no domínio da frequência consiste em modificar a transformada de Fourier de uma imagem e depois calcular a transformada inversa para obter o resultado processado.

O grau de dificuldade na construção dos filtros diminui quando se trabalha no domínio da frequência, entretanto, a proximidade dos períodos na convolução pode causar o erro de wraparound (efeito de borda). Para solucionar esse problema, é necessário fazer um padding na imagem - lembrando que algoritmos DFT tendem a executar mais rapidamente arranjos de tamanho par, ou seja, normalmente se utiliza o dobro das dimensões M e N da imagem.
