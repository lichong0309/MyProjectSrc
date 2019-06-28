# 环境仿真，用于界面设计，算法现实仿真（now_cylinder,waiting_sequence）
# 计算算法柱头的移动距离，实现算法柱头移动的可视化

import random
import csv
import matplotlib.pyplot as plt

class network_storage():
    max_cylinder = 100      # 全局标量，最大的柱面
    MaxNumWaitingCylinder = 10 # 全局变量，同一时间内最多能够等待需要执行的柱面数量
    
    def __init__(self):
        self.max_cylinder = 20
        self.MaxNumWaitingCylinder = 10
    
    def Interface(self): 
        self.waiting_sequence = []   # 需要等到执行的柱面序列
        self.now_cylinder = random.randint(0,self.max_cylinder)   # 得到目前针头所在的柱面
        print("============================")
        print("        磁盘调度算法          ")
        print("============================")
        for i in range(0,self.MaxNumWaitingCylinder):
            self.waiting_sequence.append(random.randint(0,self.max_cylinder))
        print("目前针头所在的柱面为：",self.now_cylinder)
        print("等待执行的柱面序列为：",self.waiting_sequence)  

    def computer(self,performance_sequence): 
        self.performance_sequence = performance_sequence
        self.MoveDistance = 0
        temp_now_cylinder = self.now_cylinder
        for i in self.performance_sequence:
            self.MoveDistance = self.MoveDistance + abs(i - temp_now_cylinder)
            temp_now_cylinder = i
        print("针头移动的距离为：",self.MoveDistance)

    def plot(self):
        # x,y轴的数据
        x = list(range(0,self.MaxNumWaitingCylinder+1))
        y = []
        y.append(self.now_cylinder)
        for i in self.performance_sequence:
            y.append(i)
        # x,y轴的坐标标题
        plt.xlabel("x")
        plt.ylabel("cylinder")
        # 设置x,y轴坐标范围和间隔
        plt.xticks(range(self.MaxNumWaitingCylinder),x)    # plt.xticks(坐标范围，坐标值列表)
        plt.yticks(range(self.max_cylinder),list(range(0,self.max_cylinder)))
        plt.plot(x,y,color="r",linestyle="--",marker="*")
        plt.show()
    









        




