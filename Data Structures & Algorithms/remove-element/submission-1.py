class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        n= len(nums)
        for num in nums:
            if num == val:
                count+=1
        i = 0        
        while i < count:
            nums.remove(val) 
            i+=1
        return n - count
        