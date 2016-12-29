# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#
# The above arrows point to positions where the corresponding bits are different.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_binary = bin(x)[2:][::-1]
        y_binary = bin(y)[2:][::-1]
        print x_binary, y_binary
        i = 0
        mismatch = 1
        length = min(len(x_binary),len(y_binary))
        while i < len(min([x_binary,y_binary],key = len)):
            if x_binary[i]!=y_binary[i]:
                mismatch += 1
            i+=1
        mismatch += abs(len(x_binary)-len([y_binary]))
        return mismatch
x = Solution()
print x.hammingDistance(1,4)