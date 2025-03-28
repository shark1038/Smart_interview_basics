# Gauntlets bookmark_borderYou have a collection of N gauntlets, each with a specific color represented by A[i]. Your goal is to maximize the number of pairs by repeatedly pairing up gauntlets of the same color. Determine the maximum number of pairs that can be formed.
#
# Input Format
# The first line of input contains an integer N. The second line of input contains an array of size N.
#
# Output Format
# For the given input, print a single line representing the answer.
#
# Constraints
# 1 ≤ N ≤ 102
# 1 ≤ Ai ≤ 103
#
# Example
# Input
# 6
# 4 1 7 4 1 4
#
# Output
# 2
#
# Explanation

a=int(input())
b=list(map(int,input().split()))
c={}

for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1

pairs = 0
for j in c.values():
    pairs+=j//2
print(pairs)