from simulate import network_storage
import csv
num = 100
with open("data.csv","a+") as csvfile:
    writer = csv.writer(csvfile)    

    sim = network_storage()
    for i in range(100):
        sim.Interface()
        add_info = [sim.waiting_sequence,sim.now_cylinder]
        writer.writerow(add_info)