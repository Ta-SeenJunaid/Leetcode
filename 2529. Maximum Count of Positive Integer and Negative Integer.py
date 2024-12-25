class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Total length of the array
        total_length = len(nums)
        
        # Initialize pointers and counters for positive and negative numbers
        left, right = 0, total_length - 1
        positive_count, negative_count = 0, 0
        
        # Binary search to count positive numbers
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                positive_count = total_length - mid  # Count of positive numbers
                right = mid - 1  # Narrow down to the left half
            else:
                left = mid + 1  # Narrow down to the right half
        
        # Reset pointers for counting negative numbers
        left, right = 0, total_length - 1
        
        # Binary search to count negative numbers
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                negative_count = mid + 1  # Count of negative numbers
                left = mid + 1  # Narrow down to the right half
            else:
                right = mid - 1  # Narrow down to the left half
        
        # Return the maximum count of either positive or negative numbers
        return max(positive_count, negative_count)
