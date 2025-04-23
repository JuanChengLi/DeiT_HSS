import cv2
import numpy as np
import matplotlib.pyplot as plt

# Specify the input image path
image_path = 'C:/Users/Juan/Documents/Sure Summer 2025/N5_MARTENSITE/20000X_02.png'

# Read the image
img = cv2.imread(image_path)
if img is None:
    raise ValueError(f"Image not found at {image_path}")

# Convert from BGR (OpenCV default) to RGB for display
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Compute the largest multiples of 224 not exceeding the original dimensions
h, w = img.shape[:2]
new_h = (h // 224) * 224
new_w = (w // 224) * 224

# Crop the image to those dimensions
img_cropped = img[:new_h, :new_w]

# Draw red grid lines every 224 pixels
# RGB red is (255, 0, 0)
for x in range(224, new_w, 224):
    cv2.line(img_cropped, (x, 0), (x, new_h), (255, 255, 255), thickness=3)
for y in range(224, new_h, 224):
    cv2.line(img_cropped, (0, y), (new_w, y), (255, 255, 255), thickness=3)

# Display the result using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(img_cropped)
plt.axis('off')
plt.show()

