def beautifulDays(i, j, k):
    count = 0
    for x in range(i, j + 1):
        rx = int(str(x)[::-1])
        if abs(x - rx) % k == 0:
            count += 1
    print(count)
    return count


if __name__ == '__main__':
    beautifulDays(1, 2, 4)
