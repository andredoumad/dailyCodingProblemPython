# Andre Doumad
'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function 
f and an integer n, and calls f after n milliseconds.
'''

import threading, time

# thread class
class jobTrigger(threading.Thread):
    def __init__(self, **kwargs):
        self.owner = kwargs['owner']
        self.t_id = kwargs['t_id']
        self.timeout = kwargs['timeout']
        self.function = kwargs['function']
        self.owner.append_thread_id(self.t_id)
        self.activate()
        threading.Thread.__init__(self)

    def activate(self):
        time.sleep(self.timeout)
        self.function()
        self.owner.remove_thread(self.t_id)

# delayed function
def justTryinToFunction():
    print('-----------------')
    print('yes, I am...')
    print('-----------------')

class Solution(object):
    def __init__(self):
        self.threads = []
        self.myLock = threading.Lock()


    def append_thread_id(self, t_id):
        self.log('appending new thread id ' + str(t_id)  + ' to threads ')
        self.threads.append(t_id)
        self.log(str(self.threads))

    def remove_thread(self, t_id):
        self.log('removing thread id ' + str(t_id) + ' from threads ')
        for i in range(0, len(self.threads)):
            if self.threads[i] == t_id:
                self.threads.pop(i)

    def log(self, msg):
        self.myLock.acquire(True)
        print(str(msg))
        self.myLock.release()

    def solve(self, n, f):
        n = n / 1000
        self.log('n = ' + str(n) + ' seconds')
        startTime = time.time()
        thread = threading.Thread(target=jobTrigger, daemon=True, kwargs={
                't_id' : 1, 
                'timeout' : n, 
                'function' : f, 
                'owner' : self 
            })
        thread.start()
        time.sleep(n/100)
        while len(self.threads) > 0:
            self.log('self.threads ' + str(self.threads))
            time.sleep(n/10)
            self.log('waiting for schedule to execute. ' + str(time.time() - startTime))
        self.log(' all done :)')

if __name__ == '__main__':
    solution = Solution()
    solution.solve(10000, justTryinToFunction)

'''
OUTPUT:

n = 10.0 seconds
appending new thread id 1 to threads 
[1]
self.threads [1]
waiting for schedule to execute. 1.1014673709869385
self.threads [1]
waiting for schedule to execute. 2.1025757789611816
self.threads [1]
waiting for schedule to execute. 3.103795051574707
self.threads [1]
waiting for schedule to execute. 4.104191541671753
self.threads [1]
waiting for schedule to execute. 5.105414152145386
self.threads [1]
waiting for schedule to execute. 6.106584548950195
self.threads [1]
waiting for schedule to execute. 7.1080193519592285
self.threads [1]
waiting for schedule to execute. 8.109217405319214
self.threads [1]
waiting for schedule to execute. 9.110430479049683
self.threads [1]
-----------------
yes, I am...
-----------------
removing thread id 1 from threads 
waiting for schedule to execute. 10.111694574356079
 all done :)

'''


'''
Solution
We can implement the job scheduler in many different ways, so don't worry if your solution is different from ours. Here is just one way:

First, let's try the most straightforward solution. That would probably be to spin off a new thread on each function we want to delay, sleep the requested amount, and then run the function. It might look something like this:

import threading
from time import sleep

class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call(n):
            sleep(n / 1000)
            f()
        t = threading.Thread(target=sleep_then_call)
        t.start()

While this works, there is a huge problem with this method: we spin off a new thread each time we call delay! That means the number of threads we use could easily explode. We can get around this by having only one dedicated thread to call the functions, and storing the functions we need to call in some data structure. In this case, we use a list. We also have to do some sort of polling now to check when to run a function. We can store each function along with a unix epoch timestamp that tells it when it should run by. Then we'll poll some designated tick amount and check the list for any jobs that are due to be run, run them, and then remove them from the list.

from time import sleep
import threading

class Scheduler:
    def __init__(self):
        self.fns = [] # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time() * 1000 + n))
We'll stop here, but you can go much farther with this. Some extra credit work:

Extend the scheduler to allow calling delayed functions with variables
Use a heap instead of a list to keep track of the next job to run more efficiently
Use a condition variable instead of polling (it just polls lower in the stack)
Use a threadpool or other mechanism to decrease the chance of starvation (one thread not being able to run because of another running thread)
'''