'''
A Collatz sequence in mathematics can be defined as follows.
Starting with any positive integer:
- if n is even, the next number in the sequence is n / 2
- if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1.
Test this conjecture.
Bonus: What input n <= 1000000 gives the longest sequence?
'''


def collatz(n, sequence_size, memo={}):
    if n in memo:
        return memo[n] + sequence_size
    if n == 1:
        return sequence_size + 1
    if n % 2 == 0:
        return collatz(n // 2, sequence_size + 1, memo)
    else:
        return collatz(3 * n + 1, sequence_size + 1, memo)


def longest_collatz_sequence(n=1000000):
    integer = 0
    longest_sequence = 0
    memo = {}
    for i in range(1, n+1):
        sequence_size = 0
        sequence_size = collatz(i, sequence_size, memo)
        memo[i] = sequence_size
        if sequence_size > longest_sequence:
            longest_sequence = sequence_size
            integer = i
    return integer


if __name__ == '__main__':
    print(longest_collatz_sequence())
