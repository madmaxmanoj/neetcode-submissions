class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        i = 0
        ans = []
        while i < 2:
            for _ in nums:
                ans.append(_) 
            i += 1
        return ans
        