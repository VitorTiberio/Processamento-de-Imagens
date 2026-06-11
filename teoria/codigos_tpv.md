# Como realizar uma transformação por vizinhança em Python ? # 

## 1. Filtro Passa Baixa ## 

Antes de qualquer aplicação, é importante relembrarmos das principais características de um filtro passa baixa no domínio do espaço. Portanto, primeiramente, ele é implementado através de uma máscara que realiza a média da vizinhança e obedece essas duas condições: 
* Possui todos os pesos de seu Kernel positivos;
* A soma de todos os seus elementos tem que ser igual a 1.

> [!WARNING]
> Quanto **MAIOR** for o template, **MENOR** será a frequência de corte do mesmo.

Tendo em mente que o procedimento de filtragem no domínio do espaço é realizado através de uma convolução da imagem com o filtro em questão, primeiramente, precisamos entender como realizamos isso no Python. Para tal tarefa, utiliza-se o "cv.filter2D", exemplificado abaixo: 

```python
cv.filter2D(img, -1, kernel)
```
Onde img é a imagem, -1 é um valor "padrão" (que sempre é o mesmo) e kernel é o filtro desenvolvido.

---

Agora, vamos supor que temos uma imagem "tiberio.png". Essa imagem está contaminada com um ruído gaussiano de média zero e desvio padrão de 40. Implemente um código que faça a atenuação do ruído dessa imagem, com três tamanhos de filtros diferentes: 
* Filtro da média 3x3;
* Filtro da média 9x9;
* Filtro da média 12x12.

Considere que o kernel seja sempre uma matriz de 1 normalizada. 

Podemos resolver esse exercício da seguinte maneira: 

```python
## Definindo as Funções ##
def cria_kernel(tamanho):
'''
Cria um kernel de um filtro passa baixa (filtro da média). Nesse caso, é uma matriz de 1's normalizada.
tamanho = dimensão do kernel
'''
  kernel = np.ones((tamanho,tamanho))/(tamanho**2)
  return kernel

def plota_imagem(imagem, nome):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  plt.title(nome)
  plt.show()


## Código Principal ## 
img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED) ## realiza a relitura da imagem
img = img.astype('float') ## converte a imagem para o tipo "float"
filtro3 = cria_kernel(3) ## cria o kernel 3x3 
filtro9 = cria_kernel(9) ## cria o kernel 9x9 
filtro12 = cria_kernel(12) ## cria o kernel 12x12
g1 = cv.filter2D(img, -1, filtro3) ## realiza a convolução da imagem com o kernel 3x3
g2 = cv.filter2D(img, -1, filtro9) ## realiza a convolução da imagem com o kernel 9x9 
g3 = cv.filter2D(img, -1, filtro12) ## realiza a convolução da imagem com o kernel 12x12

## Plot das Imagens ## 
plota_imagem(img, 'Imagem Original')
plota_imagem(g1, 'Saída com Filtro 3x3')
plota_imagem(g2, 'Saída com Filtro 9x9')
plota_imagem(g3, 'Saída com Filtro 12x12')
```
> [!WARNING]
> Ao trabalhar com filtros convolucionais, é essencial garantir que a imagem a ser filtrada seja de um tipo de variável que contemple números "quebrados" (tipo float). Sendo assim, ao ler a imagem (cv.imread), é necessário converter essa imagem para o tipo "float", utilizando o comando: **img.astype('float')** ou **cv.imread('tiberio.png',cv.IMREAD_UNCHANGED).astype('float')**
> A imagem de saída (g1,g2 e g3) devem ser convertidas novamente para "uint8" para serem plotadas. Isso pode ser feito assim: g1 = g1.astype('uint8')

## 2. Filtro Passa  Alta ## 

### 2.1 Aplicações Gerais ###

Em relação à filtragem espacial com um filtro passa alta, assim como no passa baixa, primeiramente precisamos compreender como é a estrutura do filtro. 
No caso, determinamos que um filtro é passa alta se: 
* O kernel possui pesos negativos;
* A soma dos elementos internos deve ser igual a zero.

É importante ressaltar que o filtro passa alta detecta na imagem os detalhes finos e mudanças abruptas de níveis de cinza na imagem. 

Um exemplo de aplicação pode ser consultado abaixo: 
```python
def plota_imagem(imagem, nome):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  shape = imagem.shape
  plt.title(f'{nome}. Dimensão: {shape}')
  plt.show()

## Código Principal ## 
img = cv.imread('tiberio.png', cv.IMREAD_UNCHANGED)
plota_imagem(img, 'Imagem Original')
kernel = np.array(((-1, -1, -1),
                    (-1, 8, -1),
                    (-1, -1, -1))) / 9
img_out = cv.filter2D(img, -1, kernel)
plota_imagem(img_out, 'Imagem com filtro passa alta')
```

### 2.2 Filtro de Sharpness (Aumento da nitidez da imagem) ###

Uma das aplicações que podemos fazer com o filtro passa alta é o aumento da nitidez das imagens. Isso pode ser aplicado da seguinte maneira: 
```python
kernel_nitidez = np.array(((-1, -1, -1),
                    (-1, 17, -1),
                    (-1, -1, -1))) / 9
img_nitida = cv.filter2D(img, -1, kernel_nitidez)
plota_imagem(img_nitida, 'Imagem com Filtro de Aguçamento')
```
Para montar o kernel de nitidez, somou-se o filtro passa alta com a imagem original. Considerando que o filtro passa alta era composto por: 

```text
1     [-1  -1  -1
─  ·   -1   8  -1
9      -1  -1  -1]
```

Logo, uma matriz que se multiplicarmos a imagem não vai acontecer nada (vai sair a própria imagem) pode ser escrita como:
```text
1     [0 0 0
─  ·   0 9 0
9      0 0 0]
```                                                     
Portando, se ambas forem somadas, obtêm-se:
```text
1     [-1  -1  -1
─  ·   -1   17 -1
9      -1  -1  -1]
```
Que no caso, torna-se o kernel de nitidez (ou sharpness). 
