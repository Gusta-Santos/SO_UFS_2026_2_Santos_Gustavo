import os
import time
import hashlib
import sys

iteracoes = int(os.environ.get('ITERACOES', 5000000))
print(f"Iniciando cálculo com {iteracoes} iterações...", flush=True)

start_wall = time.time()
start_cpu = time.process_time()

m = hashlib.sha256()
for i in range(iteracoes):
    m.update(b'1')
checksum = m.hexdigest()

end_wall = time.time()
end_cpu = time.process_time()

def read_cgroup(path):
    try:
        with open(path, 'r') as f:
            return f.read().strip()
    except:
        return "N/A"

cpu_max = read_cgroup("/sys/fs/cgroup/cpu.max")
mem_max = read_cgroup("/sys/fs/cgroup/memory.max")
mem_peak = read_cgroup("/sys/fs/cgroup/memory.peak")
pids_max = read_cgroup("/sys/fs/cgroup/pids.max")

print(f"RES,{iteracoes},{checksum},{end_wall - start_wall:.4f},{end_cpu - start_cpu:.4f},{cpu_max},{mem_max},{mem_peak},{pids_max}", flush=True)
