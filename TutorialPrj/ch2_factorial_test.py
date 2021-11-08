import time
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
before_time = time.perf_counter()
for i in range(1, 10000):
    factorial(200)
after_time = time.perf_counter()
print(after_time - before_time)
