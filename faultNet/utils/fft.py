import numpy as np
from scipy.fft import fft, fftfreq
from src.io.psee_loader import PSEELoader
import os
import random
from dataset_visualization import play_files_parallel
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
# file_path file_1 output_file sample_point_number event_time sample_number



matplotlib.use('TkAgg')
# 生成一个 1 秒内采样频率为 1000 Hz 的正弦波信号
t = np.linspace(0, 1, 1000, False)
x = np.sin(2 * np.pi * 50 * t)

# 对时域信号进行离散傅里叶变换
X = fft(x)

# 计算对应的频率序列
freqs = fftfreq(len(x), t[1] - t[0])

# 计算频谱的幅度谱
amplitudes = np.abs(X)

# 输出频谱图

plt.figure(figsize=(12, 6))
plt.plot(freqs, amplitudes)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.show()