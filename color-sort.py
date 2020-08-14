# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this problem.
# 
# Example:
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def color_sort(nums):
    counts, index = {}, 0
    for num in nums:
        counts[num] = counts[num] + 1 if num in counts else 1
    for key in sorted(counts):
        nums[index:index+counts[key]] = [key] * counts[key]
        index += counts[key]

# Note: this solution can still be used for any number of color varieties in the collection, not limited to three.
