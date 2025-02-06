def subset(arr,index=0,current=[]):
    #current=[]
    if index== len(arr):
        print(current)
        return
    subset(arr,index+1,current+[arr[index]]) #include the current element
    subset(arr,index+1,current)             #Exclude the current element

arr=[1,2,3]
subset(arr)
