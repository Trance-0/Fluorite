import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
# np.random.seed(19680823)

# Compute pie slices
N = 10
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
# radii=8
radii = 10 * np.random.rand(N)
# width=1
# width = np.pi / 4 * np.random.rand(N)
width=np.pi/N*2

colors = plt.cm.viridis(radii / 10.)

ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=5, color=colors, alpha=0.5)

plt.show()