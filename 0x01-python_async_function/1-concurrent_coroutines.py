#!/usr/bin/env python3
"""
the wait_n function module
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    listOfDelays: List[float] = []
    for i in range(n):
        listOfDelays.append(await wait_random(max_delay))
    return listOfDelays
