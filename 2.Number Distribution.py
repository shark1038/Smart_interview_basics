# Number Distribution bookmark_borderPrint the count of the occurrences of positive integers, negative integers, and zeroes in the given array.
#
# Input Format
# The first line of the input contains an integer N - size of the array, second line of input contains an array elements of the array.
#
# Output Format
# Print the frequencies of zeroes, positives elements and negative elements.
#
# Constraints
# 1 <= N <= 104
# -103 <= arr[i] <= 103
#
# Example
# Input
# 10
# 120 0 -9 89 68 -982 91 -54 -12 -139
#
# Output
# 1 4 5
#
# Explanation
#
# Self Explanatory
# =====================================================================================================
a=int(input())
b=input().split()
c=[]

for i in b:
    c+=[int(i)]
d=0
e=0
f=0
for num in c:
    if num>0:
        d+=1
    elif num<0:
        e+=1
    else:
        f+=1
print(d,e,f)