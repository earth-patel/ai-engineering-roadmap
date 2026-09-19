import asyncio

async def task1():
  print("Task 1 started")
  await asyncio.sleep(2)
  print("Task 1 finished")

async def task2():
  print("Task 2 started")
  await asyncio.sleep(1)
  print("Task 2 finished")

async def main():
  await asyncio.gather(
    task1(),
    task2(),
  )  # This will run both tasks concurrently, allowing them to execute in parallel.
  # await task1()
  # await task2()

asyncio.run(main())