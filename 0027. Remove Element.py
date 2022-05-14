class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for j in range(len(nums)):            
            if nums[j] !=val:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1            
        return i  
      
#Time complexity: O(n)
#Space complexity:O(1)
