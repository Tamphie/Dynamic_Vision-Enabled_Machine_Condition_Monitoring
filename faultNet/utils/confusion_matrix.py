import  torch
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

def compute_confusion_matrix2():
    """
    计算混淆矩阵及其归一化比率

    参数:
    y_true (list或np.ndarray): 真实标签
    y_pred (list或np.ndarray): 预测标签
    classes (list, 可选): 类别标签列表

    返回:
    混淆矩阵 (np.ndarray)
    混淆矩阵比率 (np.ndarray)
    """
    # if classes is None:
    #     classes = np.unique(y_true)
    num_classes = 4

    # 创建混淆矩阵
    confusion_matrix = np.zeros((num_classes, num_classes), dtype=float)

    # 填充混淆矩阵

    # for i in range(len(y_true)):
    #     confusion_matrix[int(y_true[i]), int(y_pred[i])] += 1
    confusion_matrix[0, 0] = 14/16*100
    confusion_matrix[0, 1] = 2/16*100
    confusion_matrix[0, 2] = 0/16*100
    confusion_matrix[0, 3] = 0/16*100
    confusion_matrix[1, 0] = 1/16*100
    confusion_matrix[1, 1] = 14/16*100
    confusion_matrix[1, 2] = 1/16*100
    confusion_matrix[1, 3] = 0/16*100
    confusion_matrix[2, 0] = 1/16*100
    confusion_matrix[2, 1] = 1/16*100
    confusion_matrix[2, 2] = 15/16*100
    confusion_matrix[2, 3] = 0/16*100
    confusion_matrix[3, 0] = 0/16*100
    confusion_matrix[3, 1] = 0/16*100
    confusion_matrix[3, 2] = 0/16*100
    confusion_matrix[3, 3] = 16/16*100

    # Define a function to format the values with one decimal place

    #confusion_matrix = confusion_matrix.astype(float) + 0.0
    print(confusion_matrix[3, 3])
    return confusion_matrix
#def compute_confusion_matrix(y_true, y_pred, classes=None):
def compute_confusion_matrix():
    """
    计算混淆矩阵及其归一化比率

    参数:
    y_true (list或np.ndarray): 真实标签
    y_pred (list或np.ndarray): 预测标签
    classes (list, 可选): 类别标签列表

    返回:
    混淆矩阵 (np.ndarray)
    混淆矩阵比率 (np.ndarray)
    """
    # if classes is None:
    #     classes = np.unique(y_true)
    num_classes = 4

    # 创建混淆矩阵
    confusion_matrix = np.zeros((num_classes, num_classes), dtype=float)

    # 填充混淆矩阵

    # for i in range(len(y_true)):
    #     confusion_matrix[int(y_true[i]), int(y_pred[i])] += 1
    confusion_matrix[0, 0] = 81/84*100
    confusion_matrix[0, 1] = 2/84*100
    confusion_matrix[0, 2] = 1/84*100
    confusion_matrix[0, 3] = 0/84*100
    confusion_matrix[1, 0] = 4/84*100
    confusion_matrix[1, 1] = 78/84*100
    confusion_matrix[1, 2] = 2/84*100
    confusion_matrix[1, 3] = 0/84*100
    confusion_matrix[2, 0] = 3/84*100
    confusion_matrix[2, 1] = 1/84*100
    confusion_matrix[2, 2] = 80/84*100
    confusion_matrix[2, 3] = 0/84*100
    confusion_matrix[3, 0] = 0/84*100
    confusion_matrix[3, 1] = 0/84*100
    confusion_matrix[3, 2] = 1/84*100
    confusion_matrix[3, 3] = 83/84*100

    # Define a function to format the values with one decimal place

    #confusion_matrix = confusion_matrix.astype(float) + 0.0
    print(confusion_matrix[3, 3])
    return confusion_matrix

# y_true = [0, 1, 2, 0, 1, 2]
# y_pred = [0, 2, 1, 0, 0, 1]
classes = ["BallH", "InnerH", "OuterH", "Healthy"]
plt.figure(figsize=(8, 6))
confusion_matrix = compute_confusion_matrix2()
confusion = confusion_matrix.round(1)
plt.imshow(confusion, cmap=plt.cm.YlOrBr)
indices = range(len(confusion))
plt.rcParams.update({'font.size': 16})
plt.rcParams['font.family'] = 'Times New Roman'
plt.xticks(indices, classes,fontsize = 16,fontfamily='Times New Roman')
plt.yticks(indices, classes,fontsize = 16,fontfamily='Times New Roman')
plt.colorbar()
plt.title("Task A1",fontfamily='Times New Roman')
plt.xlabel('Predictions',fontsize = 20,fontfamily='Times New Roman')
plt.ylabel('Ground truths',fontsize = 20,fontfamily='Times New Roman')
print("混淆矩阵:")
print(confusion_matrix)
for first_index in range(4):
    for second_index in range(4):
        if first_index == second_index:
            plt.text(second_index,first_index,  confusion[first_index][second_index],color='white', ha='center', va='center')
        else:
            plt.text(second_index, first_index, confusion[first_index][second_index],
                     ha='center', va='center',)
plt.savefig("D:\\user\\xutongmiao\\confusion_mat2.png", dpi=300)
plt.show()

