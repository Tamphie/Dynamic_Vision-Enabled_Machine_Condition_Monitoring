from src.io.psee_loader import PSEELoader
import os
import random
from dataset_visualization import play_files_parallel
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
# file_path file_1 output_file sample_point_number event_time sample_number



matplotlib.use('TkAgg')

# 定义文件位置与每个样本的加载时间
file_path = 'D:\\user\\xutongmiao\\faultNet\\data\\faultNet_data'
file_1 = 'D:\\user\\xutongmiao\\event_data\\data_source\\outerH_1500\\5_cd.dat'

cls_name = "outerH"
regions = [
# [(36, 295), (81, 160)],
#     [(147, 299), (205, 177)],
#     [(59, 285), (97, 201)],
#     [(158, 289), (198, 193)],
    [(152, 267), (178, 229)],
    [(227, 279), (278, 206)]
]



speed = file_1[-13:-9]
filename = file_1.split('\\')[-1]  # 获取文件名部分，即'1_cd.dat'
angle = filename[0]   # 獲得拍照視角


event_time = 4.5e4 # 一个周期的时间
sample_point_number = 1024
sample_number = 140 # 每个类别的样本数

start_index = ((int(speed) / 500 - 2) * 3 + ((int(angle) + 1) / 2) - 1) * sample_number

# 加载文件并设定时间戳为零 读取总时长
video = PSEELoader(file_1)
video.reset()
current_time = video.current_time
print("current time %d" % current_time)
total_time = video.total_time()
print("total time %d" % total_time)


# outer = ball = healthy = 2 inner = 3
events2 = video.load_delta_t(2e4)


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


fig, ax = plt.subplots()
ax.set_xlim(regions[0][0][0], regions[1][1][0])
ax.set_ylim(regions[1][1][1], regions[0][0][1])
# 绘制区域1
region1 = plt.Rectangle((regions[0][0][0],regions[0][1][1]), regions[0][1][0]-regions[0][0][0],
                        regions[0][0][1]-regions[0][1][1], fc='gray')
ax.add_patch(region1)
# 绘制区域2
region2= plt.Rectangle((regions[1][0][0],regions[1][1][1]) ,regions[1][1][0]-regions[1][0][0],
                        regions[1][0][1]-regions[1][1][1], fc='gray')
ax.add_patch(region2)


# 在加载时间内读取，记录事件个数，记录当前时间戳
for i in range(1,sample_number+1):
    index = int(start_index + i)
    output_file = f'{file_path}\\{cls_name}\\{cls_name}_{index:04}.txt'
    # current_time = video.current_time
    events2 = video.load_delta_t(event_time)
    # events2_len = len(events2)
    # print(f"第{i}个样本加载样本个数: {events2_len}")
    # print(f"第{i}个样本current time:{current_time}")

    ROI_events = []
    # 随机选择一个区域
    selected_region = random.choice([0, 1])

    # 获取所选区域的顶点坐标
    region_top_left, region_bottom_right = regions[selected_region]

    # 定义正方形的边长
    square_size = 25

    # 在选定的区域内生成随机正方形区域

    random_region_top_left = (random.randint(region_top_left[0], region_bottom_right[0] - square_size),
               random.randint(region_bottom_right[1] + square_size ,region_top_left[1]))

    random_region_bottom_right = (random_region_top_left[0] + square_size, random_region_top_left[1] - square_size)






    # 绘制正方形


    for event in events2:
        if random_region_top_left[0] < event['x'] < random_region_bottom_right[0] and random_region_bottom_right[1] < event['y'] < random_region_top_left[1]:
            ROI_events.append(event)
    ROI_len = len (ROI_events)
    if len(ROI_events)<sample_point_number:
        square = plt.Rectangle((random_region_top_left[0], random_region_bottom_right[1]), square_size, square_size,
                               fill=False, edgecolor='green')

    else:
        square = plt.Rectangle((random_region_top_left[0], random_region_bottom_right[1]), square_size, square_size,
                               fill=False, edgecolor='red')
    ax.add_patch(square)
    ax.annotate(f'roi{i}', xy=random_region_top_left, xytext=random_region_top_left,
                color='white', fontsize=3,
                bbox=dict(facecolor='blue', edgecolor='blue', boxstyle='round'))

    # 筛选ROI 记录ROI内事件个数
    # ROI1_events = []
    # ROI2_events = []
    # ROI3_events = []
    # ROI4_events = []
    # ROI5_events = []
    # for event in events2:
    #     event['x'] = event['x'] - 75
    #     if 100 < event['x']:
    #         if 160 < event['x'] < 180 and 280 < event['y'] < 300:
    #             ROI1_events.append(event)
    #         elif 140 < event['x'] < 165 and 195 < event['y'] < 220:
    #             ROI2_events.append(event)
    #         elif 170 < event['x'] < 190 and 235 < event['y'] < 250:
    #             ROI3_events.append(event)
    #     else:
    #         if 20 < event['x'] < 35 and 200 < event['y'] < 220:
    #             ROI4_events.append(event)
    #         elif 35 < event['x'] < 55 and 240 < event['y'] < 260:
    #             ROI5_events.append(event)
    # ROI_events = [ROI1_events, ROI2_events, ROI3_events, ROI4_events, ROI5_events]
    # lengths = []
    # for roi in ROI_events:
    #     lengths.append(len(roi))
    # ROI_len = min(lengths)


    # 统计roi最小的样本
    # if i == 1:
    #     ROI_events_min = ROI_len
    #     min_t = 1
    # else:
    #     if ROI_len < ROI_events_min :
    #         ROI_events_min = ROI_len
    #         min_t = i
    # ROI_counts.append(ROI_len)
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

print(f"ROI事件少于{sample_point_number}的片段:{','.join(str(i) for i in sparse_period)}")
# print(f"ROI事件最少为{ROI_events_min}个,对应时间片段为{min_t}")
# plt.plot(range(1,sample_number+1),ROI_counts,'o')
# plt.xlabel('time')
# plt.ylabel('ROI点个数')
# plt.title(f'{cls_name}每个采样片段的ROI点数')
# plt.show()

# 显示图形
plt.axis('equal')
plt.xlabel('x',
               labelpad=-20,  # 调整x轴标签与x轴距离
               x=1.04,  # 调整x轴标签的左右位置
               fontsize=15)
plt.ylabel('y',
               labelpad=-20,  # 调整y轴标签与y轴的距离
               y=1.02,  # 调整y轴标签的上下位置
               rotation=0, fontsize=15)
plt.show()

