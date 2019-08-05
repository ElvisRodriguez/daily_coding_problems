'''
This problem was asked by Uber.

Implement a 2D iterator class.
It will be initialized with an array of arrays,
 and should implement the following methods:

next(): returns the next element in the array of arrays.
If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]],
 calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays.
Some of the arrays can be empty.
'''


class Iterator2D:
    def __init__(self, array):
        self.array = array
        self.current_element = None
        self.row = 0
        self.col = 0

    def next(self):
        try:
            while True:
                if self.array[self.row]:
                    self.current_element = self.array[self.row][self.col]
                    self.col += 1
                    if len(self.array[self.row]) == self.col:
                        self.row += 1
                        self.col = 0
                    break
                else:
                    self.row += 1
        except IndexError:
            raise IndexError
        return self.current_element

    def has_next(self):
        row = self.row
        col = self.col
        element = None
        try:
            element = self.next()
        except IndexError:
            return False
        self.row = row
        self.col = col
        if element is None:
            return False
        return True


if __name__ == '__main__':
    array = [[1, 2], [3], [], [4, 5, 6]]
    obj = Iterator2D(array)
    while(obj.has_next()):
        print(obj.next())
