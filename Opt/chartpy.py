# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

GDP = [12406.8,13908.57,9386.87,9143.64]
# 绘图
plt.bar(range(4), GDP, align = 'center',color='steelblue', alpha = 0.8)
# 添加轴标签
plt.xlabel('__xlable__')
plt.ylabel('__ylable__')
# 添加标题
plt.title('__title__')
# 添加刻度标签
plt.xticks(range(4),['x1','x2','x3','x4'])
# 设置Y轴的刻度范围
plt.ylim([5000,15000])
# 为每个条形图添加数值标签
for x,y in enumerate(GDP):
	plt.text(x,y+100,'%s' %round(y,1),ha='center')

plt.savefig('C:\\Falcon_Proj\\MyPyLib\\filetest\\chart.png')   #图片的存储
plt.close()   #关闭matplotlib
 
