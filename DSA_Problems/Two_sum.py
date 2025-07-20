#brute_force approach
def twosum(nums,target): #nums is the list of numbers
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

# hash map approach

def twoSum (nums, target ):
    num_map={}
    for i,num in enumerate(nums):
        comp= target - num
        if comp in num_map:
            return [num_map[comp],i]
        num_map[num]=i
