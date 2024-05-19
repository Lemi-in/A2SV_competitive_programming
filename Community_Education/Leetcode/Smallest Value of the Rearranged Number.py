class Solution(object):
    def smallestNumber(self, num):
        if num == 0:
            return 0
        
        isNegative = num < 0
        digits = sorted([char for char in str(abs(num))])
        
        if isNegative:
            return -int(''.join(digits[::-1]))
        else:
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], '0'
                        break
            return int(''.join(digits))
