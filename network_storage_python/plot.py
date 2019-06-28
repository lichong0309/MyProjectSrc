# 画四种算法在相同环境下磁头的移动距离的比较
# 相同的waiting_sequence,now_cylinder 
import csv
import matplotlib.pyplot as plt
from simulate import network_storage
from alg_FIFO import alg_FIFO
from alg_SCAN import alg_SCAN
from alg_SSTF import alg_SSTF
from alg_CSCAN import alg_CSCAN

# 实例化
alg_FIFO = alg_FIFO()
alg_SSTF = alg_SSTF()
alg_SCAN = alg_SCAN()
alg_CSCAN = alg_CSCAN()

sim = network_storage()
plot_point_x = []    # 画图中的x轴的点的集合
# 画图中的y轴的点的集合
plot_point_y_FIFO = []
plot_point_y_SSTF = []
plot_point_y_SCAN = []
plot_point_y_CSCAN = []  

for i in range(100):
    sim.Interface()
    plot_point_x.append(i)

    # 执行算法
    alg_FIFO.algorithm(int(sim.now_cylinder),list(sim.waiting_sequence))
    
    alg_SCAN.algorithm(int(sim.now_cylinder),list(sim.waiting_sequence))
    alg_CSCAN.algorithm(int(sim.now_cylinder),list(sim.waiting_sequence))
    alg_SSTF.algorithm(int(sim.now_cylinder),list(sim.waiting_sequence))

    # 计算各个算法针头移动的距离
    sim.computer(alg_FIFO.performance_sequence)
    plot_point_y_FIFO.append(sim.MoveDistance)

    sim.computer(alg_SSTF.performance_sequence)
    plot_point_y_SSTF.append(sim.MoveDistance)
    
    sim.computer(alg_SCAN.performance_sequence)
    plot_point_y_SCAN.append(sim.MoveDistance)

    sim.computer(alg_CSCAN.performance_sequence)
    plot_point_y_CSCAN.append(sim.MoveDistance)

# 画图
plt.figure()
plt.xlabel("x")
plt.ylabel("MoveDistance")

plt.scatter(plot_point_x,plot_point_y_FIFO,marker='x',color='m',label='alg_FIFO')
plt.scatter(plot_point_x,plot_point_y_SSTF,marker='+',color='c',label='alg_SSTF')
plt.scatter(plot_point_x,plot_point_y_SCAN,marker='o',color='r',label='alg_SCAN')
plt.scatter(plot_point_x,plot_point_y_CSCAN,marker='*',color='k',label='alg_CSCAN')

# plt.plot(plot_point_x,plot_point_y_FIFO,marker='x',color='m')
# plt.plot(plot_point_x,plot_point_y_SSTF,marker='+',color='c')
# plt.plot(plot_point_x,plot_point_y_SCAN,marker='o',color='r')
# plt.plot(plot_point_x,plot_point_y_CSCAN,marker='*',color='k')

plt.show()