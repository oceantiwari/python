import time

def timer(fn):
  def wrapper(*args,**kwargs):
    start = time.time()
    result = fn(*args,**kwargs)
    end = time.time()
    print(f"{fn.__name__} ran in {end-start}")
    return result
  return wrapper

@timer
def example_1(n):
  time.sleep(n)
example_1(3)