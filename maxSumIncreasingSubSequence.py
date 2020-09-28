'''Given an array of n positive integers. Write a program to find the sum of maximum
sum subsequence of the given array such that the integers in the subsequence are sorted in increasing order.
For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}
, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10'''

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
