'''
This problem was asked by Google.

You are given an array of nonnegative integers.
You start at the beginning of the array and are trying to advance to the end.
You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.

For example:
Given the array [1, 3, 1, 2, 0, 1],
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
'''

import collections


def can_reach_the_end(array):
    '''Determine if by using the array node values as steps, we can 'walk' to
       the end of the array.
    '''
    # Grab the first max step count.
    steps = array[0]
    paths = collections.deque()
    # No need to explore the same path twice, we'll only check new paths.
    # visited is a set so we can check membership in O(1) time.
    visited = set()
    # For every step we can take, we create a path of the rest of the array.
    for i in range(steps):
        # Each path is what's left of the array to explore.
        path = array[i+1:]
        # It's possible for the initially generated paths to lead to the end.
        if path is None:
            return True
        # Make path a hashable type so that we may add it to visited.
        hash_path = tuple(path)
        # Add a path if it has not yet been explored.
        if hash_path not in visited:
            # Add all unique paths that we can explore.
            paths.append(path)
            visited.add(hash_path)
    # We keep generating all possible paths we can explore.
    # We'll use a breadth-first search approach to exploring paths.
    while paths:
        # We treat paths as a queue, grabbing the first path on 'line.'
        path = paths.popleft()
        # If the path we grab is empty or there's one node left, we have reached
        #   the end of the array.
        # There are two checks for True to avoid throwing an IndexError.
        if not path or len(path) == 1:
            return True
        steps = path[0]
        # If we have more steps available than array nodes,
        #   we have found a path that leads to the end of the array.
        if steps >= len(path):
            return True
        # Just like during setup, we generate all paths, and add them to paths
        #   if we haven't already explored/generated them.
        for i in range(steps):
            new_path = path[i+1:]
            hash_path = tuple(new_path)
            if hash_path not in visited:
                paths.append(new_path)
                visited.add(hash_path)
    # If the while loop exits, there exists no paths to the end of the array.
    return False
