import asyncio
from time import perf_counter
from utils import ResultTimes
import aiohttp


async def fetch(s, url):
    async with s.get(url) as r:
        return await r.text()

async def fetch_all(s, url, k: int):
    tasks = []
    for j in range(k):
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res

async def run_async(config):
    url = config['async']['url']
    N = config['async']['N']
    K = config['async']['K']

    results = []
    for i in range(N):
        start = perf_counter()
        async with aiohttp.ClientSession() as session:
            _ = await fetch_all(session, url, k=K)
        end = perf_counter()
        trial_time = end - start
        result = ResultTimes("async", url, K, 1, None, trial_time / K)
        results.append(result)
    return results

def asyncio_run_async(config):
    return asyncio.run(run_async(config))

if __name__ == '__main__':
    import os
    import toml
    from utils import ROOT_DIR
    with open(os.path.join(ROOT_DIR, 'config.toml')) as f:
        config = toml.load(f)
        
    results = asyncio_run_async(config)
    avg_times = [result.average_time for result in results]
    print(f"Avg Times: {avg_times}")
