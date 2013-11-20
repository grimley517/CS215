# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time
import math
def count(n):
    # Your code here to count the units of time
    # it takes to execute clique
    answer1 = 2 + n*(n+1)/2
    #answer = 0
    #answer += 2
    #for j in range (n):
    #    answer +=1
    #    for i in range (j):
    #        answer +=1
    #return (answer, answer1)
    return answer1

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j
            

for n in range (10):
    print(count(n))



