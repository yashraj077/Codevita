# 4 2 3 1
MAX = 100000
def Smallest2(arr, n):
	firstmin = MAX
	secmin = MAX
	for i in range(0, n):
		if arr[i] < firstmin:
			secmin = firstmin
			firstmin = arr[i]
		elif arr[i] < secmin:
			secmin = arr[i]
	return firstmin, secmin

a = [4,2,5,3,1]
time = 0

while len(a)!=1:
	f,s = Smallest2(a, len(a))
	time += (f+s)
	a.append(f+s)
	a.remove(f)
	a.remove(s)
print(time)
