# Find Duplicate Number in Array bookmark_borderFind a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
#
# Note:
#  Do not use any inbuilt functions / libraries for your main logic  Input Format
# The first line of input contains the size of the array - N and the second line contains the elements of the array, there will be only a single duplicate element in the array.
#
# Output Format
# Print the duplicate element from the given array.
#
# Constraints
# 2 <= N <= 100
# 0 <= ar[i] <= 109
#
# Example
# Input
# 6
# 5 4 10 9 21 10
#
# Output
# 10
a=int(input())
b=list(map(int,input().split()))
c=[]
seen=set()
duplicate=set()

for i in b:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
f= " ".join(map(str,duplicate))
print(f)