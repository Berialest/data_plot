# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# get data name to build list
data_name = []
with open('./data/data_name.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        data_name.append(line.replace('\n', ''))

# get data, x axis is data_name[0]
i = 0
data_name_range = []
for file in data_name:
    data_name_range.append(file)
    data_name_range[i] = []
    with open('./data/' + file + '.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            data_name_range[i].append(float(line.replace('\n', '')))
    i = i + 1

# set parameter
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
linestyle = ['-', '--', '-.', ':']

# plot
plt.figure(figsize=(8,7))
data_name_leng = len(data_name)
for plot_index in range(1, data_name_leng):
    plt.plot(data_name_range[0], data_name_range[plot_index], label = data_name, color = color[plot_index-1], marker='p', linestyle = linestyle[0])
plt.grid(axis='y') # close y grid
plt.grid(axis='x') # close x grid
plt.ylabel('浓度/ppm', fontproperties='SimHei')
plt.xlabel('温度/T', fontproperties='SimHei')
plt.legend(data_name[1:data_name_leng])
plt.yticks(range(0,500,30))
plt.savefig('./figure/line.png')
plt.show()