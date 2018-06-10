#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

a = list(input())
b = list(input())

count = 0;
for c in a:
	if c not in b:
		count+=1
	else:
		b.remove(c)

count+=len(b)

print(count)
