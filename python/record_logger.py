'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log.
    i is guaranteed to be smaller than or equal to N.
    You should be as efficient with time and space as possible.
'''

import collections


class RecordLogger:
    def __init__(self, max_size=100):
        self.records = collections.deque(maxlen=max_size)

    def record(self, order_id):
        self.records.appendleft(order_id)

    def get_last(self, i):
        return self.records[i]


if __name__ == '__main__':
    r_log = RecordLogger(max_size=10)
    r_log.record('24423')
    r_log.record('25523')
    r_log.record('24413')
    r_log.record('33423')
    print(r_log.get_last(2))
