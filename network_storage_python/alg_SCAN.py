# SCAN算法的实现

from simulate import network_storage

class alg_SCAN():
    # 从小到大冒泡排序
    def sort_sequence(self,waiting_sequence):
        for i in range(len(waiting_sequence) - 1):
            for j in range(len(waiting_sequence) - 1 -i):
                if waiting_sequence[j+1] <= waiting_sequence[j]:
                    temp = waiting_sequence[j+1]
                    waiting_sequence[j+1] = waiting_sequence[j]
                    waiting_sequence[j] = temp
        print("排序之后的等待执行的柱面序列为：",waiting_sequence)
        return waiting_sequence    # 返回排序过后的waiting_sequence
    
    def algorithm(self,now_cylinder, waiting_sequence):
        #print("传输函数中的形参waiting_sequence为：",waiting_sequence)
        waiting_sequence = self.sort_sequence(waiting_sequence)
        #print("排序之后的waiting_sequence为：",waiting_sequence)
        self.performance_sequence = []    # 定义performance_sequence
        
        
        # 从内向外，从底到高循环
        # 第一部分
        for i in range(len(waiting_sequence)):
            if waiting_sequence[i] >= now_cylinder:
                break
        
        for j in range(i,len(waiting_sequence)):
            self.performance_sequence.append(waiting_sequence[j])
        #print("第一部分的performance_sequence：",self.performance_sequence)

        # 第二部分
        # 翻转waiting_sequence列表 
        waiting_sequence = waiting_sequence[::-1]
        #print("翻转过后的waiting_sequence为：",waiting_sequence)
        #print("现在磁头所在的位置为:",now_cylinder)
        for m in range(len(waiting_sequence)):
            if waiting_sequence[m] < now_cylinder:
                break

        for a in range(m,len(waiting_sequence)):
            self.performance_sequence.append(waiting_sequence[a])
            #print("第二部分之后的performance_sequence为：",self.performance_sequence)

        print("针头移动的柱头顺序为：",self.performance_sequence)
        
if __name__ == '__main__':
    sim = network_storage()
    sim.Interface()
    alg = alg_SCAN()
    alg.algorithm(sim.now_cylinder,sim.waiting_sequence)
    sim.computer(alg.performance_sequence)
    sim.plot()

        

