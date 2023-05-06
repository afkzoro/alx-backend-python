#!/usr/bin/env python3
""" Modified wait_n """
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """sumary_line

 Keyword arguments:
 argument -- description
 Return: return_description
 """

    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return sorted(delays)
