import random


def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)
    return nums


def partition(nums, low, high):
    pivot = low
    nums[pivot], nums[high] = nums[high], nums[pivot]
    for i in range(low, high):
        if nums[i] <= nums[high]:
            nums[i], nums[low] = nums[low], nums[i]
            low += 1
    nums[low], nums[high] = nums[high], nums[low]
    return low


if __name__ == '__main__':
    user_input = input('Enter number with comma: ')
    unsorted = [int(item) for item in user_input.split(',')]
    print(quick_sort(unsorted, 0, len(unsorted)-1), sep=',')




