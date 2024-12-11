from src.io.psee_loader import PSEELoader
import os
import random
from dataset_visualization import play_files_parallel
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
# file_path file_1 output_file sample_point_number event_time sample_number

# 定义文件位置与每个样本的加载时间
file_path = 'D:\\user\\xutongmiao\\faultNet\\data\\faultNet_data'
file_1 = 'D:\\user\\xutongmiao\\event_data\\innerH_1000_1_cd.dat'
cls_name = "innerH_1000"
event_time = 6e4 # 改变时长以减少点的个数
sample_point_number = 1810
sample_number = 239 # 每个类别的样本数
# 加载文件并设定时间戳为零 读取总时长
video = PSEELoader(file_1)
video.reset()
current_time = video.current_time
print("current time %d" % current_time)
total_time = video.total_time()
print("total time %d" % total_time)


# outer = ball = healthy = 2 inner = 3
events2 = video.load_delta_t(3e4)


# events = video.load_n_events(100000)
#
# x_len = len(events['x'])
# y_len = len(events['y'])
# t_len = len(events['t'])
# p_len = len(events['p'])
# print(cls_name)
# print(f"x长度: {x_len}")
# print(f"y长度: {y_len}")
# print(f"t长度: {t_len}")
# print(f"p长度: {p_len}")
# output_file = f'D:\\事件相机\\{cls_name}_001.txt'
# with open(output_file, 'w') as f:
#     for event in events:
#         x = event['x']
#         y = event['y']
#         t = event['t']
#         p = event['p']
#
#
#         line = f"{x},{y},{t},{p}\n"
#         f.write(line)

#

# 记录ROI事件少于sample_point_number的时间片段 记录各个时间片段的ROI点数
sparse_period = []
ROI_counts = []


# 在加载时间内读取，记录事件个数，记录当前时间戳
for i in range(1,sample_number+1):

    output_file = f'{file_path}\\{cls_name}\\{cls_name}_{i:03}.txt'
    # current_time = video.current_time
    events2 = video.load_delta_t(event_time)
    events2_len = len(events2)
    # print(f"第{i}个样本加载样本个数: {events2_len}")
    # print(f"第{i}个样本current time:{current_time}")

    # 筛选ROI 记录ROI内事件个数
    ROI_events = []
    for event in events2:
        if 150 < event['x'] < 200 and 270 < event['y'] < 290:
            ROI_events.append(event)
    ROI_len = len(ROI_events)
    # 统计roi最小的样本
    # if i == 1:
    #     ROI_events_min = ROI_len
    #     min_t = 1
    # else:
    #     if ROI_len < ROI_events_min :
    #         ROI_events_min = ROI_len
    #         min_t = i
    ROI_counts.append(ROI_len)
    print(f"第{i}个样本ROI事件个数: {ROI_len}")
    # 筛选3w个数（假设 sample_point_number 为 30000）
    if sample_point_number > ROI_len:
        sparse_period.append(i)
        continue
    random_events = random.sample(ROI_events, sample_point_number)
    with open(output_file, 'w') as f:
        for event in random_events:
            x2 = float(event['x'])
            y2 = float(event['y'])
            t2 = float(event['t'])
            p2 = float(event['p'])
            line = f"{x2},{y2},{t2},{p2}\n"
            f.write(line)
# print(f"ROI事件少于{sample_point_number}的片段:{','.join(str(i) for i in sparse_period)}")
# print(f"ROI事件最少为{ROI_events_min}个,对应时间片段为{min_t}")
# plt.plot(range(1,sample_number+1),ROI_counts,'o')
# plt.xlabel('time')
# plt.ylabel('ROI点个数')
# plt.title(f'{cls_name}每个采样片段的ROI点数')
# plt.show()


