import heapq

def kth_largest(arr, k):
    max_heap = [-num for num in arr]  
    heapq.heapify(max_heap) 

    for _ in range(k):  
        kth_largest = -heapq.heappop(max_heap)  

    return kth_largest

arr = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(arr, k)) 
