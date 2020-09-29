def zigzagarray(arr):
    i = 0
    j = 1
    n = len(arr)
    while i < n and j < n:
        if i % 2 == 0 and arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        elif i % 2 != 0 and arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

        i += 1
        j += 1
    print(arr)


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    zigzagarray(arr)