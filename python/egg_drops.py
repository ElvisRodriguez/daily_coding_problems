'''
This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k floors.
Your task is to find the lowest floor that will cause an egg to break,
 if dropped from that floor.
Once an egg breaks, it cannot be dropped again.
If an egg breaks when dropped from the xth floor,
 you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take,
 in the worst case, to identify this floor.

For example, if N = 1 and k = 5,
 we will need to try dropping the egg at every floor, beginning with the first,
 until we reach the fifth floor, so our solution will be 5.
'''


def max_trials(eggs, floors, trials=0, original_floors=0):
    '''
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    if eggs == 1:
        try:
            return trials + floors
        except TypeError:
            return trials + (floor[1] - floor[0] - 2)

    if floors in [0, 1]:
        return trials + 1
    if does_egg_break(test_floor):
        original_floors = floors
        return max_trials(eggs - 1, test_floor, trials + 1)
    else:
        return max_trials(eggs, (test_floor + floors), trials + 1)
