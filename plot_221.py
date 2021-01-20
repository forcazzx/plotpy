# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math

font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 60}

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 30,
         }
b = np.loadtxt('../../FileRecv/Navigation/组合导航数据处理/20192229车载ADIS16465评估/H5A/C/error2.txt')
b = np.reshape(b, (-1, 15))

fig = plt.figure(num=2, figsize=(30, 16))
plt.subplot(221)
plt.tick_params(labelsize=40)
plt.plot(b[:, 0], b[:, 1]/math.pi*180, color='blue', linewidth=1.0, label='x')
plt.plot(b[:, 0], b[:, 2]/math.pi*180, color='green', linewidth=1.0, label='y')
plt.plot(b[:, 0], b[:, 3]/math.pi*180, color='red', linewidth=1.0, label='z')
plt.legend(loc='upper right', fontsize=20)
plt.xlabel("time(s)", font1)
plt.ylabel("error(deg/s)", font1)
plt.title('gyrobias', font1)

plt.subplot(222)
plt.tick_params(labelsize=40)
plt.plot(b[:, 0], b[:, 4], color='blue', linewidth=1.0, label='x')
plt.plot(b[:, 0], b[:, 5], color='green', linewidth=1.0, label='y')
plt.plot(b[:, 0], b[:, 6], color='red', linewidth=1.0, label='z')
plt.legend(loc='upper right', fontsize=20)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m/s^2)", font1)
plt.title('accebias', font1)

plt.subplot(223)
plt.tick_params(labelsize=40)
plt.plot(b[:, 0], b[:, 7], color='blue', linewidth=1.0, label='x')
plt.plot(b[:, 0], b[:, 8], color='green', linewidth=1.0, label='y')
plt.plot(b[:, 0], b[:, 9], color='red', linewidth=1.0, label='z')
plt.legend(loc='upper right', fontsize=20)
plt.xlabel("time(s)", font1)
plt.ylabel("error", font1)
plt.title('gyroscale', font1)

plt.subplot(224)
plt.tick_params(labelsize=40)
plt.plot(b[:, 0], b[:, 10], color='blue', linewidth=1.0, label='x')
plt.plot(b[:, 0], b[:, 11], color='green', linewidth=1.0, label='y')
plt.plot(b[:, 0], b[:, 12], color='red', linewidth=1.0, label='z')
plt.legend(loc='upper right', fontsize=20)
plt.xlabel("time(s)", font1)
plt.ylabel("error", font1)
plt.title('accescale', font1)

# plt.subplot(313)
# plt.tick_params(labelsize=40)
# plt.plot(b[:, 0], b[:, 13])
# plt.xlabel("time(s)", font1)
# plt.ylabel("error", font1)
# plt.title('odoscale', font1)

plt.tight_layout()
fig.align_ylabels()
plt.savefig('../../FileRecv/Navigation/组合导航数据处理/20192229车载ADIS16465评估/H5A/C/error2.png')
plt.show()
