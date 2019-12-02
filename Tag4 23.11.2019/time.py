import time
start=time.perf_counter()
def c_time():
    start=time.perf_counter()
    time.perf_counter()
    stop=time.perf_counter()
    print(f"{stop-start}")
print(c_time())
