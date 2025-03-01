# Merge Two Sorted Arrays bookmark_borderYou are given two sorted integer arrays A and B of size N and M respectively. Print the entire data in sorted order.
#
# Input Format
# First line of input contains N - the size of the array. The second line contains N integers - the elements of the first array. The third line contains M - the size of the second array. The fourth line contains M integers - the elements of the second array.
#
# Output Format
# For each test case, print the entire data in sorted order with each element separated by a space, on a new line.
#
# Constraints
# 1 <= N <= 103
# 1 <= M <= 103
# -105 <= A[i], B[i] <= 105
#
# Example
# Input
# 7
# 1 1 5 8 10 12 15
# 5
# -1 2 4 5 7
#
# Output
# -1 1 1 2 4 5 5 7 8 10 12 15
#
# Explanation
#
# Self Explanatory

a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
e=b+d
e.sort()
print(e)
f=" ".join(map(str,e))
print(f)