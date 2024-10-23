from typing import List
import requests
from time import perf_counter
from utils import ResultTimes

def run_basic(config) -> List[ResultTimes]:
    url = config['basic']['url']
    N = config['basic']['N']
    K = config['basic']['K']
    
    max_time = 0
    results = []
    for i in range(N):
        trial_time = 0
        for j in range(K):
            start = perf_counter()
            _ = requests.get(url)
            end = perf_counter()
            cur_time = end - start
            max_time = max(max_time, cur_time)
            trial_time += cur_time
        result = ResultTimes("basic", url, K, 1, max_time, trial_time / K)
        results.append(result)
    return results
    
if __name__ == '__main__':
    import os
    import toml
    from utils import ROOT_DIR
    with open(os.path.join(ROOT_DIR, 'config.toml')) as f:
        config = toml.load(f)
        
    results = run_basic(config)
    avg_times = [result.average_time for result in results]
    max_time = max(result.max_time for result in results)
    
    print(f"Max time: {max_time}")
    print(f"Avg Times: {avg_times}")