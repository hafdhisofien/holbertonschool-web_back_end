#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime measure the total runtime (four times)
    and return it.
    """
    start = time.time()
    run_it = [async_comprehension() for i in range(4)]
    await asyncio.gather(*run_it)
    return time.time() - start
