import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")


x = np.linspace(1, 5, 40)
y = x + 3*np.random.rand(40)-1.5
y_1 = x
y_2 = 0.8 * x + 0.6
l = np.linspace(1, 5, 40)
m = 1.8*np.ones(40)


plt.figure()
for i, j in enumerate(y):
    if j > 1.8:
        plt.scatter(x[i], j, color="blue")


for i, j in enumerate(y):
    if j < 1.8:
        plt.scatter(x[i], j, color="green")


plt.plot(l, m, color="red",linestyle='--')
plt.plot(x, y_1, color="black")
plt.plot(x, y_2, color="black", linestyle='--')
plt.xlabel("Education Level")
plt.ylabel("Real Expected Wage")
plt.text(1, 4, r'$Women\ with\ Jobs $',
         fontdict={'size': 10, 'color': 'blue'})
plt.text(3, 1, r'$Women\ without\ Jobs $',
         fontdict={'size': 10, 'color': 'green'})
plt.show()
