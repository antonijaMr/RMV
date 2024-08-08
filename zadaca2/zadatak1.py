import cv2
import numpy as np
from matplotlib import pyplot as plt

print("Pokretanje skripte...")

# Učitajmo zasumljenu sliku
image = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)

# Provera da li je slika uspješno učitana
if image is None:
    print("Slika nije uspešno učitana. Proverite putanju do slike.")
    exit()

print("Primjena Gaussovog filtera...")
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

print("Primjena averaging filtera...")
# Primena averaging filtera
mean_blur = cv2.blur(image, (5, 5))

print("Primjena median filtera...")
median_blur = cv2.medianBlur(image, 5)

print("Priprema za prikaz slika...")
# Prikaz originalne i filtrirane slike
titles = ['Original Image', 'Gaussian Blur', 'Averaging Blur', 'Median Blur']
images = [image, gaussian_blur, mean_blur, median_blur]

plt.figure(figsize=(12, 6))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

print("Prikaz slika...")
plt.show()
