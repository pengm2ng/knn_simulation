from resources import map
from resources import frontier_function
from matplotlib import pyplot as plt
from matplotlib import colors
map_type = map.map_data_ex_2
explored_data = map.map_data1
candidate_list = []


cmap = colors.ListedColormap(['white', 'blue', 'yellow', 'white', 'green', 'black'])
plt.figure(figsize=(6, 6))
plt.pcolor(map_type[::-1], cmap=cmap, edgecolors='k', linewidths=3)
plt.axis('off')
plt.show()