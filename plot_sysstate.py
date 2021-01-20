import numpy as np
import matplotlib.pyplot as plt

R2D = 57.29577951308232
ticksize = 30
legendsize = 20
titlesize = 40
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': titlesize}

b = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/error.txt')
b = np.reshape(b, (-1, 15))
plt.figure(1)
plt.plot(b[:, 0], b[:, 1]*R2D, color='blue')
plt.figure(1)
plt.plot(b[:, 0], b[:, 2]*R2D, color='green')
plt.figure(1)
plt.plot(b[:, 0], b[:, 3]*R2D, color='red')
plt.xlabel("time(s)")
plt.ylabel("gyrobias(deg/s)")
plt.grid(True)
plt.title('x=blue y=green z=red')

plt.figure(2)
plt.plot(b[:, 0], b[:, 4], color='blue')
plt.figure(2)
plt.plot(b[:, 0], b[:, 5], color='green')
plt.figure(2)
plt.plot(b[:, 0], b[:, 6], color='red')
plt.xlabel("time(s)")
plt.ylabel("accebias(m/s^2)")
plt.grid(True)
plt.title('x=blue y=green z=red')

plt.figure(3)
plt.plot(b[:, 0], b[:, 7], color='blue')
plt.figure(3)
plt.plot(b[:, 0], b[:, 8], color='green')
plt.figure(3)
plt.plot(b[:, 0], b[:, 9], color='red')
plt.xlabel("time(s)")
plt.ylabel("gyroscale")
plt.grid(True)
plt.title('x=blue y=green z=red')

plt.figure(4)
plt.plot(b[:, 0], b[:, 10], color='blue')
plt.figure(4)
plt.plot(b[:, 0], b[:, 11], color='green')
plt.figure(4)
plt.plot(b[:, 0], b[:, 12], color='red')
plt.xlabel("time(s)")
plt.ylabel("accescale")
plt.grid(True)
plt.title('x=blue y=green z=red')

fig1 = plt.figure(num=5, figsize=(20, 16))
plt.tick_params(labelsize=ticksize)
plt.plot(b[:, 0], b[:, 13])
plt.xlabel("time(s)",font1)
plt.ylabel('odoscale',font1)
plt.grid(True)
plt.tight_layout()
plt.savefig('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result2/odoscale.svg',dpi=600,format='svg')

fig2 = plt.figure(num=6, figsize=(20, 16))
plt.tick_params(labelsize=ticksize)
plt.plot(b[:, 0], b[:, 14]*R2D)
plt.xlabel("time(s)",font1)
plt.ylabel('deltacita(deg)',font1)
plt.grid(True)
plt.tight_layout()
plt.savefig('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result2/deltacita.svg',dpi=600,format='svg')
plt.show()
