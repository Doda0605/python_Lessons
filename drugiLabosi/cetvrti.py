import numpy as np
import matplotlib.pyplot as plt

black = np.ones((50,50))
white = np.zeros((50,50))

col1 = np.vstack((black,white))
col2 = np.vstack((white,black))
img = np.hstack((col2,col1))
plt.imshow(img,cmap = "gray")
plt.show()