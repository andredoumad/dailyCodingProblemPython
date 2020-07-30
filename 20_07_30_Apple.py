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