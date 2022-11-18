arr = [2,9, 8, 1, 0, 88, 7, 33, 15, 10]

for i in range(len(arr)-1):

    j = i+1

    while j>0:

        if arr[j]<arr[j-1]:
            tmp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = tmp

        j-=1


for ele in arr:
    print(ele,end=" ")
