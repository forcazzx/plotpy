import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

R2D = 57.29577951308232
ticksize = 40
insticksize = 30
titlesize = 50
line_width = 3
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': titlesize}
plt.rcParams['font.sans-serif'] = 'Times New Roman'
define = 1

if define == 1:
    b = np.loadtxt('E:/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/4/error.txt')
else:
    b = np.loadtxt('E:/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/44/error.txt')
b = np.reshape(b, (-1, 15))
# plt.figure(1)
# plt.plot(b[:, 0], b[:, 1]*R2D, color='blue')
# plt.figure(1)
# plt.plot(b[:, 0], b[:, 2]*R2D, color='green')
# plt.figure(1)
# plt.plot(b[:, 0], b[:, 3]*R2D, color='red')
# plt.xlabel("time(s)")
# plt.ylabel("gyrobias(deg/s)")
# plt.grid(True)
# plt.title('x=blue y=green z=red')

# plt.figure(2)
# plt.plot(b[:, 0], b[:, 4], color='blue')
# plt.figure(2)
# plt.plot(b[:, 0], b[:, 5], color='green')
# plt.figure(2)
# plt.plot(b[:, 0], b[:, 6], color='red')
# plt.xlabel("time(s)")
# plt.ylabel("accebias(m/s^2)")
# plt.grid(True)
# plt.title('x=blue y=green z=red')

# plt.figure(3)
# plt.plot(b[:, 0], b[:, 7], color='blue')
# plt.figure(3)
# plt.plot(b[:, 0], b[:, 8], color='green')
# plt.figure(3)
# plt.plot(b[:, 0], b[:, 9], color='red')
# plt.xlabel("time(s)")
# plt.ylabel("gyroscale")
# plt.grid(True)
# plt.title('x=blue y=green z=red')

# plt.figure(4)
# plt.plot(b[:, 0], b[:, 10], color='blue')
# plt.figure(4)
# plt.plot(b[:, 0], b[:, 11], color='green')
# plt.figure(4)
# plt.plot(b[:, 0], b[:, 12], color='red')
# plt.xlabel("time(s)")
# plt.ylabel("accescale")
# plt.grid(True)
# plt.title('x=blue y=green z=red')

if define == 1:
    ticks = np.arange(439050, 439500, 200)
else:
    ticks = np.arange(441050, 441500, 200)
fig5 = plt.figure(num=5, figsize=(20, 16))

ax1 = plt.subplot(211)
plt.tick_params(labelsize=ticksize)
plt.plot(b[:, 0], b[:, 13], linewidth=line_width)
# plt.xlabel("time(s)",font1)
plt.ylabel(r'$s_{odo}$',font1)
plt.grid(True)
plt.setp(ax1.get_xticklabels(), visible=False)

ax1ins = ax1.inset_axes((0.5, 0.2, 0.4, 0.2))
ax1ins.plot(b[:, 0], b[:, 13], linewidth=line_width)
if define == 1:
    ax1ins.set_xlim(439000, 439500)
    ax1ins.set_ylim(0.023, 0.0235)
else:
    ax1ins.set_xlim(441000, 441500)
    ax1ins.set_ylim(0.0235, 0.024)
ax1ins.set_xticks(ticks)
mark_inset(ax1, ax1ins, loc1=1, loc2=3, fc="none", ec='k', lw=1)
ax1ins.tick_params(labelsize=insticksize)

ax2 = plt.subplot(212)
plt.tick_params(labelsize=ticksize)
plt.plot(b[:, 0], b[:, 14]*R2D, linewidth=line_width)
plt.xlabel("time (s)",font1)
plt.ylabel(r'$\delta\theta$ (deg)',font1)
plt.grid(True)

if define == 1:
    ax2ins = ax2.inset_axes((0.5, 0.2, 0.4, 0.2))
else:
    ax2ins = ax2.inset_axes((0.5, 0.6, 0.4, 0.2))
ax2ins.plot(b[:, 0], b[:, 14]*R2D, linewidth=line_width)
if define == 1:
    ax2ins.set_xlim(439000, 439500)
    ax2ins.set_ylim(-2, -1.8)
    mark_inset(ax2, ax2ins, loc1=1, loc2=3, fc="none", ec='k', lw=1)
else:
    ax2ins.set_xlim(441000, 441500)
    ax2ins.set_ylim(-2.25, -2.05)
    ax2ins.set_yticks(np.arange(-2.25, -2.0, 0.2))
    mark_inset(ax2, ax2ins, loc1=3, loc2=4, fc="none", ec='k', lw=1)
ax2ins.set_xticks(ticks)
ax2ins.tick_params(labelsize=insticksize)

labels = ax1.get_yticklabels() + ax2.get_xticklabels() + ax2.get_yticklabels() + ax1ins.get_xticklabels() + ax1ins.get_yticklabels() + ax2ins.get_xticklabels() + ax2ins.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
# plt.tight_layout()
fig5.align_ylabels()
if define == 1:
    plt.savefig('E:/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/4/odo&cita.svg',dpi=600,format='svg')
else:
    plt.savefig('E:/FileRecv/Navigation/组合导航数据处理/机器人数据/20201009-信操数据/result/44/odo&cita.svg',dpi=600,format='svg')
plt.show()
