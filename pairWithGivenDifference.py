'''Given an unsorted array and a number n, find if there exists a pair of elements in the array whose difference is n.'''
def pair(arr, n, difference):
    arr.sort()
    i, j = 0, 1
    while i < n and j < n:
        if arr[j] - arr[i] == difference:
            print('pair : {0} {1}'.format(arr[i], arr[j]))
            return 1
        elif arr[j] - arr[i] > difference:
            i += 1
        elif arr[j] - arr[i] < difference:
            j += 1
    print('no pair found')


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    difference = int(input())
    n = len(arr)
    pair(arr, n, difference)
