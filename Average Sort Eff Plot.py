import bubble
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
y2 = []
yr = []
for i in range(2, 90):
    x.append(i)
    y2.append(i**2)
    a = bubble.average(i, 5000)
    y.append(a)
    yr.append(a/i**2)
    print(i)
xp = np.array(x)
yp = np.array(y)
y2p = np.array(y2)
yrp = np.array(yr)
plt.figure("Worst Case Over Average Case Plot")
plt.plot(xp, yp)
plt.plot(xp, y2p)
plt.figure("Average Case by Worst Case Ratio Plot")
plt.plot(xp, yrp)
plt.show()
