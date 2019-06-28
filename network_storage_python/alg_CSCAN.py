# CSCAN算法的实现
from simulate import network_storage

class alg_CSCAN():
    def sort_sequence(self,waiting_sequence):
        for i in range(len(waiting_sequence) - 1):     # 循环次数
            for j in range(len(waiting_sequence)-1-i):    # 每次循环比较的次数
                if waiting_sequence[j] > waiting_sequence[j+1]:
                    temp = waiting_sequence[j+1]
                    waiting_sequence[j+1] = waiting_sequence[j]
                    waiting_sequence[j] = temp
        print("排序之后的等待执行的柱面序列为：",waiting_sequence)
        return waiting_sequence

    def algorithm(self,now_cylinder,waiting_sequence):
        waiting_sequence = self.sort_sequence(waiting_sequence)
        self.performance_sequence = []
        # 从里向外循环
        for i in range(len(waiting_sequence)):
            if waiting_sequence[i] >= now_cylinder:
                break
        
        for j in range(i, len(waiting_sequence)):
            self.performance_sequence.append(waiting_sequence[j])
        
        for a in range(0, i):
            self.performance_sequence.append(waiting_sequence[a])
        print("针头移动的柱头顺序为：",self.performance_sequence)

if __name__ == '__main__':
    sim = network_storage()
    sim.Interface()
    alg = alg_CSCAN()
    alg.algorithm(sim.now_cylinder,sim.waiting_sequence)
    sim.computer(alg.performance_sequence)
    sim.plot()


        

