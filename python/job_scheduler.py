'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and
calls f after n milliseconds.
'''

import time


def func():
    print('Test Function')


def job_scheduler(f, n):
    time.sleep(n // 10)
    f()


if __name__ == '__main__':
    job_scheduler(func, 3)
