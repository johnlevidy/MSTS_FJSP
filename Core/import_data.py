import numpy as np

"""
Import data from benchmarking tests
"""

def next_noncomment_line(f):
    tmp = f.readline()
    if tmp == '':
        return ''
    while tmp[0] == '#':
        tmp = f.readline()
        if tmp == '':
            return ''
        continue
    return tmp

def import_txt_data(filename):
    with open(filename) as f:
        line = next_noncomment_line(f)
        line = line.split()
        num_ops, num_edges, num_machs = int(line[0]), int(line[1]), int(line[2])

        op_precedence = []
        op_machines = []
        t_times = np.zeros([num_machs, num_machs], dtype=np.uint8)

        for i in range(num_edges):
            line = next_noncomment_line(f)
            print(f"Edge: {line}")
            line = line.split()
            op_precedence.append(line)
        
        for i in range(num_ops):
            line = next_noncomment_line(f)
            print(f"Operation: {line}")
            line = line.split()
            line.insert(0, str(i))
            op_machines.append(line)

        for i in range(num_machs):
            line = next_noncomment_line(f) 
            if line == '':
                t_times = None
                break
            line = line.split()
            line = [int(x) for x in line]
            t_times[i] = np.array(line)

    f.close
    return op_precedence, op_machines, t_times
