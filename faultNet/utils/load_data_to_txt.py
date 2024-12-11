from src.io.psee_loader import PSEELoader
import os
import random
from dataset_visualization import play_files_parallel
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
# file_path file_1 output_file sample_point_number event_time sample_number
import matplotlib.pyplot as plt
import matplotlib
import random

matplotlib.use('TkAgg')
def test_plot():

    # 定义区域1的左上顶点和右下顶点坐标
    region1_top_left = (100, 100)
    region1_bottom_right = (200, 200)

    # 定义正方形的大小
    square_size = 50

    # 计算可随机选择的范围
    offset_range = region1_bottom_right[0] - region1_top_left[0] - square_size

    # 随机生成正方形的左上顶点坐标
    square_top_left = (
        random.randint(region1_top_left[0], region1_top_left[0] + offset_range),
        random.randint(region1_top_left[1], region1_top_left[1] + offset_range)
    )

    # 计算正方形的右下顶点坐标
    square_bottom_right = (
        square_top_left[0] + square_size,
        square_top_left[1] + square_size
    )

    # 绘制区域和正方形
    fig, ax = plt.subplots()
    ax.set_xlim(region1_top_left[0], region1_bottom_right[0])
    ax.set_ylim(region1_top_left[1], region1_bottom_right[1])

    # 绘制区域1
    region1 = plt.Rectangle(region1_top_left, region1_bottom_right[0] - region1_top_left[0], region1_bottom_right[1] - region1_top_left[1], fc='gray')
    ax.add_patch(region1)

    # 绘制正方形
    square = plt.Rectangle(square_top_left, square_size, square_size, fc='red')
    ax.add_patch(square)

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
    return

def test_obtain_file_name_string():
    file_1 = 'D:\\user\\xutongmiao\\event_data\\data_source\\ballH_1000\\1_cd.dat'

    # 获取倒数第5个字符
    character = file_1[-13:-9]

    print(character)  # 输出结果为 '1'
    return

def test_index():
    file_path = 'D:\\user\\xutongmiao\\faultNet\\data\\faultNet_data'
    file_1 = 'D:\\user\\xutongmiao\\event_data\\data_source\\Healthy_1000\\3_cd.dat'

    regions = [
        [(89, 283), (121, 204)],
        [(180, 285), (230, 198)]
    ]
    fault_name = "healthy"
    cls_name = "healthy_2000"

    speed = file_1[-13:-9]
    print(f"speed :{speed}")
    filename = file_1.split('\\')[-1]  # 获取文件名部分，即'1_cd.dat'
    angle = filename[0]  # 獲得拍照視角
    print(f"angle :{angle}")
    event_time = 6e4  # 一个周期的时间
    sample_point_number = 1024
    sample_number = 140  # 每个类别的样本数

    start_index = ((int(speed) / 500 - 2) * 3 + ((int(angle) + 1) / 2) - 1) * sample_number
    print(f"start_index :{start_index}")
    for i in range(1, sample_number + 1):
        index = int(start_index + i)
        print( f'{file_path}\\{fault_name}\\{fault_name}_{index:04}.txt')
        # current_time = video.current_time


test_plot()