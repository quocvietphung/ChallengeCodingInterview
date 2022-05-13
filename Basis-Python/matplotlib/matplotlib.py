import numpy as np
import matplotlib.pyplot as plt
# T½nh tåa  ë x, y cho  ç thà h¼nh sin
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
# Plot the points using matplotlib
plt.plot(x, y)
plt.show() # You must call plt.show() to make graphics appear.