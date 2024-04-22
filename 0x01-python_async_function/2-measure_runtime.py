#!/usr/bin/env python3
"""
the measure_time function module
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
     measures the total execution time for wait_n
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    timeframe: float = (end_time - start_time) / n
    return timeframe
