def plota(imagem):
  plt.figure(figsize=(5,5))
  plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
  shape = imagem.shape
  plt.title(f'{shape}')
  plt.show()
  plt.hist(imagem.flatten(),bins=100,density=False,range=(0,255))
  plt.xlim([0,255])
  plt.show()
img = cv.imread('palavrascruzadas.tif', -1)
img = img.astype(np.uint8)
img_bin = cv.imread('palavrascruzadas.tif', -1)
img_bin = img_bin.astype(np.uint8)
plota(img)
## Analisando o Hist. obtido, temos que o vale ocorre próximo ao bit n = 150. 
limiar = 150
for i in range(len(img_bin)): 
  for j in range(len(img_bin[0])):
    if img_bin[i][j] >= limiar:
      img_bin[i][j] = 255
    else:
      img_bin[i][j] = 0
plota(img_bin)
