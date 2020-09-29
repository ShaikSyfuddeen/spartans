def minDifferenceArray(arr, packets):
    arr.sort()
    i = 1
    j = packets
    n = len(arr)
    minDiff = arr[packets - 1] - arr[0]
    if packets > n:
        return 0
    while j < n:
        diff = arr[j] - arr[i]
        if diff < minDiff:
            minDiff = diff
        i += 1
        j += 1
    print('Minimum difference is {0}'.format(minDiff))
    

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    packets = int(input())
    minDifferenceArray(arr, packets)