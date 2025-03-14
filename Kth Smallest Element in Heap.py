import heapq

def kth_smallest(arr, k):
    heapq.heapify(arr)  
    for _ in range(k - 1):  
        heapq.heappop(arr)

    return heapq.heappop(arr)  

arr = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_smallest(arr, k)) 
