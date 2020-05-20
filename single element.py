'''
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

To find unqiue no --->Brut force method --->check next element ---->o(n)

for o(log n)-->Binary Search

 '''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left +(right - left) // 2
            check_even = (right - mid) % 2 == 0
            
            if nums[mid+1] == nums[mid]:
                
                #check if half is evne 
                if check_even:
                    left = mid + 2
                else:
                    right = mid - 1
                    
            elif nums[mid - 1] == nums[mid]:
                if check_even:
                    right = mid -2 
                else:
                    left = mid + 1
            else:
                return nums[mid]
            
        return nums[left]
