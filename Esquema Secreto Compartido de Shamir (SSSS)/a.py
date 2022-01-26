import cv2
path = r'C:\Users\jonqt\Music\Python\Esteganografía\RevealShowApp\Imágenes\Ulthwe.png'
# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread('Ulthwe.png')
  
# Displaying the image
cv2.imshow('image', img)