import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
# Create a sample data matrix
data = np.random.rand(10, 10)

# Define the colormaps to display
colormaps = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

# Create a figure with subplots
fig, axes = plt.subplots(nrows=3, ncols=6, figsize=(18, 12))

# Loop through the colormaps and plot them
for i, cmap in enumerate(colormaps):
    row = i // 6
    col = i % 6
    axes[row, col].imshow(data, cmap=cmap)
    axes[row, col].set_title(cmap)
    axes[row, col].axis('off')

plt.tight_layout()
plt.show()