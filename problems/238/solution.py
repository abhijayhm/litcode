from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total = 1
        zero_case = False
        zeroes_count = 0
        
        # First loop: calculate inverse and total product
        for value in nums:
            if value != 0:
                output.append(value ** -1)
                total = total * value
            else:
                # if any one zero, others are 0 and only zero indices are non zero
                output.append(value)
                zero_case = True
                zeroes_count = zeroes_count + 1
        
        # if more than one zero, everything will be zero lol
        if zeroes_count > 1:
            return [0] * len(nums)

        # Second loop: compute final output values
        for i in range(len(nums)):
            if not zero_case:
                output[i] = int(output[i] * total)
            else:
                if output[i] == 0:
                    output[i] = int(total)
                else:
                    output[i] = 0
        
        return output
