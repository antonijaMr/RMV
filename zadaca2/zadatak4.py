import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('photo.jpg')
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)

dilation = cv2.dilate(img, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

titles = ['Original image', 'Erosion', 'Dilatation', 'Opening', 'Closing', 'Gradient']
images = [img, erosion, dilation, opening, closing, gradient]

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

