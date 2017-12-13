# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x.bit_length() < 32:
            if x < 0:
                absInt = int(str(abs(x))[::-1])
                if absInt.bit_length() < 32:
                    return - (absInt)
                else:
                    return 0
            else:
                absInt = int(str(abs(x))[::-1])
                if absInt.bit_length() < 32:
                    return absInt
                else:
                    return 0
        else:
            return 0
