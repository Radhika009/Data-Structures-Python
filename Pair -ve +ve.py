'''

Pairs of Positive Negative values in an array
Given an array of distinct integers, print all the pairs having positive value and negative value of a number that exists in the array. We need to print pairs in order of their occurrences. A pair whose any element appears first should be printed first.

Examples:

Input  :  arr[] = { 1, -3, 2, 3, 6, -1 }
Output : -1 1 -3 3

Input  :  arr[] = { 4, 8, 9, -4, 1, -1, -8, -9 }
Output : -1 1 -4 4 -8 8 -9 9


(Simple : O(n2))
The idea is to use two nested loop. For each element arr[i], find negative of arr[i] from index i + 1 to n – 1 and store it in another array. For output, sort the stored element and print negative positive value of the stored element.


'''

  
# Print pair with negative and  
# positive value 
def printPairs(arr, n): 
    v = [] 
  
    # For each element of array. 
    for i in range(n):  
  
        # Try to find the negative value  
        # of arr[i] from i + 1 to n 
        for j in range( i + 1,n) : 
  
            # If absolute values are  
            # equal print pair. 
            if (abs(arr[i]) == abs(arr[j])) : 
                v.append(abs(arr[i]))  
  
    # If size of vector is 0, therefore  
    # there is no element with positive 
    # negative value, print "0" 
    if (len(v) == 0): 
        return; 
  
    # Sort the vector 
    v.sort() 
  
    # Print the pair with negative  
    # positive value. 
    for i in range(len( v)): 
        print(-v[i], "" , v[i], end = " ")  
  
# Driver Code 
if __name__ == "__main__": 
    arr = [ 4, 8, 9, -4, 1, -1, -8, -9 ] 
    n = len(arr) 
    printPairs(arr, n) 








































