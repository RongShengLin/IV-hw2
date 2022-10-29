import math
import random

def cal_worst(l, n, tau):
    out = 0
    for i in range(n):
        B = 0
        for j in range(n):
            if l[i][0] <= l[j][0] and l[j][1] > B:
                B = l[j][1]
        Q = B
        findsol = False
        while True:
            RHS = B
            for j in range(n):
                if l[i][0] > l[j][0]:
                    RHS += (math.ceil((Q + tau) / l[j][2]) * l[j][1])
            if RHS + l[i][1] >= l[i][2]:
                findsol = False
                break
            elif Q == RHS:
                findsol = True
                break
            else:
                Q = RHS
        if findsol:
            out += Q + l[i][1]
        else:
            return 1000
    return out

n = int(input())
tau = float(input())
l = []
for i in range(n):
    P, C, T = input().split()
    l.append([int(P), float(C), float(T)])
old_costS = cal_worst(l, n, tau)
T = 500
r = 0.5
mini = float("INF")
it = 1000
ans = []
while(T > 0):
    a = random.randint(0,n-1)
    b = random.randint(0,n-1)
    l[a][0] , l[b][0] = l[b][0], l[a][0]
    new_costS = cal_worst(l, n, tau)
    if(new_costS < mini):
        mini = new_costS
        ans = []
        for i in range(n):
            ans.append(l[i][0])
    #print(new_costS, old_costS, T)
    if(new_costS > old_costS):
        prob = math.exp(-(new_costS - old_costS)/T)
        p = random.uniform(0,1)
        if(p > prob):
            l[a][0], l[b][0] = l[b][0], l[a][0]
            #print("no_change")
        #else:
            #print("change")
    T = r * T
#for i in range(n):
#    print(l[i][0])
#print(cal_worst(l, n, tau))
for i in range(n):
    print(ans[i])
print(mini)

