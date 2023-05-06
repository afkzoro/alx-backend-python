#!/usr/bin/env python3
"""The total runtime of 10 seconds is due to the fact that each call to
async_comprehension is awaiting for 10 random numbers to be generated with
a one-second delay between each number """
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """_summary_

 Returns:
     float: _description_
 """
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end_time = perf_counter()
    return end_time - start_time
