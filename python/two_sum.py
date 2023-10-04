nums = [3,3]
target = 6

for index_1 in range(len(nums)):
    for index_2 in range(len(nums)):
        if index_1 != index_2:
            if nums[index_1] + nums[index_2] == target:
                print(index_1)
                print(index_2)
            
            
    
    
