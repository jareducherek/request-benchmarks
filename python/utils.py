from dataclasses import dataclass
from typing import Optional
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@dataclass
class ResultTimes:
    run_type: str
    url: str
    K: int
    num_threads: int
    max_time: float
    average_time: Optional[float]