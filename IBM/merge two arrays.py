import math
def merge(arr1,arr2,n,m):
    gap=math.ceil((n+m)/2)

    while gap>0:
        i=0
        while i+gap <n:
            if arr1[i] > arr1[i+gap]:
                arr1[i],arr1[i+gap] =arr1[i+gap],arr1[i]
            i += 1

        j=max(0,gap-n)
        while i<n and j<m:
            if arr1[i] > arr2[j]:
                arr1[i],arr2[j]= arr2[j],arr1[i]

            i+=1
            j+=1

        j=0
        while j+gap<m:
            if arr2[j]>arr2[j+gap]:
                arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
            j+=1

        if gap==1:
            break
        gap= math.ceil(gap/2)



arr1=[1,4,7,8,10]
arr2=[2,3,9]
n=len(arr1)
m=len(arr2)


merge(arr1,arr2,n,m)
print(arr1,arr2)




