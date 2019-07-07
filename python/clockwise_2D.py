def clockwise_visit(multi_arr, n, m):
    row = 0
    col = 0
    lower_bound = 0
    upper_bound = n - 1
    count = 0
    while count < n * m:
        while col < upper_bound:
            print(multi_arr[row][col])
            col += 1
        while row < upper_bound:
            print(multi_arr[row][col])
            row += 1
        while col > lower_bound:
            print(multi_arr[row][col])
            col -= 1
        while row > lower_bound:
            print(multi_arr[row][col])
            row -= 1
        upper_bound -= 1
        lower_bound += 1
        row += 1
        col += 1
        count += 1
        if n in [row, col]:
            break
    print(multi_arr[row][col])


if __name__ == '__main__':
    multi_arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    clockwise_visit(multi_arr, len(multi_arr), len(multi_arr[0]))
