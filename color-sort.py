def color_sort(nums):
    counts, index = {}, 0
    for num in nums:
        counts[num] = counts[num] + 1 if num in counts else 1
    for key in sorted(counts):
        nums[index:index+counts[key]] = [key] * counts[key]
        index += counts[key]