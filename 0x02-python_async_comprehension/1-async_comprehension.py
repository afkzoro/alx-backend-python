#!/usr/bin/env python3
""" write a coroutine called async_comprehension that takes no arguments """
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

 Returns:
     List[int]: _description_
 """

    return [x async for x in async_generator()]
