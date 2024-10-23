from typing import List
import requests
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
from utils import ResultTimes

def run_threading(config) -> List[ResultTimes]:
    url = config['threading']['url']
    N = config['threading']['N']
    K = config['threading']['K']
    THREADS = config['threading']['num_threads']
    results = []

    for i in range(N):
        start = perf_counter()
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            futures = [executor.submit(lambda: requests.get(url)) for _ in range(K)]
            for future in futures:
                _ = future.result()
        end = perf_counter()
        trial_time = end - start
        result = ResultTimes("threading", url, K, THREADS, None, trial_time / K)
        results.append(result)
    return results

if __name__ == "__main__":
    import os
    import toml
    from utils import ROOT_DIR
    with open(os.path.join(ROOT_DIR, 'config.toml')) as f:
        config = toml.load(f)
        
    results = run_threading(config)
    avg_times = [result.average_time for result in results]
    print(f"Avg Times: {avg_times}")
    