import numpy as np
import matplotlib.pyplot as plt


points = np.array([[3,1],[1,1],[2,2],[3,2], [3,1]])
x = points[:,0]
y=points[:,1]

plt.plot(x,y, linewidth = 5,marker = ".",markersize=25,color = 'green',linestyle = 'dashdot' )
plt.axis([0,4,0,4])
plt . xlabel ( 'x os')
plt . ylabel ( ' y os ' )
plt . title ( ' zad 1 ' )
plt . show ()