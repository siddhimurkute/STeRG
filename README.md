# STeRG
# Multithreading in Python
Website: https://www.geeksforgeeks.org/multithreading-python-set-1/
Ability of a processor to execute multiple threads concurrently (at the same time).

Process- is an instance of a computer program that is being executed.
3 basic components:

1.An executable program.
2.The associated data needed by the program (variables, work space, buffers, etc.)
3.The execution context of the program (State of process)

Thread- is an entity within a process that can be scheduled for execution.
Smallest unit of processing that can be performed in an OS.
A thread is a sequence of such instructions within a program that can be executed independently of other code.

A thread contains all this information in a Thread Control Block (TCB):

Thread Identifier: Unique id (TID) is assigned to every new thread
Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
Program counter: a register which stores the address of the instruction currently being executed by thread.
Thread state: can be running, ready, waiting, start or done.
Thread’s register set: registers assigned to thread for computations.
Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.

Process control block <------ Thread control block --------> Process memory (stack/data)

Multi-threading: Multiple threads can exist within one process where:

1.Each thread contains its own register set and local variables (stored in stack).
2.All threads of a process share global variables (stored in heap) and the program code.

Context Switching:
1.In a simple, single-core CPU, Multithreading is achieved using frequent switching between threads. This is termed as context switching.
2.The state of a thread is saved and state of another thread is loaded whenever any interrupt (due to I/O or manually set) takes place. 
3.Context switching takes place so frequently that all the threads appear to be running parallelly (this is termed as multitasking).


API stands for Application Programming Interface.
An API, or application programming interface, is a set of defined rules that enable different applications to communicate with each other.

In Python, the threading module provides a very simple and intuitive API for spawning multiple threads in a program.


# Python program to illustrate the concept of threading
# importing the threading module
import threading


def print_cube(num):
	# function to print cube of given num
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))


if _name_ =="_main_":
	# creating thread
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()

	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed
	print("Done!")


#Once the threads start, the current program (you can think of it like a main thread) also keeps on executing. 
#In order to stop execution of current program until a thread is complete, we use join method.


# Python program to illustrate the concept
# of threading
import threading
import os

def task1():
	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 1: {}".format(os.getpid()))

def task2():
	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 2: {}".format(os.getpid()))

if _name_ == "_main_":

	# print ID of current process
	print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
	print("Main thread name: {}".format(threading.current_thread().name))

	# creating threads
	t1 = threading.Thread(target=task1, name='t1')
	t2 = threading.Thread(target=task2, name='t2')

	# starting threads
	t1.start()
	t2.start()

	# wait until all threads finish
	t1.join()
	t2.join()


Using a thread pool:
A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks. 

concurrent.futures module- provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool. 

Note: It’s important to be careful when working with threads to avoid issues such as race conditions and deadlocks.
When two processes are waiting for each other directly or indirectly, it is called deadlock. 
A race condition occurs when two threads use the same variable at a given time.
This situation will stop both threads from processing or executing the functions.

import concurrent.futures

def worker():
	print("Worker thread running")

# create a thread pool with 2 threads
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# submit tasks to the pool
pool.submit(worker)
pool.submit(worker)

# wait for all tasks to complete
pool.shutdown(wait=True)

print("Main thread continuing to run")
