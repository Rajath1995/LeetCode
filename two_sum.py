class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if (len(nums) > 2):
            i = 0
            while i < len(nums):
                for j in range(i+1, len(nums)):
                    if (nums[i] + nums[j] == target):
                        return [i, j]
                    else:
                        continue
                i+=1
                        
        elif (len(nums) < 3):
            if (nums[0] + nums[1] == target):
                return [0,1]
        
        elif (len(nums) == 1):
            if (nums[0] == target):
                return [0]
        else:
            return []
