#!/usr/bin/env python3
"""
rite an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for
a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument named
    wait_random that waits for a random delay between 0 and max_delayseconds
    and eventually returns it.
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
