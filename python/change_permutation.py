'''
This problem was asked by Twitter.

A permutation can be specified by an array P,
 where P[i] represents the location of the element at i in the permutation.
For example, [2, 1, 0]
 represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array.
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0],
 return ["c", "b", "a"].
'''

# Runtime: O(n) where n is the size of the array
# Space Complexity: O(n) where n is the size of the array


def change_array_permutation(array, permutation):
    result = []
    for index in permutation:
        result.append(array[index])
    return result


# Runtime: O(n) where n is the size of the array
# Space Complexity: O(n) where n is the size of the array
def change_array_permutation_in_place(array, permutation):
    swaps = set()
    for i in range(len(array)):
        if i != permutation[i]:
            swap = tuple(sorted([i, permutation[i]]))
            if swap not in swaps:
                swaps.add(swap)
    for swap in swaps:
        i, j = swap
        array[i], array[j] = array[j], array[i]


# Runtime: O(n) where n is the size of the array
# Space Complexity: O(1) no extra space needed
def change_array_permutation_in_constant_space(array, permutation):
    for i in range(len(array)):
        if i != permutation[i]:
            j = permutation[i]
            array[i], array[j] = array[j], array[i]
            permutation[i], permutation[j] = permutation[j], permutation[i]


if __name__ == '__main__':
    array = ['a', 'b', 'c']
    permutation = [2, 1, 0]
    print(change_array_permutation(array, permutation))
    change_array_permutation_in_place(array, permutation)
    print(array)
    array = ['a', 'b', 'c']
    change_array_permutation_in_constant_space(array, permutation)
    print(array)
