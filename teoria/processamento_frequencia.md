# 📘 Discretização de Sistemas 📘 #
> Este resumo contém informações referentes a processamento de Imagens no Domínio da Frequência. Aqui, teremos o desenvolvimento da teoria de filtros passa alta e baixa, assim como rejeita e passa banda.

# Filtragem sem alteração de fase # 

O filtro H(u,v) deve multiplicar a matriz complexa F(u,v) para garantir que a fase não seja alterada no processo de filtragem. Esse tipo de filtro é chamado de *zero-phase shift filters* 

# Filtos Passa-Baixa # 

O filtro passa-baixa retira (ou atenua) as ondas senoidas de alta frequência espacial (acima da frequência de corte $D_0$, definida na construção do filtro). Logo, será mantido somente as ondas senoidas de baixa-frequência espacial, ou sejam que estão abaixo da frequência de corte pré definida. 

>[!CAUTION]
>Não há aumento da amplitude de nenhuma onda senoidal no espectro de Fourier da Imagem.

Os filtros passa-baixa podem ser de vários tipos. Entre eles, podemos citar os filtros: Ideal, Butterworth e Gaussiano. 
