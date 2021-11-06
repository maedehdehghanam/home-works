arr=[]
for x in range(9):
	arr.append((input()))
print(arr)
temp = arr[0]
arr[0] = arr[3]
temp2 = arr[1]
arr[1] = temp
temp = arr[2]
arr[2]= temp2
temp2=arr[5]
arr[5] = temp
temp=arr[8]
arr[8] = temp2
temp2=arr[7]
arr[7] = temp
temp = arr[6]
arr[6] = temp2
arr[3] = temp
print(arr)