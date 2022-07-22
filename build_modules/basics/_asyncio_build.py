import asyncio
"""
using this module we can write an concurrency code.
using this module we can run the next line code without complete the execution of the running line execution
"""


async def main():
    print("It's working..")
    await asyncio.sleep(5)
    print("oh!!")
    return print("done.")


async def phone():
    print("it's mobile..")
    await asyncio.sleep(6)
    print("completed 2 sec..")


async def main1():
    task1 = asyncio.create_task(main())
    task2 = asyncio.create_task(phone())
    value = await task1
    value
asyncio.run(main1())