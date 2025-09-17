# Python `multiproceesing`
This is, in my opinion, the most straightforward way to multiprocess. It obviously has some limitations, but is absolutely perfect for plenty of programs where we simply want to use multiprocessing to speed up calculations that can be done simultaneously.

Examples of such processes include (but are not limited to):
- Multiple iterations of a calculation
    - e.g. you need 10 runs to get a mean and average. Instead of running all 10 in series, just run all 10 at once
- Calculating multiple unrelated correlation functions
    - e.g. xi, omega, and eta correlations. Normally, we'd calculate one,then the next, etc. But you can use 3 cores and run all three at once

Basically, any time you need to run multiple lines of code before proceeding to the next step, and those lines don't rely on each other, multiprocessing can help.

# multiprocessing Pool
A Pool of workers is how you manage multiple cores using multiprocessing. You create a pool accessing some number of cores (you can specify the number or specify all available CPUs). You can then use the pool to call functions in parallel. This isn't close to everything multiprocessing can do, but it's pretty much the only way I use it.

## Safely creating a Pool
When assigning cores as workers, you need to make sure you release them after you're done.
I recommend the following format:
```
processes = 3
with multiprocessing.Pool(processes=processes) as pool:
    # YOUR CODE HERE USING MAP, STARMAP, ETC.
```

The `with` statement handles all of the safe closing once you're finished. Without using `with`, you could run as follows:
```
processes = 3
pool = multiprocessing.Pool(processes=processes)
# YOUR CODE HERE USING MAP, STARMAP, ETC.
pool.close()
pool.join()
```

You get the same result, but if you forget to close and join, you can run into issues later. This is the same style as safely opening and closing a file using:
```
with open("file_name.txt") as f:
    # SOME CODE
```
instead of
```
f = open("file_name.txt")
# SOME CODE
f.close()
```

## Using Pool
Now that we actually have the cores ready to run stuff in parallel, let's use it.

### Using `map`

### Using `starmap`