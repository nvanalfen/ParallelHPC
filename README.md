# Parallel Computing on Explorer HPC
Since our group's work can greatly benefit from parallelization, I've made some tutorials on how to do it on Explorer (and some work locally as well). Just requesting more cores won't speed things up. The code you're using has to explicitly use extra cores, otherwise they're sitting idle and we're using up allocation without getting benefits.

There are plenty of ways to parallelize, and some will be easier or more natural for different cases. I'll go through three different methods as best I can. I'll mention the different ways here briefly, then each will get a more in-depth discussion. I'm no expert and there's certainly more to each of these than I will go over, but it should be a good start.

## Multiple SLURM Jobs
The simplest way is to submit multiple jobs on SLURM. This doesn't even require any changes to your code (though if you're trying to use this method to tackle multiple parts of a single dataset, you will need to be clever in how you access). This is just running the same code on multiple computers at once. It can be very handy when the separate jobs don't need to talk to each other at all.

## Python multiprocessing
Python has a multiprocessing module that can take advantage of multiple cores. This is quite nice and can be a pretty easy way to have a single script use mutliple cores for parts of the code. Unlike multiple SLURM jobs, this is a single computer running a script (as opposed to multiple computers running different instances of the same code). This can be great if you have sections of the code that need to parallel process, but overall need the code to talk to itself.

## MPI
[MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) (Message Passing Interface). At its most basic, it can function similar to multiprocessing in that it can simply use separate cores on a single device. Unlike multiprocessing, MPI can scale to multiple machines (i.e. multiple nodes on the cluster) and can allow you to pass information back and forth. It can be quite a bit mor complicated to learn (if you're like me), but it lets you scale code to multiple machines and their resources (unlike multiprocessing) while maintining the ability to communicate between separate processes (unlike multiple SLURM jobs).