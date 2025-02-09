class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            
            if (bit_a | bit_b) != bit_c:
                if bit_c == 1:
                    count += 1  # Need at least one of a or b to be 1
                else:
                    count += bit_a + bit_b  # Flip both if both are 1
                    
            a, b, c = a >> 1, b >> 1, c >> 1  # Shift to check next bit
            
        return count
