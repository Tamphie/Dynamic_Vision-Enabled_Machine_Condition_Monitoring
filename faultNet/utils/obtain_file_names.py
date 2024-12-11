import os

def write_file_names(folder_path, output_file):
    # 遍历文件夹内的所有文件
    file_names = []
    folder_name = os.path.basename(folder_path)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(folder_name, file).replace("\\", "/")
            file_names.append(file_path)

    # 写入文件路径到文本文件
    with open(output_file, 'a') as f:
        for file_name in file_names:
            f.write(f"{file_name}\n")

# 调用函数进行操作
folder_path = 'D:\\user\\xutongmiao\\faultNet\\data\\faultNet_data\\healthy'  # 替换为实际的文件夹路径
output_file = 'D:\\user\\xutongmiao\\faultNet\\data\\faultNet_data\\filelist.txt'   # 输出文件名

write_file_names(folder_path, output_file)