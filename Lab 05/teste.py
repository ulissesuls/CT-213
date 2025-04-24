import numpy as np
import matplotlib.pyplot as plt

num_samples = 1000
mu = np.array([1.0, 0.0])
C = np.array([[1.0, 0.5], [0.5, 1]])
X = np.random.multivariate_normal(mu, C, num_samples)

plt.figure()
plt.plot(X[:,0], X[:,1], '.')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()