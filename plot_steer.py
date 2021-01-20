# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

ticksize = 30
legendsize = 20
titlesize = 30
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': titlesize}

# b1 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/11/result.err')
# b1 = np.reshape(b1, (-1, 10))
# b2 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/22/result.err')
# b2 = np.reshape(b2, (-1, 10))
# b3 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/33/result.err')
# b3 = np.reshape(b3, (-1, 10))
# b4 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/44/result.err')
# b4 = np.reshape(b4, (-1, 10))
# y_ticks1 = np.arange(-2.5, 3.6, 1)
# y_ticks11 = np.arange(-2.5, 3.6, 1)
# y_ticks2 = np.arange(-0.25, 0.26, 0.05)
# y_ticks3 = np.arange(-1.0, 3.1, 1)

b1 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/1/result.err')
b1 = np.reshape(b1, (-1, 10))
b2 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/2/result.err')
b2 = np.reshape(b2, (-1, 10))
b3 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/3/result.err')
b3 = np.reshape(b3, (-1, 10))
b4 = np.loadtxt('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/4/result.err')
b4 = np.reshape(b4, (-1, 10))
y_ticks1 = np.arange(-3, 3.1, 1.5)
y_ticks2 = np.arange(-0.35, 0.51, 0.2)
y_ticks3 = np.arange(-1.5, 2.6, 1)

fig1 = plt.figure(num=1, figsize=(20, 16))

plt.subplot(411)
plt.tick_params(labelsize=ticksize)
plt.plot(b1[:, 0], b1[:, 1], color='blue', linewidth=1.0, label='north')
plt.plot(b1[:, 0], b1[:, 2], color='green', linewidth=1.0, label='east')
plt.plot(b1[:, 0], b1[:, 3], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m)", font1)
plt.title('Position Error', font1)
plt.grid(True)
plt.yticks(y_ticks1)

plt.subplot(412)
plt.tick_params(labelsize=ticksize)
plt.plot(b2[:, 0], b2[:, 1], color='blue', linewidth=1.0, label='north')
plt.plot(b2[:, 0], b2[:, 2], color='green', linewidth=1.0, label='east')
plt.plot(b2[:, 0], b2[:, 3], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m)", font1)
plt.title('Position Error', font1)
plt.grid(True)
plt.yticks(y_ticks1)

plt.subplot(413)
plt.tick_params(labelsize=ticksize)
plt.plot(b3[:, 0], b3[:, 1], color='blue', linewidth=1.0, label='north')
plt.plot(b3[:, 0], b3[:, 2], color='green', linewidth=1.0, label='east')
plt.plot(b3[:, 0], b3[:, 3], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m)", font1)
plt.title('Position Error', font1)
plt.grid(True)
plt.yticks(y_ticks1/10)

plt.subplot(414)
plt.tick_params(labelsize=ticksize)
plt.plot(b4[:, 0], b4[:, 1], color='blue', linewidth=1.0, label='north')
plt.plot(b4[:, 0], b4[:, 2], color='green', linewidth=1.0, label='east')
plt.plot(b4[:, 0], b4[:, 3], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m)", font1)
plt.title('Position Error', font1)
plt.grid(True)
plt.yticks(y_ticks1/10)

plt.tight_layout()
fig1.align_ylabels()
plt.savefig('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/4/poserr.svg',dpi=600,format='svg')

fig2 = plt.figure(num=2, figsize=(20, 16))

plt.subplot(411)
plt.tick_params(labelsize=ticksize)
plt.plot(b1[:, 0], b1[:, 4], color='blue', linewidth=1.0, label='north')
plt.plot(b1[:, 0], b1[:, 5], color='green', linewidth=1.0, label='east')
plt.plot(b1[:, 0], b1[:, 6], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m/s)", font1)
plt.title('Velocity Error', font1)
plt.grid(True)
plt.yticks(y_ticks2)

plt.subplot(412)
plt.tick_params(labelsize=ticksize)
plt.plot(b2[:, 0], b2[:, 4], color='blue', linewidth=1.0, label='north')
plt.plot(b2[:, 0], b2[:, 5], color='green', linewidth=1.0, label='east')
plt.plot(b2[:, 0], b2[:, 6], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m/s)", font1)
plt.title('Velocity Error', font1)
plt.grid(True)
plt.yticks(y_ticks2)

plt.subplot(413)
plt.tick_params(labelsize=ticksize)
plt.plot(b3[:, 0], b3[:, 4], color='blue', linewidth=1.0, label='north')
plt.plot(b3[:, 0], b3[:, 5], color='green', linewidth=1.0, label='east')
plt.plot(b3[:, 0], b3[:, 6], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m/s)", font1)
plt.title('Velocity Error', font1)
plt.grid(True)
plt.yticks(y_ticks2)

plt.subplot(414)
plt.tick_params(labelsize=ticksize)
plt.plot(b4[:, 0], b4[:, 4], color='blue', linewidth=1.0, label='north')
plt.plot(b4[:, 0], b4[:, 5], color='green', linewidth=1.0, label='east')
plt.plot(b4[:, 0], b4[:, 6], color='red', linewidth=1.0, label='down')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(m/s)", font1)
plt.title('Velocity Error', font1)
plt.grid(True)
plt.yticks(y_ticks2)

plt.tight_layout()
fig2.align_ylabels()
plt.savefig('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/4/velerr.svg',dpi=600,format='svg')

fig3 = plt.figure(num=3, figsize=(20, 16))

plt.subplot(411)
plt.tick_params(labelsize=ticksize)
plt.plot(b1[:, 0], b1[:, 7], color='blue', linewidth=1.0, label='roll')
plt.plot(b1[:, 0], b1[:, 8], color='green', linewidth=1.0, label='pitch')
plt.plot(b1[:, 0], b1[:, 9], color='red', linewidth=1.0, label='yaw')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(deg)", font1)
plt.title('Attitude Error', font1)
plt.grid(True)
plt.yticks(y_ticks3)

plt.subplot(412)
plt.tick_params(labelsize=ticksize)
plt.plot(b2[:, 0], b2[:, 7], color='blue', linewidth=1.0, label='roll')
plt.plot(b2[:, 0], b2[:, 8], color='green', linewidth=1.0, label='pitch')
plt.plot(b2[:, 0], b2[:, 9], color='red', linewidth=1.0, label='yaw')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(deg)", font1)
plt.title('Attitude Error', font1)
plt.grid(True)
plt.yticks(y_ticks3)

plt.subplot(413)
plt.tick_params(labelsize=ticksize)
plt.plot(b3[:, 0], b3[:, 7], color='blue', linewidth=1.0, label='roll')
plt.plot(b3[:, 0], b3[:, 8], color='green', linewidth=1.0, label='pitch')
plt.plot(b3[:, 0], b3[:, 9], color='red', linewidth=1.0, label='yaw')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(deg)", font1)
plt.title('Attitude Error', font1)
plt.grid(True)
plt.yticks(y_ticks3)

plt.subplot(414)
plt.tick_params(labelsize=ticksize)
plt.plot(b4[:, 0], b4[:, 7], color='blue', linewidth=1.0, label='roll')
plt.plot(b4[:, 0], b4[:, 8], color='green', linewidth=1.0, label='pitch')
plt.plot(b4[:, 0], b4[:, 9], color='red', linewidth=1.0, label='yaw')
plt.legend(loc='upper right', fontsize=legendsize)
plt.xlabel("time(s)", font1)
plt.ylabel("error(deg)", font1)
plt.title('Attitude Error', font1)
plt.grid(True)
plt.yticks(y_ticks3)

plt.tight_layout()
fig3.align_ylabels()
plt.savefig('/mnt/Storage/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/4/atterr.svg',dpi=600,format='svg')
