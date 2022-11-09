import matplotlib.pyplot as plt
import numpy as np

nAdaptation = 6
nDots = 100
dat = []
with open(r".\DATA\No adaptation.txt") as f:
    for line in f:
        dat.append([float(x) for x in line.split()])
for i in range(1, nAdaptation + 1):
    with open(r".\DATA\adaptation " + str(i) +" .txt") as f:
        for line in f:
            dat.append([float(x) for x in line.split()])
with open(r".\DATA\Exact.txt") as f:
    for line in f:
        dat.append([float(x) for x in line.split()])
dat = np.array(dat, dtype=float)



fig = plt.figure(figsize=(15, 6))
plt.rcParams['font.size'] = '18'

ax_1 = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.09, right=0.92, top=0.915, bottom=0.125)
ax_1.plot(dat[0:nDots, 0], dat[0:nDots, 1], label="Without adaptation")
for i in range(1, nAdaptation + 1):
    ax_1.plot(dat[nDots * i:nDots * (i + 1), 0], dat[nDots * i:nDots * (i + 1), 1], label="adaptation" + str(i))
ax_1.plot(dat[nDots * (nAdaptation + 1):, 0], dat[nDots * (nAdaptation + 1):, 1], label="Exact solution")
ax_1.set(xlabel='s')
ax_1.set(ylabel='u(x(s),y(s))')
ax_1.legend()
plt.show()
