#!/usr/bin/env python3
"""
the task_wait_n function module
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    akes in 2 int arguments
    return the list of all the delays (float values)
    """
    listOfDelays: List[float] = []
    for i in range(n):
        taskRandom: float = await task_wait_random(max_delay)
        listOfDelays.append(taskRandom)
    return sorted(listOfDelays)
