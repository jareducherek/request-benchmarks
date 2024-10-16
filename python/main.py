from threaded import run_threading
from basic import run_basic
import pandas as pd
from utils import ROOT_DIR
import toml
import os

def main():
    # read in config.toml
    with open(os.path.join(ROOT_DIR, 'config.toml')) as f:
        config = toml.load(f)
    
    all_results = []
    for func in run_basic, run_threading:
        results = func(config)
        all_results.extend(results)
        
    df_results = pd.DataFrame([result.__dict__ for result in results])    
    df_results.to_csv(os.path.join(ROOT_DIR, "python_results.csv"), index=False)

if __name__ == "__main__":
    main()