#!/usr/bin/env python3
""" Async generator in python """
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous generator that yields a random float between 0 and 10

 Returns:
     AsyncGenerator[float, None]: _description_

 Yields:
     Iterator[AsyncGenerator[float, None]]: _description_
 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
