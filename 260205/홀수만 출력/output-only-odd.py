min_num, max_num = list(map(int,input().split()))

for i in range(min_num, max_num+1):
    if i % 2 == 1:
        print(i,end=" ")