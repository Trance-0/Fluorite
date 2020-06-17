import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
# np.random.seed(19680823)

# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
# radii=8
radii = 10 * np.random.rand(N)
# width=1
# width = np.pi / 4 * np.random.rand(N)
width=2*np.pi/N

colors = plt.cm.viridis(radii / 10.)

ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=5, color=colors, alpha=0.5)

plt.show()