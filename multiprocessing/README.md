# Python `multiproceesing`
This is, in my opinion, the most straightforward way to multiprocess. It obviously has some limitations, but is absolutely perfect for plenty of programs where we simply want to use multiprocessing to speed up calculations that can be done simultaneously.

Examples of such processes include (but are not limited to):
- Multiple iterations of a calculation
    - e.g. you need 10 runs to get a mean and average. Instead of running all 10 in series, just run all 10 at once
- Calculating multiple unrelated correlation functions
    - e.g. xi, omega, and eta correlations. Normally, we'd calculate one,then the next, etc. But you can use 3 cores and run all three at once

Basically, any time you need to run multiple lines of code before proceeding to the next step, and those lines don't rely on each other, multiprocessing can help.

An example script is given to illustrate the usage and how it functionally differs from the looped version: `multiprocessing_test.py`

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
Now that we actually have the cores ready to run stuff in parallel, let's use it. There are a bunch of ways to do this, but I will focus on `map` and `starmap`. Both have an async version (`map_async` and `starmap_async`), but for our purposes, this won't do much. If you're curious about the benefits, you can look them up, but in terms of computational speedup, there's really no extra benefit for us.

### Using `map`
When your function only takes a single argument.</br>
```
def test_function(arg):
    # Some code
    return arg

args = [1,2,3,4,5,6]

with multiprocessing.Pool(processes=3) as p:
    results = p.map( test_function, args )
```

Here, `args` is an iterable where each element is a single value. the function `test_function` is called for each value, passing each call to the next available process.

### Using `starmap`
Whe your function has multiple arguments.</br>
```
def test_function(arg1, arg2, arg3):
    # Some code
    return arg1 + arg2 + arg3

args = [
    (1,2,3),
    (4,5,6),
    (7,8,9),
    (10,11,12),
    (13,14,15),
    (16,17,18)
]

with multiprocessing.Pool(processes=3) as p:
    results = p.starmap( test_function, args )
```

Here, `args` is an iterable where each iterable is a tuple (or some iterable). Each of those tuples contains all the arguments to be passed into a single call. It functions essentially the same as `map`, except the function being parallelized expects multiple arguments, and each tuple in `args` here will be unpacked and passed.

## Accessing results
In the examples above, we store the results in `results`. The nice thing about these methods is that they preserve the order. This means that if we did these in order using a loop, storing results sequentially, we would get the same order! So we don't need to worry that some processes finishing faster than others will mess up the order of results.

Sometimes order won't matter (e.g. when we just need 10 iterations to get a mean and standard deviation). But in cases where we want the n<sup>th</sup> result to match the n<sup>th</sup>  input, we're covered.