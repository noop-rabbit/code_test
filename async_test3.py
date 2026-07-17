import asyncio

class Cleaner:
    def __init__(self, name):
        self.name = name

    def report(self, status):
        print(f"{self.name} is {status}...")

    async def do_task(self):
        self.report("Cleaning")
        await asyncio.sleep(10)
        self.report("Cleaning completed")

async def main():
    print("starting main")

    cleaner = Cleaner("Cleaner1")
    task = asyncio.create_task(cleaner.do_task())
    await asyncio.sleep(0)

    for i in range(4):
        print("Still cleaning...")
        await asyncio.sleep(1)

    await task

    print("Done")

if __name__ == "__main__":
    asyncio.run(main())

