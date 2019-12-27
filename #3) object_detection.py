from PIL import Image
from skimage.io import imread
from skimage.morphology import convex_hull_image
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np


image = imread('12.jpg')
image_ = 1 - rgb2gray(image)
threshold = 0.5
image_[image_ <= threshold] = 0
image_[image_ > threshold] = 1
chull = convex_hull_image(image_)
imageBox = Image.fromarray((chull*255).astype(np.uint8)).getbbox()
cropped = Image.fromarray(image).crop(imageBox)
_,ax = plt.subplots(1,3,figsize=(10,10))
ax[0].imshow(image)
ax[1].imshow(chull)
ax[2].imshow(cropped)
plt.show()

# Uncomment this line to save cropped image
# cropped.save('output.png') # Change file format if any errors...