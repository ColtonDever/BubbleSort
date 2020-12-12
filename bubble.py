array = [5,2,12,14,23,9,1,0,2]
for i in range(len(array)-1,0,-1):
    for i in range(i):
        if array[i]>array[i+1]:
            b = array[i]
            array[i] = array[i+1]
            array[i+1] = b
            print(array)
print("Sorted Array: ",array)