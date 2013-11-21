import random
#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#

L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 27, 36]

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return (smaller, [v], bigger)

print partition(L, 84)
# >>>[31, 45, 51, 66, 82, 28, 33, 11, 27, 36, 84, 91, 89]

def top_k (L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L, v)
    # middle used below (in place of [v]) for clarity
    if len(left) == k:   return left
    if len(left)+1 == k: return left + middle
    if len(left) > k:    return top_k(left, k)
    return left + middle + top_k(right, k - len(left) - len(middle))

def minimize_absolute(L):
    leng = len(L)
    if leng  % 2 ==1:
        medPosn = (leng+1)/2
        median = max(top_k(L,medPosn))
    else:
        medInd1 = leng/2
        medInd2 = medInd1 + 1
        median1 = max(top_k(L,medInd1))
        median2 = max(top_k(L,medInd2))
        median = (median1 + median2) /2
    # your code here
    print(median)
    return median

print ( minimize_absolute(L))
