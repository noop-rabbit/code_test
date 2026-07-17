import asyncio

class Worker():
    def __init__(self, name):
        self.name = name

    def report(self, status):
        print(f"{self.name} is {status}...")

    async def do_task(self):
        print("Passing")
        #pass

class Cleaner(Worker):

    async def do_task(self):
        self.report("Cleaning")
        await asyncio.sleep(5)
        self.report("Cleaning completed")

class Packer(Worker):

    async def do_task(self):
        self.report("Packing")
        await asyncio.sleep(3)
        self.report("Packing completed")
    #pass

async def main():

    print("Starting main function...")

    cleaner = Cleaner("Cleaner1")
    packer = Packer("Packer1")

    tasks = [
        cleaner.do_task(),
        packer.do_task(),
    ]

    await asyncio.gather(*tasks)

    print("All tasks completed.")

if __name__ == "__main__":
    asyncio.run(main())