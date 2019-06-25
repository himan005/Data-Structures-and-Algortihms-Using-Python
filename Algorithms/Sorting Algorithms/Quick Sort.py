def partition(nums, low, high):
    i = low - 1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return(i+1)


def quicksort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quicksort(nums, low, p-1)
        quicksort(nums, p+1, high)
    return nums


if __name__ == '__main__':
    user_input = input('Enter numbers with comma: ')
    unsorted = [int(item) for item in user_input.split(',')]
    print(quicksort(unsorted, 0, len(unsorted)-1), sep=',')
