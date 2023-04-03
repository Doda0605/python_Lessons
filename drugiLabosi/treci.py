import numpy as np
import matplotlib.pyplot as plt



img = plt.imread("road.jpg")
h,w,c = img.shape


img = img[:,:,0].copy ()
print(img.shape)
print(img.dtype)
plt.figure ()

plt.title("Base image")
plt.imshow(img)
plt.show()

plt.title("Bright image")
plt.imshow(img,vmin=0,vmax=150)
plt.show()

crop = int(w/4)
plt.title("Cropped image")
plt.imshow(img[0:,0:crop])
plt.show()


plt.title("Rotated Image")
plt.imshow(np.rot90(img,3))
plt.show()

plt.title("Mirrored Image")
plt.imshow(np.fliplr(img))
plt.show()