def sortedSquares(nums):
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        sortednums = sorted(nums)
        return sortednums
        
# NOTE:
# This solution works but runs in O(n log n) due to sorting.
# An optimized O(n) solution exists using two pointers.
