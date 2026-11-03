class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i, num in enumerate(nums):
            compl = target -num

            if compl in Map:
                return [Map[compl],i]
            
            Map[num] = i
        return []