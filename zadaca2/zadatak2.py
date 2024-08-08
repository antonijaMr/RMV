import cv2
import matplotlib.pyplot as plt

# Read the original image
img = cv2.imread('photo.jpg')

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

# Plotting all images together
titles = ['Original Image', 'Gray Image', 'Blurred Image', 'Sobel X', 'Sobel Y', 'Sobel XY', 'Canny']
images = [img, img_gray, img_blur, sobelx, sobely, sobelxy, edges]

plt.figure(figsize=(20, 10))

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    if len(images[i].shape) == 2:  # Grayscale image
        plt.imshow(images[i], cmap='gray')
    else:  # BGR image
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
