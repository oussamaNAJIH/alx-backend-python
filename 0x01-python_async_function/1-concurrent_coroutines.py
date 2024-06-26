#!/usr/bin/env python3
"""
the wait_n function module
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    akes in 2 int arguments
    return the list of all the delays (float values)
    """
    listOfDelays: List[float] = []
    for i in range(n):
        listOfDelays.append(await wait_random(max_delay))
    return sorted(listOfDelays)
