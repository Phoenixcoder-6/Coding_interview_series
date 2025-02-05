def find_number(arr):
   # Getting the original sum
   first = arr[0]
   n = len(arr)
   last = arr[n-1]
   expected_sum = 0
   original_sum = sum(arr)
   
   # Calculate expected sum from 'first' to 'last'
   for i in range(first, last + 1):
        expected_sum += i
    
   return expected_sum - original_sum  # Return the missing number

arr = [3, 5, 6, 7, 8]  # Missing number is 4
res1 = find_number(arr)
print(res1)  
