#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

# n: number of array elements
# d: number of rotations to perform:
# a: array

def rotLeft(n, d, a):

	b = [None for i in range(n)]

	for i in range(n):
		b[i-d] = a[i]

	return b

n, d = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

print(rotLeft(n, d, a))
