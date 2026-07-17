import threading, time



class DownloaderClass():
    def __init__(self, filename):
        self.filename = filename

    def DownloadFile(self):
        print(f"Downloading {self.filename}...")
        time.sleep(5)
        print(f"{self.filename} download has completed.")

class Logger:                                                 # I access downloader1.filename from another class, if reqd.
    def log_status(self, downloader):
        print(downloader.filename)

def main():
    print("starting main download function...")
    downloader1 = DownloaderClass("File1.txt")
    downloader2 = DownloaderClass("File2.txt")
    downloader3 = DownloaderClass("File3.txt")
    th1 = threading.Thread(target=downloader1.DownloadFile)
    th2 = threading.Thread(target=downloader2.DownloadFile)
    th3 = threading.Thread(target=downloader3.DownloadFile)
    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()
    print("Main download function has completed.")
if __name__ == "__main__":
    main()
'''

def DownloadFile(filename):
    print(f"Downloading {filename}...")
    time.sleep(5)
    print(f"{filename} download has completed.")
    return 0

def main():
    print("starting main download function...")
    th1 = threading.Thread(target=DownloadFile, args=("File1.txt",))
    th2 = threading.Thread(target=DownloadFile, args=("File2.txt",))
    th3 = threading.Thread(target=DownloadFile, args=("File3.txt",))
    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()
    print("Main download function has completed.")
'''

if __name__ == "__main__":
    main()