import numpy as np
import math
import matplotlib.pyplot as plt


def show_cdf(errfile):
    data = errfile

    # 统计平面误差的CDF曲线, 精度为0.01m
    plane = data[:, 1] * data[:, 1] + data[:, 2] * data[:, 2]
    for i in range(plane.shape[0]):
        plane[i] = math.sqrt(plane[i])
    precision = 0.01
    maxplane = np.max(plane)
    length = len(plane)
    err = np.arange(round(maxplane + 0.5) * int(1 / precision) + 1) * precision
    cdf = np.zeros(len(err))

    for k in range(len(err)):
        cdf[k] = len(np.argwhere(plane < err[k])) / length * 100

    plt.figure('Plane_cdf')
    plt.plot(err, cdf, 'o', markersize=4)
    plt.plot(err, cdf, 'y')
    plt.grid()
    plt.xlabel('Error [m]')
    plt.ylabel('Probability [%]')
    plt.ylim(60, 100)
    plt.title('CDF of Plane Error')
    plt.tight_layout()

    vel = data[:, 4] * data[:, 4] + data[:, 5] * data[:, 5] + data[:, 6] * data[:, 6]
    for i in range(vel.shape[0]):
        vel[i] = math.sqrt(vel[i])
    precision = 0.001
    maxvel = np.max(vel)
    length = len(vel)
    err = np.arange(round(maxvel + 0.5) * int(1 / precision) + 1) * precision
    cdf = np.zeros(len(err))

    for k in range(len(err)):
        cdf[k] = len(np.argwhere(vel < err[k])) / length * 100

    plt.figure('Vel_cdf')
    plt.plot(err, cdf, 'o', markersize=4)
    plt.plot(err, cdf, 'y')
    plt.grid()
    plt.xlabel('Error [m/s]')
    plt.ylabel('Probability [%]')
    plt.ylim(60, 100)
    plt.title('CDF of Vel Error')
    plt.tight_layout()

    plt.show()


data = np.loadtxt("F:/stim300/result/spp1/LC_OUTAGE46S_TXT.err")
data = np.reshape(data, (-1, 10))
for i in range(data.shape[0]):
    if(data[i, 0] >= 466500):
        break
data = data[i:, :]
# print(data)
show_cdf(data)
