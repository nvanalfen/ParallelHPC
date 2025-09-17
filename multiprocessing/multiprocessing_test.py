import multiprocessing
import time
import numpy as np

def fake_single_arg_func(t):
    time.sleep(t)
    return t

def fake_multi_arg_func(t, x):
    time.sleep(t)
    return t + x

##### Map #########################################################################################
print("\n>>>>>Testing map<<<<<\n")
wait_times = [2,2,0.2,0.1,1,0.5,0.1,1]

# Run standard in loop
print("Looping...")
start = time.time()
results = []
for t in wait_times:
    results.append(fake_single_arg_func(t))
end = time.time()
print("Loop results:")
print(f"Results: {results}")
print(f"Total time taken: {end - start:.2f} seconds\n")

# Run using multiprocessing Pool map
print("Using multiprocessing Pool map...")
start = time.time()
with multiprocessing.Pool(4) as p:
    results = p.map(fake_single_arg_func, wait_times)
end = time.time()
print("Map results:")
print(f"Results: {results}")
print(f"Total time taken: {end - start:.2f} seconds\n")

##### starmap #####################################################################################
args = [(t, 2*t) for t in wait_times]               # Just to give a second argument for each call

print("\n>>>>>Testing Starmap<<<<<\n")

# Run standard in loop
print("Looping...")
results = []
start = time.time()
for t, x in args:
    results.append(fake_multi_arg_func(t, x))
end = time.time()
print("Loop results:")
print(f"Results: {results}")
print(f"Total time taken: {end - start:.2f} seconds\n")

start = time.time()
with multiprocessing.Pool(4) as p:
    results = p.starmap(fake_multi_arg_func, args)
end = time.time()
print("Starmap results:")
print(f"Results: {results}")
print(f"Total time taken: {end - start:.2f} seconds")
