import heapq

def mergeKSortedArrays(arr):
    k = len(arr)  
    min_heap = []
    result = []
    
    for i in range(k):
        heapq.heappush(min_heap, (arr[i][0], i, 0)) 
    
    while min_heap:
        val, row, col = heapq.heappop(min_heap)
        result.append(val) 
        if col + 1 < len(arr[row]):
            heapq.heappush(min_heap, (arr[row][col + 1], row, col + 1))
    
    return result

arr = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11]
]

print(mergeKSortedArrays(arr))

