N = int(input())
T = int(input())
arr = []
dist = []
for _ in range(N):
  x = list(map(int,input("").split()))
  dist.append(x[-1])
  x.pop(-1)
  arr.append(x)
temp = [0]*N
temp_sum = [0]*N
for i in range(1, len(arr[0]), 2):
  j = 0
  while j<N:
    temp_sum[j] += arr[j][i]*dist[j] + arr[j][i-1]*dist[j]
    j+=1
  index = temp_sum.index(max(temp_sum))
  temp[index]+=1
print(temp.index(max(temp))+1)