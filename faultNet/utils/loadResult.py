import  torch
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# model = torch.load("D:\\user\\xutongmiao\\faultNet\\log\\classification\\2024-03-24_15-12\\checkpoints\\best_model.pth")
# print(model)
# for name, param in model.named_parameters():
#     print(name,param)

log_file = 'D:\\user\\xutongmiao\\faultNet\\log\\classification\\2024-05-30_22-10\\logs\\pointnet2_cls_msg.txt'
with open(log_file,'r') as file:
    lines = file.readlines()
train_loss_new = []
train_loss = []
train_acc_new = []
train_acc = []

for line in lines:
    if " - Loss:" in line:
        loss = float(line.split("Loss:")[1].strip())
        train_loss.append(loss)
        #train_loss_new = [x - 0.7 for x in train_loss]

    elif " - Train Instance Accuracy:" in line:
        acc = float(line.split("Train Instance Accuracy:")[1].strip())
        train_acc.append(acc)
        #train_acc_new = [x + 0.3 for x in train_acc]


print(train_loss)
print(train_acc)
plt.plot(range(1,201),train_loss)
plt.xlabel('epoch')
plt.ylabel('Loss')
plt.title('Loss Per Epoch')
plt.show()
plt.plot(range(1,201),train_acc)
plt.xlabel('epoch')
plt.ylabel('Acc')
plt.title('Acc Per Epoch')
plt.show()