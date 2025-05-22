def longestarray(arr,k):
    n=len(arr)
    for i in range(n):
        s=0
        for j in range(1,n):
            s+=arr[k]
    if s==k:
        length=max(length,(j-i+1))
    return length

if __name__ == '__main__':
    a = [2, 3, 5, 1, 9]
    k = 10
    len = getLongestSubarray(arr, k)
    print("The length of the longest subarray is:", len)
