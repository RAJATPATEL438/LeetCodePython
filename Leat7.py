# Reverse Integer

class Solution:
    def reverse(self, x):
        INTEGER_MAX_VALUE = 2**31 - 1
        INTEGER_MIN_VALUE = -(2**31)
        reversed_num = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            # Check for overflow
            if (reversed_num > INTEGER_MAX_VALUE // 10 or
                (reversed_num == INTEGER_MAX_VALUE // 10 and pop > 7)):
                return 0
            if (reversed_num < INTEGER_MIN_VALUE // 10 or
                (reversed_num == INTEGER_MIN_VALUE // 10 and pop > 8)):
                return 0
            reversed_num = reversed_num * 10 + pop
        
        return sign * reversed_num

sol = Solution()
x1 = 123
result1 = sol.reverse(x1)
print("Input:", x1, "Output:", result1) 
x2 = -321
result2 = sol.reverse(x2)
print("Input:", x2, "Output:", result2) 
x3 = 120
result3 = sol.reverse(x3)
print("Input:", x3, "Output:", result3)  






 
# class Solution:
#     def reverse(self, x: int) -> int:
#         reversed_num = 0
#         is_negative = x < 0
#         x = abs(x)
        
#         while x != 0:
#             pop = x % 10
#             x //= 10
#             if reversed_num > (2**31 - 1) // 10 or (reversed_num == (2**31 - 1) // 10 and pop > 7):
#                 return 0
#             reversed_num = reversed_num * 10 + pop
        
#         if is_negative:
#             reversed_num = -reversed_num
        
#         return reversed_num

# if __name__ == "__main__":
#     sol = Solution()
    
#     x1 = 123
#     result1 = sol.reverse(x1)
#     print("Input:", x1, "Output:", result1)  # Output: 321

#     x2 = -321
#     result2 = sol.reverse(x2)
#     print("Input:", x2, "Output:", result2)  # Output: -123

#     x3 = 120
#     result3 = sol.reverse(x3)
#     print("Input:", x3, "Output:", result3)  # Output: 21