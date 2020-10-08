import pandas as pd
import time
import numpy as np

from bruteforce import Bruteforce
from sieve_of_eratosthenes import SieveOfEratosthenes


start_time = time.time()
for i in SieveOfEratosthenes(3000):
    print(i, end=", ")
print("\n\nExecuted in", round(time.time() - start_time, 4), "seconds")


start_time = time.time()
for i in Bruteforce(3000):
    print(i, end=", ")
print("\nExecuted in", round(time.time() - start_time, 4), "seconds")


result1 = []
result2 = []
index = [round(100**i) for i in np.arange(1, 2.1, 0.02)]
for n in index:
    start_time = time.time()
    for i in Bruteforce(n):
        pass
    result1.append(time.time() - start_time)
    
    start_time = time.time()
    for i in SieveOfEratosthenes(n):
        pass
    result2.append(time.time() - start_time)


df = pd.DataFrame(list(zip(result1, result2)), index=index, columns =['Brute-force', 'Sieve Of Eratosthenes']) 


df


df.plot(kind='bar', logy=True, xlabel="Max number", ylabel="Time in seconds", figsize=(20,10))


df.plot(xlabel="Max number", ylabel="Time in seconds", figsize=(20,10))
