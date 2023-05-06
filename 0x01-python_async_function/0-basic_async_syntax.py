#!/usr/bin/env python3
""" asynchronous coroutine """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random

 Args:
     max_delay (int): _description_. Defaults to 10.

 Returns:
     float:delay
   """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
