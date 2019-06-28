# SSTF算法的实现

from simulate import network_storage
class alg_SSTF():
    # 计算目前针头到各个等待执行柱头的距离
    def computer_distance(self,now_cylinder,waiting_cylinder):
        self.distance = []
        for i in waiting_cylinder:
            self.distance.append(abs(now_cylinder - i))

    def algorithm(self,now_cylinder,waiting_sequence):
        self.performance_sequence = []
        for a in range(len(waiting_sequence)):
            self.computer_distance(now_cylinder,waiting_sequence)
            # 寻找列表中最小值，并返回所在的位置
            min_local = self.distance.index(min(self.distance))
            self.performance_sequence.append(waiting_sequence[min_local])
            now_cylinder = waiting_sequence[min_local]
            del waiting_sequence[min_local]
        print("针头移动的柱头顺序为：",self.performance_sequence)
        
if __name__ == '__main__':
    sim = network_storage()
    sim.Interface()
    alg = alg_SSTF()
    alg.algorithm(sim.now_cylinder, sim.waiting_sequence)
    sim.computer(alg.performance_sequence)
    sim.plot()


        

        