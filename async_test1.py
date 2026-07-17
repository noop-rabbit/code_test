import asyncio, time

class DownloaderClass():
    def __init__(self, filename):
        self.filename = filename

    async def download_file(self):
        print(f"Starting download {self.filename}...")
        await asyncio.sleep(5)
        print(f"{self.filename} download finished...")


async def main():
    print("Starting main file download function...")

    tasks = [
        DownloaderClass("File1.txt").download_file(),
        DownloaderClass("File2.txt").download_file(),
        DownloaderClass("File3.txt").download_file(),
    ]

    results = await asyncio.gather(*tasks)

    print("Main file download function has completed.")

if __name__ == "__main__":
    asyncio.run(main())