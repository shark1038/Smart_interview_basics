# #
# Reverse Array bookmark_borderPrint the array in reverse order.
#
# Note:
#  Try solving this using recursion. Do not use any inbuilt functions / libraries for your main logic.  Input Format
# The first line of input contains N - the size of the array and the second line contains the elements of the array.
#
# Output Format
# Print the given array in reverse order.
#
# Constraints
# 1 <= N <= 100
# 0 <= ar[i] <= 1000
#
# Example
# Input
# 5
# 2 19 8 15 4
#
# Output
# 4 15 8 19 2
#
# Explanation
#
# Self Explanatory

a=int(input())
b=list(map(int,input().split()))
print(*b[::-1])