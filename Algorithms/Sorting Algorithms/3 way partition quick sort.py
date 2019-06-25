# Dutch national Flag
# def partition(nums, low, high):
#     if high - low <= 1:
#         if nums[high] < nums[low]:
#             nums[high], nums[low] = nums[low], nums[high]
#         i = low
#         j = high
#         return
#
#     mid = low
#     pivot = nums[high]
#     while mid <= high:
#         if nums[mid] < pivot:
#             nums[low+1], nums[mid+1] = nums[mid+1], nums[low+1]
#         elif nums[mid] == pivot:
#             mid +=1
#         elif nums[mid] > pivot:
#             nums[mid], nums[high-1] = nums[high-1], nums[mid]
#     i = low - 1
#     j = mid
#     return i, j

# def quick_sort(nums, low, high):
#     if low >= high:
#         return
#     i, j = partition(nums, low, high)
#     quick_sort(nums, low, i)
#     quick_sort(nums, j, high)
#     return nums
#
#
# if __name__ == '__main__':
#     user_input = input("Enter number with comma: ")
#     unsorted = [int(item) for item in user_input.split(',')]
#     print(quick_sort(unsorted, 0, len(unsorted)-1), sep=',')


import random

def partition(nums, low, high):
    lt = low
    i = low
    gt = high
    pivot = nums[low]

    while i<= gt:
        if nums[i] < pivot:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt +=1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= i
        else:
            i += 1
    return lt, gt


def quick_sort(nums, low, high):
    if low >= high:
        return
    k = random.randint(low, high)
    nums[k], nums[low] = nums[low], nums[k]
    lt, gt = partition(nums, low, high)
    quick_sort(nums, low, lt-1)
    quick_sort(nums, gt+1, high)
    return nums


if __name__ == '__main__':
    user_input = input('Enter the numbers with comma: ')
    unsort = [int(item) for item in user_input.split(',')]
    print(quick_sort(unsort, 0, len(unsort)-1), sep = ',')

