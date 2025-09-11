def plota(imagem, nome):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  shape = imagem.shape
  plt.title(f'{nome}. Dimensão: {shape}')
  plt.show()
  plt.hist(imagem.flatten(),bins=100,density=False,range=(0,255))
  plt.xlim([0,255])
  plt.show()
img = cv.imread('palavrascruzadas.tif', -1)
img = img.astype(np.uint8)
img_bin = cv.imread('palavrascruzadas.tif', -1)
img_bin = img_bin.astype(np.uint8)
plota(img, 'Imagem Original')
## Analisando o Hist. obtido, temos que o vale ocorre próximo ao bit n = 140. 
limiar = 140
for i in range(len(img_bin)): 
  for j in range(len(img_bin[0])):
    if img_bin[i][j] >= limiar:
      img_bin[i][j] = 255
    else:
      img_bin[i][j] = 0
plota(img_bin, 'Imagem Binarizada (regular)')
th_value, img_bin_otsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plota(img_bin_otsu, 'Imagem Binarizada (Otsu)')
print(f'O valor encontrado pelo Otsu é: {th_value}')
