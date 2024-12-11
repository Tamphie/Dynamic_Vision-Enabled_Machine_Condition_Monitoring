import  torch
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np


# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams.update({'font.size': 16})


# 准备数据
labels = ['Single-perspective','Multi-perspective ' ]
label = ['A1','A2','B1','B2']
values = [87.5, 94.7,93.2 ,95.4 ]

# 设置图形大小
plt.figure(figsize=(6, 5))

# 绘制条形图
bar_width = 0.12
x = [0.15,0.28,0.5,0.63]
plt.bar(x[0], values[0], bar_width, color=(247/255,239/255,174/255))
plt.bar(x[1], values[1], bar_width, color=(243/255,200/255,70/255))
plt.bar(x[2], values[2], bar_width, color=(139/255,181/255,209/255),)
plt.bar(x[3], values[3], bar_width, color=(74/255,114/255,152/255) ,)
plt.legend(label,ncol=2,loc=2 )

# 设置刻度线
plt.xticks([0.215,0.565], labels)
plt.ylim(80,100)
plt.yticks(np.arange(80, 101, 4))
plt.grid(axis='y', color='gray', linestyle='--')

# 添加标题和坐标轴标签

plt.xlabel('Camera Position',fontsize = 18)
plt.ylabel('Testing Accuracy (%)',fontsize= 18)


plt.savefig("D:\\user\\xutongmiao\\Bar.png", dpi=300)
# 显示图形
plt.show()
