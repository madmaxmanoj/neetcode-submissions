class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final = []
        i = 0
        while i < 2:
            for num in nums:
                final.append(num)
            i += 1
        return final

        