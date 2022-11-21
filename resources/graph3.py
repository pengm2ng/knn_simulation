from matplotlib import pyplot as plt
import numpy as np

advanced_152 = [41.75,43.3,26.3,56.9]
a = advanced_152[0]+advanced_152[1]
advanced_153 = [29.1,28.4,26.65,18.8,45.8]
b = advanced_153[0]+advanced_153[1]+advanced_153[2]
advanced_154 = [
21.7,21.1,20.2,23.15,15.75,40.25]
c = advanced_154[0]+advanced_154[1]+advanced_154[2]+advanced_154[3]
advanced_155 = [
18.75,18.65,18.5,16.8,16.4,12.75,36.3]
d = advanced_155[0]+advanced_155[1]+advanced_155[2]+advanced_155[3] + advanced_155[4]
advanced_156 = [15.15,16.1,15.6,17.05,16.7,13.35,11.65,36.85]
e = advanced_156[0]+advanced_156[1]+advanced_156[2]+advanced_156[3] + advanced_156[4] + advanced_156[5]
a2 = [a,advanced_152[-1:]]
a3 = [b,advanced_153[-1:]]
a4 = [c,advanced_154[-1:]]
a5 = [d,advanced_155[-1:]]
a6 = [e,advanced_156[-1:]]


kimst_152 = [43.65,42.5,32.45,54.0]
a = kimst_152[0]+kimst_152[1]
kimst_153 = [31.55,28.8,31.95,23.0,47.2]
b = kimst_153[0]+kimst_153[1]+kimst_153[2]
kimst_154 = [25.6,23.8,24.0,21.35,18.2,42.55]
c = kimst_154[0]+kimst_154[1]+kimst_154[2]+kimst_154[3]
kimst_155 = [22.55,21.35,19.25,20.35,18.4,14.7,44.15]
d = kimst_155[0]+kimst_155[1]+kimst_155[2]+kimst_155[3] + kimst_155[4]
kimst_156 = [17.65,20.4,18.9,16.05,15.4,15.7,12.0,41.4]
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
plt.axis([1,7, 0, 100])
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
plt.axis([1,7, 0, 300])
plt.legend()

plt.show()