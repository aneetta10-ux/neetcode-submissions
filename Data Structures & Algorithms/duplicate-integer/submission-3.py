class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i=i+1
            else:
                return True
        
        return False
        