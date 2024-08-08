import cv2
import numpy as np
from matplotlib import pyplot as plt

# Učitajte originalnu sliku
img = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)

# Izračunavanje histograma
hist = cv2.calcHist([img], [0], None, [256], [0, 256])


_, binary_simple = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

binary_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

_, binary_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Prikazivanje originalne slike, histograma i binarnih slika na istom grafu
plt.figure(figsize=(10, 8))

# Originalna slika
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

# Histogram
plt.subplot(2, 3, 2)
plt.plot(hist, color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Intensity Value')
plt.ylabel('Pixel Count')
plt.xlim([0, 256])


plt.subplot(2, 3, 4)
plt.imshow(binary_simple, cmap='gray')
plt.title('Simple Thresholding')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(binary_adaptive, cmap='gray')
plt.title('Adaptive Thresholding')
plt.axis('off')


plt.subplot(2, 3, 6)
plt.imshow(binary_otsu, cmap='gray')
plt.title('Otsu Thresholding')
plt.axis('off')

# Prikazivanje svih grafova zajedno
plt.tight_layout()
plt.show()
