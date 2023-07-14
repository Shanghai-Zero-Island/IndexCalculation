import math
import numpy as np
def get_distance(x1, y1, z1, x2, y2, z2, coff):
    return math.sqrt(pow((x1 - x2) * coff, 2) + pow((y1 - y2) * coff, 2) + pow((z1 - z2) * coff, 2))

path = 'Player1.txt'
player_list = []
participant_count = 7
npc_list0 = []
npc_list1 = []
npc_list2 = []
npc_list3 = []
npc_list4 = []
npc_list5 = []
npc_list6 = []
t_max = 0
with open(path, 'r') as f:
    for i in f.readlines():
        data_list = i.split('|')
        for j in range(2, 5):
            data_list[j] = data_list[j].replace(',', '')
        # print(data_list)
        if data_list[0] == '0':
            npc_list0.append(data_list)
        elif data_list[0] == '1':
            npc_list1.append(data_list)
        elif data_list[0] == '2':
            npc_list2.append(data_list)
        elif data_list[0] == '3':
            npc_list3.append(data_list)
        elif data_list[0] == '4':
            npc_list4.append(data_list)
        elif data_list[0] == '5':
            npc_list5.append(data_list)
        elif data_list[0] == '6':
            npc_list6.append(data_list)
        else:
            player_list.append(data_list)
        # index = data_list[0]
        # bis_Player = data_list[1]
        # x = data_list[2]
        # y = data_list[3]
        # z = data_list[4]
        # t = data_list[5]
    # print(player_list)


dataset = []
dataset.append(npc_list0)
dataset.append(npc_list1)
dataset.append(npc_list2)
dataset.append(npc_list3)
dataset.append(npc_list4)
dataset.append(npc_list5)
dataset.append(npc_list6)
# dataset.append(player_list)
# print(float(dataset[0][5][2]))
# print(float(dataset[1][4][3]))
# print(float(dataset[5][2][2]))


def all_time_density(t_max):
    density = []
    r = 0.7
    c = 1 / (math.pi * r * r)
    for t in range(0, t_max, 1):
        density_each_step = []
        for i in range(0, participant_count):
            tem_p = 0.0
            for j in range(0, participant_count):
                tem_p += c * math.e ** (-pow(get_distance(float(dataset[i][t][2]), float(dataset[i][t][3]), float(dataset[i][t][4]), float(dataset[j][t][2]), float(dataset[j][t][3]), float(dataset[j][t][4]), 0.01), 2))
            density_each_step.append(tem_p)
        density.append(density_each_step)
    return density

t_max = int(float(t_max) * 10)

# shape n * m
# n = players
# m = times
density = all_time_density(400)

density_np = np.array(density)
density_np.resize((density_np.shape[1], density_np.shape[0]))

# 指标1
def index_max_density():
    return max([max(_) for _ in density])

# 指标2
def index_average_density():
    return sum([sum(_) for _ in density]) / (len(density[0]) * len(density))

# 指标4
def index_std_time_density():
    std_list = []
    for i in density_np:
        std_list.append(np.std(i))
    return std_list

# 指标5
def evacuation_time():
    with open(path, 'r') as f:
        return f.readlines()[-1].split('|')[-1]

print('最大密度：', index_max_density(), '人/平方米')
print('平均密度：', index_average_density(), '人/平方米')
print('密度时间不均匀性：', index_std_time_density())
print('疏散时间： ', evacuation_time(), '秒')



# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd
# # %matplotlib notebook
# from pylab import mpl
# # 设置字体，防止中文乱码
# arr = np.random.rand(3, 3)
# # print(arr)
# mpl.rcParams['font.sans-serif'] = ['FangSong']
# # 生成一个3x3的随机矩阵
# arr = np.random.rand(3, 3)
# fig, ax = plt.subplots(figsize = (6, 5))
# cc = np.array(density)
# dd = cc.resize(20, 20)
# # print(cc.shape)
# print(arr.shape)
# # 调动heatmap方法，annot表示注释，即方格中的数字，cmap表示颜色代码
# sns.heatmap(pd.DataFrame(cc), cmap="YlGnBu")
# # 设置标题、坐标轴标签及字体大小
# ax.set_title('热力图', fontsize = 14)
# ax.set_ylabel('Y', fontsize = 14)
# ax.set_xlabel('X', fontsize = 14)
# print(cc.shape)
# plt.show()