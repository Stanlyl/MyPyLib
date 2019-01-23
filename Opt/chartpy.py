# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
 
#添加图形属性
plt.xlabel('这个是行属性字符串')
plt.ylabel('这个是列属性字符串')
plt.title('这个是总标题')
 
y = [10, 11, 12, 13, 14, 20, 16, 17, 18, 19]  #这个是y轴的数据
first_bar = plt.bar(range(len(y)), y, color='blue')  #初版柱形图，x轴0-9，y轴是列表y的数据，颜色是蓝色
 
#开始绘制x轴的数据
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
name_list = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']  #x轴标签
plt.xticks(index, name_list) #绘制x轴的标签
 
#柱形图顶端数值显示
for data in first_bar:
    y = data.get_height()
    x = data.get_x()
    plt.text(x+0.15, y , str(y), va='bottom')  #0.15为偏移值，可以自己调整，正好在柱形图顶部正中
 
#图片的显示及存储
plt.show()   #这个是图片显示
plt.savefig('C:\\Falcon_Proj\\MyPyLib\\filetest\\chart.png')   #图片的存储
plt.close()   #关闭matplotlib
 
