


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


import time

p = ThreadPoolExecutor(10)

def run(i):

    time.sleep(1)
    print(i)

for i in range(100):

    p.submit(run, i)





