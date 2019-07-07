'''
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): 
 returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?
'''


class HitCounter(object):
    def __init__(self):
        self.hit_total = 0
        self.timestamps = []

    def record(self, timestamp):
        self.hit_total += 1
        self.timestamps.append(timestamp)

    def total(self):
        return self.hit_total

    def range(self, lower, uppper):
        hits = 0
        for timestamp in self.timestamps:
            if lower <= timestamp <= upper:
                hits += 1
        return hits
