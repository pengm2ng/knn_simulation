from matplotlib import pyplot as plt
import numpy as np

advanced_152 = [41.75,43.3,26.3,56.9]
a = advanced_152[0]+advanced_152[1]
advanced_153 = [29.1,28.4,26.65,18.8,45.8]
b = advanced_153[0]+advanced_153[1]+advanced_153[2]
advanced_154 = [21.7,21.1,20.2,23.15,15.75,40.25]
c = advanced_154[0]+advanced_154[1]+advanced_154[2]+advanced_154[3]
advanced_155 = [18.75,18.65,18.5,16.8,16.4,12.75,36.3]
d = advanced_155[0]+advanced_155[1]+advanced_155[2]+advanced_155[3] + advanced_155[4]
advanced_156 = [15.15,16.1,15.6,17.05,16.7,13.35,11.65,36.8]
e = advanced_156[0]+advanced_156[1]+advanced_156[2]+advanced_156[3] + advanced_156[4] + advanced_156[5]


a_mean = a/2
b_mean = b/3
c_mean = c/4
d_mean = d/5
e_mean = e/6



a2 = [a,advanced_152[-1:], a_mean]
a3 = [b,advanced_153[-1:], b_mean]
a4 = [c,advanced_154[-1:], c_mean]
a5 = [d,advanced_155[-1:], d_mean]
a6 = [e,advanced_156[-1:], e_mean]



kimst_152 = [52.05, 44.4,36.85,63.05]
a = kimst_152[0]+kimst_152[1]
kimst_153 = [34.8,31.25,33.15,25.65,53.6]
b = kimst_153[0]+kimst_153[1]+kimst_153[2]
kimst_154 = [28.25,24.25,26.85,25.85,20.3,51.55]
c = kimst_154[0]+kimst_154[1]+kimst_154[2]+kimst_154[3]
kimst_155 = [24.5,20.45,21.95,22.25,20.0,17.05,49.55]
d = kimst_155[0]+kimst_155[1]+kimst_155[2]+kimst_155[3] + kimst_155[4]
kimst_156 = [18.75,18.5,18.5,18.95,17.8,17.15,13.95,46.75]
e = kimst_156[0]+kimst_156[1]+kimst_156[2]+kimst_156[3] + kimst_156[4] + kimst_156[5]



a_mean = a/2
b_mean = b/3
c_mean = c/4
d_mean = d/5
e_mean = e/6


k2 = [a,kimst_152[-1:],a_mean]
k3 = [b,kimst_153[-1:],b_mean]
k4 = [c,kimst_154[-1:],c_mean]
k5 = [d,kimst_155[-1:],d_mean]
k6 = [e,kimst_156[-1:],e_mean]

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
plt.axis([1,7, 0, 200])
plt.legend()

plt.show()


x= np.arange(2,7)
y = [k2[2],k3[2],k4[2],k5[2],k6[2]]
y2 = [a2[2],a3[2],a4[2],a5[2],a6[2]]
plt.plot(x,y, 'bs--', label = 'KNN')
plt.plot(x,y2, 'g^--',label = 'Advanced-KNN')
plt.title("Comparison of Distance Travelled average")
plt.xlabel("Number of Robots")
plt.ylabel("Distance Travelled average")
plt.axis([1,7, 0, 100])
plt.legend()

plt.show()