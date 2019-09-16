'''
A Collatz sequence in mathematics can be defined as follows.
Starting with any positive integer:
- if n is even, the next number in the sequence is n / 2
- if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1.
Test this conjecture.
Bonus: What input n <= 1000000 gives the longest sequence?
'''


def collatz(n, sequence=[], memo={}):
    if n in memo:
        return memo[n]
    sequence.append(n)
    if n == 1:
        return sequence
    if n % 2 == 0:
        return collatz(n // 2, sequence, memo)
    else:
        return collatz(3 * n + 1, sequence, memo)


def longest_collatz_sequence(n=1000000):
    integer = 0
    longest_sequence = []
    memo = {}
    for i in range(1, n+1):
        sequence = []
        sequence = collatz(i, sequence, memo)
        memo[i] = sequence
        if len(sequence) > len(longest_sequence):
            longest_sequence == sequence
            integer = i
    return integer


if __name__ == '__main__':
    print(longest_collatz_sequence())
