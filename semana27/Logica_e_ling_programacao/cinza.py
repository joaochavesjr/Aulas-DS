#from skimage import io, color
#imagem = io.imread('imagem.jpg')
#imagem_cinza = color.rgb2gray(imagem)
#io.imsave('imagem_cinza.png', imagem_cinza)

import matplotlib.pyplot as plt
from PIL import Image # For opening images with PIL
img = Image.open("imagem.jpg")

gray_img = img.convert("L") # "L" mode for 8-bit grayscale

plt.imshow(gray_img, cmap='gray') # Display with grayscale colormap
plt.axis('off') # Optional: Remove axes
plt.savefig('imagem_cinza.png')