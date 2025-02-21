class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # Shift result left and add the last bit of n
            n >>= 1  # Shift n right to process the next bit
          
        return result  # Fixed indentation
