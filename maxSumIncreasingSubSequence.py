def increasingSubSequence(arr, n):
    maxSum = arr[0]
    sum = arr[0]
    for i in range(1, n):
        if arr[i-1] < arr[i] or sum == 0:
            sum += arr[i]
            print(sum)
        else:
            sum = arr[i]
            print(sum)
        if maxSum < sum:
            maxSum = sum
            print(maxSum)
    print(maxSum)


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    n = len(arr)
    increasingSubSequence(arr,n)
