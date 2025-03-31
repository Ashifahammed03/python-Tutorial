import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot two lines on the same graph
plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='-')
plt.plot(x, y2, label='Cosine Wave', color='red', linestyle='--')

# Labels, title, and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Waves')
plt.legend()

# Show plot
plt.show()
