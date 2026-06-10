# 📸  Aquisição de Imagens Digitais 📸

## Objetivos deste resumo

- Entender como uma imagem é formada;
- Compreender o processo de aquisição digital;
- Estudar amostragem e quantização;
- Analisar resolução espacial e resolução em níveis de cinza;
- Entender o funcionamento de sensores CCD e CMOS;
- Calcular armazenamento de imagens digitais.
> [!NOTE]
> Esse resumo foi feito através de uma Inteligência Artificial, com o objetivo de ser consultado somente para revisão de conceitos primordiais de aquisição de imagens digitais. 
---

# 1. Formação da Imagem

Uma imagem monocromática pode ser representada por uma função bidimensional:

$$
f(x,y)
$$

onde:

- $x$ e $y$ representam as coordenadas espaciais;
- $f(x,y)$ representa a intensidade luminosa (nível de cinza).

A intensidade observada é dada por:

$$
f(x,y)=i(x,y)\cdot r(x,y)
$$

onde:

- $i(x,y)$ → iluminação;
- $r(x,y)$ → refletância;
- $f(x,y)$ → intensidade da imagem.

---

# 2. Imagem Digital

Uma imagem digital é uma representação discreta de uma imagem contínua.

Ela é armazenada como uma matriz:

INSERIR IMAGEM COM A MATRIZ

Cada elemento da matriz corresponde a um **pixel**.

---

# 3. Pixel

**Pixel (Picture Element)** é a menor unidade de informação da imagem.

Cada pixel possui:

- uma posição $(x,y)$;
- um valor de intensidade $f(x,y)$.

Exemplo para uma imagem de 8 bits:

| Valor | Cor |
|---------|---------|
| 0 | Preto |
| 255 | Branco |

---

# 4. Convenção dos Eixos

Em Processamento Digital de Imagens:

```text
(0,0) ─────────► y
  │
  │
  │
  ▼
  x
```

- Origem no canto superior esquerdo.
- Eixo x cresce para baixo.
- Eixo y cresce para a direita.

---

# 5. Aquisição de Imagens

O processo de aquisição ocorre em quatro etapas:

1. Iluminação da cena;
2. Reflexão da luz pelos objetos;
3. Captura por sensores;
4. Conversão para formato digital.

---

# 6. Sensores de Imagem

Os sensores mais comuns são:

## CCD

- Melhor qualidade.
- Menor ruído.
- Maior sensibilidade.
- Maior consumo de energia.

## CMOS

- Menor consumo.
- Menor custo.
- Mais utilizado atualmente.
- Maior ruído.

### Comparação

| Característica | CCD | CMOS |
|--------------|------|------|
| Qualidade | Alta | Média |
| Ruído | Menor | Maior |
| Consumo | Alto | Baixo |
| Custo | Alto | Baixo |

---

# 7. Amostragem e Quantização

## Amostragem

Digitaliza as coordenadas espaciais.

Relacionada à:

✅ Resolução espacial;
✅ Quantidade de Linhas;
✅ Quantidade de Colunas.
---

## Quantização

Digitaliza os níveis de intensidade.

Relacionada à:

✅ Resolução em níveis de cinza --> Transforma intensidades contínuas em níveis discretos

---

# 8. Resolução Espacial

A resolução espacial depende do número de pixels.

Maior resolução:

- mais detalhes;
- menor pixelização.

Menor resolução:

- menos detalhes;
- maior pixelização.

---

# 9. Resolução em Níveis de Cinza

Se cada pixel utiliza $n$ bits:

$$
L = 2^n
$$

onde:

- $L$ = número de níveis de cinza.

O maior valor possível é:

$$
W = 2^n - 1
$$

## Exemplos

| Bits | Níveis |
|--------|---------|
| 1 | 2 |
| 2 | 4 |
| 4 | 16 |
| 8 | 256 |
| 10 | 1024 |
| 16 | 65536 |

---

# 10. Imagem Binária

Imagem com apenas dois níveis:

| Valor | Cor |
|---------|---------|
| 0 | Preto |
| 1 | Branco |

Utiliza:

```text
1 bit por pixel
```

---

# 11. Armazenamento

O espaço ocupado por uma imagem depende de:

- resolução espacial;
- profundidade de bits.

## Exemplo

Imagem:

```text
640 × 480
```

Profundidade:

```text
8 bits/pixel
```

Armazenamento:

$$
640 \times 480 \times 1
=
307200 \text{ bytes}
$$

≈ 300 kB

---

# 12. Profundidade de Cor

| Profundidade | Espaço por Pixel |
|--------------|-----------------|
| 8,7,6,5 bits | 1 byte |
| 4,3 bits | 1/2 byte |
| 2 bits | 1/4 byte |
| 1 bit | 1/8 byte |

---

# 13. Razão de Aspecto

Representa a relação entre largura e altura.

Exemplos:

```text
4:3
16:9
```

---

# 14. Métricas de Resolução

| Equipamento | Métrica |
|------------|----------|
| Câmera | Megapixels (MP) |
| Scanner | DPI |
| Monitor | Dot Pitch |
| Sensor | Pixel Size |

---

# 15. DPI

DPI significa:

**Dots Per Inch**

$$
1 \text{ pol} = 25,4 \text{ mm}
$$

Para um scanner de 600 DPI:

$$
Pixel = \frac{25,4}{600}
$$

$$
Pixel \approx 0,042 \text{ mm}
$$

---

# 16. Principais Efeitos Visuais

## Baixa Resolução Espacial

- Pixelização;
- Perda de detalhes.

## Baixa Resolução em Níveis de Cinza

- Falsos contornos;
- Banding.

---

# 17. Fórmulas para Prova

### Formação da imagem

$$
f(x,y)=i(x,y)\cdot r(x,y)
$$

### Número de níveis de cinza

$$
L=2^n
$$

### Maior nível de cinza

$$
W=2^n-1
$$

### Tamanho do pixel (DPI)

$$
Pixel=\frac{25,4}{DPI}
$$

### Armazenamento

$$
\text{Memória}=
M \times N \times
\text{bytes/pixel}
$$

---

# 18. Resumo para Revisão

✅ Imagem digital = matriz de pixels

✅ Pixel = posição + intensidade

✅ Amostragem → discretiza posição

✅ Quantização → discretiza intensidade

✅ Resolução espacial → quantidade de pixels

✅ Resolução de cinza → quantidade de níveis

✅ CCD → melhor qualidade

✅ CMOS → menor custo e consumo

✅ DPI → resolução de scanners

✅ Armazenamento depende da resolução e da profundidade
