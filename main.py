import numpy
import random

'''for x in numpy.arange(0.0, 0.6, 0.1):
    y = 2**x
    print(y)
'''
'''
x = 0
y = 0
while x < 100:
    print(x)
    y += 1
    x = 2**y
'''


n = int(input("Input list size:\n"))
A = []

for i in range(n):
    a = random.randint(0, 100)
    A.append(a)
    print(A[i])

#print(A)
print('\n')
'''

A.pop(2)

for i in range(n-1):
    print(A[i])


A.clear()

print('\n')
print(A)'''

for i in range(1, len(A)-1):
    if A[i-1]<A[i] and A[i]>A[i+1]:
        print(i)
