import httpx
import time
import asyncio
from typing import Callable, Coroutine

addr = "https://langa.pl/crawl/"
todo = set()


async def progress(
        url: str,
        algo: Callable[..., Coroutine],
) -> None:
    task = asyncio.create_task(
        algo(url),
        name=url,
    )
    todo.add(task)
    start = time.time()
    while len(todo):
        done, pending = await asyncio.wait(todo, timeout=0.5)
        todo.difference_update(done)
        urls = (t.get_name() for t in todo)
        print(f"{len(todo)}:" + ", ".join(sorted(urls))[-120:])

    end = time.time()
    print(f"Took {format(end - start, '.2f')} seconds")


async def crawl(
        prefix: str,
        url: str = ""
) -> None:
    url = url or prefix
    client = httpx.AsyncClient()
    try:
        res = await client.get(url)
    finally:
        await client.aclose()

    for line in res.text.splitlines():
        if line.startswith(prefix):
            task = asyncio.create_task(
                crawl(prefix, line),
                name=line
            )
            todo.add(task)


asyncio.run(progress(addr, crawl))
