'''
This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary
 representation.
For example, 21 (10101) is sparse, but 22 (10110) is not.

For a given input N, find the smallest sparse number greater than or equal to N.
Do this in faster than O(N log N) time.
'''


def check_sparsity(n, memo):
    if n in [0, 1]:
        memo[n] = True
        return True
    if n in memo:
        return memo[n]
    last_bit = None
    while n > 0:
        bit = n % 2
        if last_bit is None:
            last_bit = bit
        else:
            if last_bit == 1 and bit == 1:
                memo[n] = False
                return False
            last_bit = bit
        n //= 2
        if n in memo:
            return memo[n]
    memo[n] = True
    return True


def find_next_sparse_number(n):
    memo = {}
    while not check_sparsity(n, memo):
        n += 1
    return n


if __name__ == '__main__':
    #print(check_sparsity(21), check_sparsity(22), sep='\n')
    memo = {}
    for i in range(100):
        print(f'{i}:', check_sparsity(i, memo))
    print(memo)
