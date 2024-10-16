from typing import List
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from utils import ResultTimes

def run_threading(config) -> List[ResultTimes]:
    url = config['threading']['url']
    N = config['threading']['N']
    K = config['threading']['K']
    THREADS = config['threading']['num_threads']
    results = []

    for i in range(N):
        start = time.time()
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            futures = [executor.submit(lambda: requests.get(url)) for _ in range(K)]
            for future in futures:
                _ = future.result()
        end = time.time()
        trial_time = end - start
        result = ResultTimes("threading", url, K, THREADS, None, trial_time / K)
        results.append(result)
    return results

if __name__ == "__main__":
    results = run_threading()
    avg_times = [result.average_time for result in results]
    max_time = max(result.max_time for result in results)
    print(f"Max time: {max_time}")
    print(f"Avg Times: {avg_times}")
    