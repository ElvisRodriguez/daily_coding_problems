'''
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
'''


class BitArray(object):
    def __init__(self, size):
        self.size = size
        self.array = [0 for i in range(size)]

    def set(self, i, val):
        if i >= self.size or val not in [0, 1]:
            return 'error'
        else:
            self.array[i] = val

    def get(self, i):
        if i >= self.size:
            return 'error'
        else:
            return self.array[i]


if __name__ == '__main__':
    barr = BitArray(16)
    barr.set(2, 1)
    barr.set(5, 0)
    print(barr.array)
