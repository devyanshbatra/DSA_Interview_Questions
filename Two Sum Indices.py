def two_sum(nums, target):
    num_dict = {}
    
    for i, num in enumerate(nums):
        if (complement := target - num) in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    
    return None