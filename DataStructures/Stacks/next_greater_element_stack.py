## next greator element using stack

def next_greater_elements(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = nums[i]
        stack.append(i)
    
    return res

    
# Example usage:
nums = [4, 5, 2, 10, 8]
print(next_greater_elements(nums))