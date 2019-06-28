# FIFO算法的实现
from simulate import network_storage
class alg_FIFO():
    def algorithm(self,now_cylinder,waiting_sequence):
        self.performance_sequence = waiting_sequence
        print("针头移动的柱头顺序为：",self.performance_sequence)
if __name__ == '__main__':
    sim = network_storage()
    sim.Interface()
    alg = alg_FIFO()
    alg.algorithm(sim.now_cylinder,sim.waiting_sequence)
    sim.computer(alg.performance_sequence)
    sim.plot()