from skimage import io
import matplotlib.pyplot as plt

#Le a imagem
image = io.imread('len_std.png')
#Mostra o tamanho da imagem
width = image.shape[0]
height = image.shape[1]
print "Tamanho: %dx%d" % (height, width)
#Mostra a imagem na janela
plt.figure("Imagem Original") # define a janela
plt.imshow(image)
plt.show()