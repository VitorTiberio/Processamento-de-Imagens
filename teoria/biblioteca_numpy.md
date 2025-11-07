# 📘 Resumo da Biblioteca NumPy

O **NumPy** (Numerical Python) é a principal biblioteca para **computação científica em Python**, oferecendo suporte para **arrays multidimensionais** e uma ampla coleção de funções matemáticas de alto desempenho. É amplamente utilizada em ciência de dados, engenharia, aprendizado de máquina, visão computacional e outras áreas que exigem processamento numérico eficiente.

---

## 🚀 Principais Características
- **Array multidimensional (`ndarray`)**: estrutura central do NumPy, mais eficiente que listas nativas do Python.  
- **Operações vetorizadas**: elimina loops explícitos, tornando o código mais rápido e conciso.  
- **Broadcasting**: permite operações entre arrays de diferentes dimensões de forma automática.  
- **Funções matemáticas otimizadas**: álgebra linear, transformadas de Fourier, estatísticas, funções trigonométricas, entre outras.  
- **Integração**: compatível com bibliotecas como Pandas, SciPy, Matplotlib, TensorFlow, PyTorch.  

---

## 🧩 Estrutura Principal: `ndarray`
O **`numpy.ndarray`** é um array homogêneo (mesmo tipo de dado), que suporta operações em múltiplas dimensões.

### Criação de Arrays
```python
import numpy as np

a = np.array([1, 2, 3])           # Array 1D
b = np.array([[1, 2], [3, 4]])    # Array 2D
c = np.zeros((3, 3))              # Matriz de zeros
d = np.ones((2, 2))               # Matriz de uns
e = np.eye(3)                     # Matriz identidade
f = np.arange(0, 10, 2)           # Intervalo [0,10) com passo 2
g = np.linspace(0, 1, 5)          # 5 pontos entre 0 e 1
```
## 🔎 Atributos Importantes
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.ndim      # Número de dimensões
arr.shape     # Formato (linhas, colunas)
arr.size      # Quantidade de elementos
arr.dtype     # Tipo dos elementos
arr.itemsize  # Tamanho em bytes de cada elemento
```

## ⚡ Operações Básicas
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b         # [5 7 9]
a * b         # [ 4 10 18]
a ** 2        # [1 4 9]
np.dot(a, b)  # Produto escalar (32)
```
## 🎯 Indexação e Fatiamento
```python
arr = np.array([[10, 20, 30], [40, 50, 60]])

arr[0, 1]       # Elemento da 1ª linha, 2ª coluna -> 20
arr[:, 1]       # Toda a 2ª coluna -> [20 50]
arr[1, :]       # Toda a 2ª linha -> [40 50 60]
arr[0:2, 1:3]   # Submatriz -> [[20 30], [50 60]]
```
## 🧮 Funções Matemáticas
```python
x = np.array([1, 2, 3, 4])

np.mean(x)   # Média
np.std(x)    # Desvio padrão
np.sum(x)    # Soma
np.min(x)    # Valor mínimo
np.max(x)    # Valor máximo
np.sqrt(x)   # Raiz quadrada
```
## 🔄 Broadcasting
```python
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])

a + b
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]
```
## 🏗️ Álgebra Linear
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.dot(A, B)          # Produto matricial
np.linalg.det(A)      # Determinante
np.linalg.inv(A)      # Inversa
np.linalg.eig(A)      # Autovalores e autovetores
```
## 🔀 Manipulação de Arrays
```python
arr = np.arange(12).reshape(3, 4)

arr.T            # Transposta
arr.ravel()      # "Achatar" em 1D
np.hstack((arr, arr)) # Concatenar horizontalmente
np.vstack((arr, arr)) # Concatenar verticalmente
```
