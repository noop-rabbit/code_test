import threading
import time


class Worker():
    def __init__(self, name):
        self.name = name

    def report(self, status):
        print(f"{self.name} is {status}...")

    def do_task(self):
        pass

class Cleaner(Worker):

    def do_task(self):
        self.report("Cleaning")
        time.sleep(5)
        self.report("Cleaning completed")


class Packer(Worker):

    def do_task(self):
        self.report("Packing")
        time.sleep(3)
        self.report("Packing completed")

def main():

    print("Starting main function...")

    cleaner = Cleaner("Cleaner1")
    packer = Packer("Packer1")

    cleaner_th = threading.Thread(target=cleaner.do_task)
    packer_th = threading.Thread(target=packer.do_task)

    cleaner_th.start()
    packer_th.start()

    cleaner_th.join()
    packer_th.join()
    
    print("All tasks completed.")

if __name__ == "__main__":
    main()