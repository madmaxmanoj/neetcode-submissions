class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxis = []
        n =  len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                maxis.append(i)
       
        if len(maxis) == 1:
            return max(maxis[0],n - maxis[0] - 1)
        
        if len(maxis) > 1:
            fmax = []
            for j in range(len(maxis) - 1):
                fmax.append((maxis[j+1] - maxis[j]) - 1)
            s = max(fmax)
            return max(maxis[0],s,n - maxis[-1] - 1)
                        
        return n
        
            
                 
        