from src.io.psee_loader import PSEELoader
import os
import random
from dataset_visualization import play_files_parallel
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

plt.rcParams['font.family'] = 'Times New Roman'
# file_path file_1 output_file sample_point_number event_time sample_number


# 定义文件位置与每个样本的加载时间
file_path = 'D:\\user\\xutongmiao\\event_data\\healthy2000'
file_1 = 'D:\\user\\xutongmiao\\event_data\\data_source\\ballH_1000\\1_cd.dat'
cls_name = "healthy1000"
output_file = f'{file_path}\\{cls_name}_3.txt'


event_time = 1e3 # 一个周期的时间
#sample_point_number = 1810
sample_number = 140 # 每个类别的样本数
# 加载文件并设定时间戳为零 读取总时长
video = PSEELoader(file_1)
video.reset()
current_time = video.current_time
#print("current time %d" % current_time)
total_time = video.total_time()
#print("total time %d" % total_time)
timestamp = []
event_num = []
ROI_events = []

# outer = ball = healthy = 2 inner = 3
events = video.load_delta_t(2e4)
current_time = video.current_time
#print("current time %d" % current_time)
for i in range(1,sample_number+1):
    events = video.load_delta_t(event_time)
    # for event in events:
    #     if 0 < event['x'] < 200 and 160 < event['y'] < 320:
    #         ROI_events.append(event)
    length = len(events)
    #print("current time %d event_number %d" % (current_time,length))
    timestamp.append(current_time/10000)
    event_num.append(length)
    current_time = video.current_time
print(event_num)
#print(len(event_num))
# 创建图形
fig, ax = plt.subplots()

# 绘制散点图
ax.plot(timestamp, event_num, marker='o',markerfacecolor=(74/255,114/255, 152/255),  markeredgecolor='none', color = (139/255,181/255,209/255),linestyle='--')

# 设置标签和标题
ax.set_xlabel('Time(0.01s)', fontsize=18)
ax.set_ylabel('Event Number',  fontsize=18)
#ax.set_title('Current Time vs Event Number')

# 显示图形
plt.show()