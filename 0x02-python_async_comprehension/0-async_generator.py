#!/usr/bin/env python3
""" Async generator """
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Asynchronous generator that yields a random float between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
