# Unique Elements bookmark_borderPrint unique elements of the array in the same order as they appear in the input.
#
# Note:
#  Do not use any inbuilt functions / libraries for your main logic.  Input Format
# The first line of input contains the size of the array - N and the second line contains the elements of the array.
#
# Output Format
# Print unique elements from the given array.
#
# Constraints
# 1 <= N <= 100
# 0 <= ar[i] <= 109
#
# Example
# Input
# 7
# 5 4 10 9 21 4 10
#
# Output
# 5 9 21
#
# Explanation
#
# Self Explanatory

a=int(input())
b=list(map(int,input().split()))
seen = set()
duplicate = set()

for i in b:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
result = [i for i in seen if i not in duplicate]
# or this loop
# result=[]
# for i in seen:
#     if i not in duplicate:
#         result.append(i)
#
f = " ".join(map(str,result))
print(f)