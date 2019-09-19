from hotel import scrap_hotel

import matplotlib.pyplot as plt

all_data = {}
colours = ['green', 'orange', 'red', 'blue', 'black', 'pink', 'yellow']

# range_list = []

# for i in range(1, 100000):
#     range_list.append(i)

all_data = scrap_hotel(all_data)

fig = plt.figure()
ax = fig.add_subplot(111)

for colour, (x, ys) in zip(colours, all_data.items()):
    ax.scatter([x], ys, c=colour, linewidth=0, s=50)

plt.show()