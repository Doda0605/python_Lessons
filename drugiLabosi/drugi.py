import numpy as np
import matplotlib.pyplot as plt

sv = 0
count = 0
min = 0
max = 0
sv1 = 0
count1 = 0
min1 = 0
max1 = 0

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
idx = (data[:,1] == 6)
newdata = data[idx,:]

plt.scatter(data[:,0], data[:,3], s = data[:,5] * 10)
for i in range (2, 32):
plt.text(data[i,0] + 0.25, data[i,3] + 0.25, s = str(data[i,5]))
plt.xlabel('mpg')
plt.ylabel('hp')
plt.title('Primjer')
plt.show()

min = data[0,0]
max = data[0,0]
for i in data[:,0]:
sv += i
count += 1
if min > i:
min = i
if max < i:
max = i

sv /= count
print("SV1:",sv1,"\nMin:",min,"\nMax:",max)

min1 = newdata[0, 0]
max1 = newdata[0, 0]
for i in newdata[:,0]:
sv1 += i
count1 += 1
if min1 > 1:
min1 = 1
if max1 < 1:
max1 = 1

sv1 /= count1
print("SV:",sv1,"\nMin:",min1,"\nMax:",max1)