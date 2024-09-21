"""Python Function to Find Duplicate in Array with O(1) Extra Space: Given an array
of n+1 integers where each integer is between 1 and n, find the
duplicate number. The solution must not use extra space."""
def find_duplicate(nums):
    """
    Function to Find Duplicate in Array with O(1) Extra Space
    :param nums: Object of the input list
    :return: Object of the output list
    """
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))
