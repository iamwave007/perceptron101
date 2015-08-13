import numpy as np
import matplotlib.pyplot as plt


# x = np.arange(0, 5, 0.01);
# # y = 1.0 - x ** 2
# plt.plot(x, y)
# plt.grid(True)
# plt.show()
np.random.seed(101)
g = np.floor(np.random.random((100, 100)) + .5)

plt.subplot(211)
plt.imshow(g)
plt.subplot(212)
plt.imshow(g, cmap='Greys',  interpolation='nearest')
plt.savefig('blkwht.png')

plt.show()