import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

app = FastAPI()

fifo_queue = asyncio.Queue()


async def worker():
    while True:
        print(f"Got a job: (size of remaining queue: {fifo_queue.qsize()})")
        job = await fifo_queue.get()
        await job()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    # Line of code below is for running asyncio queue worker
    asyncio.create_task(worker())
    yield
    # shutdown
    pass


async def long_running_process():
    print("in a long running task")
    await asyncio.sleep(10)
    print("done with long running task")


@app.post("/process")
async def asyncio_queue():
    """
    Using standard asycio queue for long running process
    """
    print("Queueing a job")
    await fifo_queue.put(long_running_process)
    return {"result": "success"}
