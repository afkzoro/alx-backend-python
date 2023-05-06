#!/usr/bin/env python3
""" async function """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> any:
    """
    Regular function that creates a asyncio.Task object that calls
    wait_random() with the given max_delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
