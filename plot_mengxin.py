# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 60}

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 30,
         }
b = np.loadtxt('C:/Users/91375/Desktop/测试/测试数据/log.txt')
b = np.reshape(b, (-1, 12))

fig = plt.figure(num=1, figsize=(30, 24))
plt.subplot(311)
plt.tick_params(labelsize=50)
plt.plot(b[:, 0], b[:, 1], color='blue', linewidth=1.0, label='x')
plt.plot(b[:, 0], b[:, 2], color='green', linewidth=1.0, label='y')
plt.plot(b[:, 0], b[:, 3], color='red', linewidth=1.0, label='z')
plt.legend(loc='upper right', fontsize=20)
plt.xlabel("time(s)", font1)
plt.ylabel("acce(g)", font1)
plt.title('accelerometer', font1)

plt.subplot(312)
plt.tick_params(labelsize=50)
plt.plot(b[:, 0], b[:, 4], color='blue', linewidth=1.0, label='x')
plt.plot(b[:, 0], b[:, 5], color='green', linewidth=1.0, label='y')
plt.plot(b[:, 0], b[:, 6], color='red', linewidth=1.0, label='z')
plt.legend(loc='upper right', fontsize=20)
plt.xlabel("time(s)", font1)
plt.ylabel("gyro(deg/s)", font1)
plt.title('gyroscope', font1)

plt.subplot(313)
plt.tick_params(labelsize=50)
plt.plot(b[:, 0], b[:, 7], color='blue', linewidth=1.0, label='x')
plt.plot(b[:, 0], b[:, 8], color='green', linewidth=1.0, label='y')
plt.plot(b[:, 0], b[:, 9], color='red', linewidth=1.0, label='z')
plt.legend(loc='upper right', fontsize=20)
plt.xlabel("time(s)", font1)
plt.ylabel("m(gauss)", font1)
plt.title('magnatic', font1)

plt.tight_layout()
fig.align_ylabels()
plt.savefig('C:/Users/91375/Desktop/测试/测试数据/九轴传感器.png')

fig2 = plt.figure(num=1, figsize=(30, 16))
plt.subplot(211)
plt.tick_params(labelsize=50)
plt.plot(b[:, 0], b[:, 10], color='blue')
plt.xlabel("time(s)", font1)
plt.ylabel("temp(c)", font1)
plt.title('temperature', font1)

plt.subplot(212)
plt.tick_params(labelsize=50)
plt.plot(b[:, 0], b[:, 11], color='blue')
plt.xlabel("time(s)", font1)
plt.ylabel("pressure(Pa)", font1)
plt.title('pressure', font1)

plt.tight_layout()
fig2.align_ylabels()
plt.savefig('C:/Users/91375/Desktop/测试/测试数据/温度与气压.png')
