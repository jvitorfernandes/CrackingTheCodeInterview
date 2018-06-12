#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

close = {'{':'}', '[':']', '(':')'}

def checkBalance(expression):
    
    stck = []
    
    for i, c in enumerate(expression):
        if c in close.keys():
            # print(c)
            if (i < len(expression)-1):
                stck.append(close[c])
        else:
            # print(stck)
            if(len(stck)<=0):
                return False
            elif(c != stck.pop()):
                return False
            # print(stck)
            
    return len(stck)<=0

t = int(input())

for t_itr in range(t):
    expression = input()
    if(checkBalance(expression)):
        print('YES')
    else:
        print('NO')
    
            
