from PIL import Image, ImageFilter

# Abrir uma imagem
imagem = Image.open('imagem.jpg')

# Aplicar um filtro de desfoque
# BLUR, CONTOUR, DETAIL, EMBOSS, SHARPEN 
imagem_desfocada = imagem.filter(ImageFilter.BLUR)

# Salvar a imagem editada
imagem_desfocada.save('imagem_desfocada.jpg')