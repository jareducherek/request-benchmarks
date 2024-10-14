import requests
import toml
import os
import time

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# read in config.toml
with open(os.path.join(ROOT_DIR, 'config.toml')) as f:
    config = toml.load(f)
    
url = config['basic']['url']
N = config['basic']['N']
K = config['basic']['K']

max_time = 0
avg_times = []
for i in range(N):
    trial_time = 0
    for j in range(K):
        start = time.time()
        response = requests.get(url)
        end = time.time()
        cur_time = end - start
        max_time = max(max_time, cur_time)
        trial_time += cur_time
    avg_times.append(trial_time / K)
    print(f"Trial {i+1}: {trial_time} seconds")
    
print(f"Max time: {max_time}")
print(f"Avg Times: {avg_times}")