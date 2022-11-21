from matplotlib import pyplot as plt
import numpy as np

advanced_152 = [85.3,77.6,48.6,117.0]
a = advanced_152[0]+advanced_152[1]
advanced_153 = [56.0,46.0,49.3,36.0,90.0]
b = advanced_153[0]+advanced_153[1]+advanced_153[2]
advanced_154 = [40.6,34,31.3,36.3,26.3,77.0]
c = advanced_154[0]+advanced_154[1]+advanced_154[2]+advanced_154[3]
advanced_155 = [24.3,25.0,27.6,33.3,29.6,24.3,67.6]
d = advanced_155[0]+advanced_155[1]+advanced_155[2]+advanced_155[3] + advanced_155[4]
advanced_156 = [25.6,29.0,17.0,24.3,22.6,19.6,20.6,60.3]
e = advanced_156[0]+advanced_156[1]+advanced_156[2]+advanced_156[3] + advanced_156[4] + advanced_156[5]

a2 = [a,advanced_152[-1:]]
a3 = [b,advanced_153[-1:]]
a4 = [c,advanced_154[-1:]]
a5 = [d,advanced_155[-1:]]
a6 = [e,advanced_156[-1:]]


kimst_152 = [92.6, 90.0, 68.3, 120.6]
a = kimst_152[0]+kimst_152[1]
kimst_153 = [55.6, 67, 78, 46.3, 109.0]
b = kimst_153[0]+kimst_153[1]+kimst_153[2]
kimst_154 = [66, 47.6, 47.3, 57.6, 35, 102]
c = kimst_154[0]+kimst_154[1]+kimst_154[2]+kimst_154[3]
kimst_155 = [40.6, 45.3, 49, 38.3, 54.0, 29, 102]
d = kimst_155[0]+kimst_155[1]+kimst_155[2]+kimst_155[3] + kimst_155[4]
kimst_156 = [49.8, 37.6, 47.8, 37.6, 32.2, 31.0, 23.8, 100.4]
e = kimst_156[0]+kimst_156[1]+kimst_156[2]+kimst_156[3] + kimst_156[4] + kimst_156[5]


k2 = [a,kimst_152[-1:]]
k3 = [b,kimst_153[-1:]]
k4 = [c,kimst_154[-1:]]
k5 = [d,kimst_155[-1:]]
k6 = [e,kimst_156[-1:]]

x= np.arange(2,7)
y = [k2[1],k3[1],k4[1],k5[1],k6[1]]
y2 = [a2[1],a3[1],a4[1],a5[1],a6[1]]
plt.plot(x,y, 'bs--', label = 'KNN')
plt.plot(x,y2, 'g^--',label = 'Advanced-KNN')
plt.title("Comparison of Exploration Time")
plt.xlabel("Number of Robots")
plt.ylabel("Total Exploration Time(s)")
plt.axis([1,7, 0, 200])
plt.legend()

plt.show()



x= np.arange(2,7)
y = [k2[0],k3[0],k4[0],k5[0],k6[0]]
y2 = [a2[0],a3[0],a4[0],a5[0],a6[0]]
plt.plot(x,y, 'bs--', label = 'KNN')
plt.plot(x,y2, 'g^--',label = 'Advanced-KNN')
plt.title("Comparison of Distance Travelled")
plt.xlabel("Number of Robots")
plt.ylabel("Total Distance Travelled")
plt.axis([1,7, 100, 300])
plt.legend()

plt.show()