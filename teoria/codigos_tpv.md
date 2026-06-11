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
  kernel = np.ones((tamanho,tamanho))/(tamanho**2)
  return kernel

def plota_imagem(imagem, nome):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  shape = imagem.shape
  plt.title(f'{nome}. Dimensão: {shape}')
  plt.show()

## Parte 01 ##
img = cv.imread('coins_noisy.tif', -1)
img = img.astype('float')
filtro3 = cria_kernel(3)
filtro9 = cria_kernel(9)
filtro12 = cria_kernel(12)
g1 = cv.filter2D(img, -1, filtro3)
g2 = cv.filter2D(img, -1, filtro9)
g3 = cv.filter2D(img, -1, filtro12)
plota_imagem(img, 'Imagem Original')
plota_imagem(g1, 'Saída com Filtro 3x3')
plota_imagem(g2, 'Saída com Filtro 9x9')
plota_imagem(g3, 'Saída com Filtro 12x12')
```
## 2. Filtro Passa  Alta ## 
