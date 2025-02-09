class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_to_indices = {}
        for i, num in enumerate(nums):
            values_to_indices[num] = i
        
        for i, num in enumerate(nums):
            difference = target - num
            j = values_to_indices.get(difference)
            if j is not None and j != i:
                return [values_to_indices.get(difference), i]
        # no solution found lol
        return []