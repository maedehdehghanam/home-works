def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def smallest_greater(array):
	flag1=-1
	flag2=-1
	for i in range(len(array)-1, -1, -1):
		for j in range(i-1, -1, -1):
			if array[j]<array[i]:
				flag1 = i
				flag2 = j
				break
		if flag1!=-1:
			print(flag1)
			print(flag2)
			break
	if flag1==-1:
		print("No possible option!")
	else:
		d = flag1 - flag2
		temp = array[flag1]
		array[flag1]= array[flag2]
		array[flag2]=temp
		array2 = array[len(array)-(d+1):]
		mergeSort(array2)
		i = 0
		for x in range(len(array)-(d+1),len(array)):
			array[x]=array2[i]
			i=1+i
		print(array)

array = []
size = int(input())
for i in range(size):
	array.append(int(input()))
smallest_greater(array)