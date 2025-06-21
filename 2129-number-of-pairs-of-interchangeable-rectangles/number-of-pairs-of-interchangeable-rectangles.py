from collections import defaultdict
from fractions import Fraction

class Solution:
    def interchangeableRectangles(self, rectangles):
        ratio_count = defaultdict(int)
        
        for width, height in rectangles:
            ratio = Fraction(width, height)  # Avoid float precision issues
            ratio_count[ratio] += 1

        result = 0
        for count in ratio_count.values():
            if count >= 2:
                result += count * (count - 1) // 2  # nC2
        
        return result
