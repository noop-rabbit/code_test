import time
import threading

def slow_square(n):
  time.sleep(n)
  return n * n

def run_in_thread(func, args_list: list) -> list:
  threads = []
  results = [None] * len(args_list)

  def worker(i, value):
    results[i] = func(value)

  for i, value in enumerate(args_list):
    thread = threading.Thread(target=worker, args=(i, value))
    threads.append(thread)
    thread.start()
  for thread in threads:
    thread.join()
  return results



results = run_in_thread(slow_square, [5, 2, 3])
print(results)