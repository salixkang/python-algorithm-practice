# mars

t = int(input())

test = [[] for _ in range(t)]

for i in range(t):
    test[i].append(int(input()))
    n = test[i][0]
    cost = [[] for _ in range(n)]
    for j in range(n):
        cost[j] = list(map(int, input().split()))

    test[i].append(cost)




#
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4