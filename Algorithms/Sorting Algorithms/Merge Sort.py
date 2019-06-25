def merge_sort(nums):
    if len(nums) < 0:
        return 'Enter more then 5 element'
    elif len(nums) == 1:
        return
    else:

        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left = 0
        right = 0
        result = 0

        while left < len(left_half) and right < len(right_half):
            if left_half[left] < right_half[right]:
                nums[result] = left_half[left]
                left += 1
            else:
                nums[result] = right_half[right]
                right += 1
            result += 1

        while left < len(left_half):
            nums[result] = left_half[left]
            result += 1
            left += 1

        while right < len(right_half):
            nums[result] = right_half[right]
            result += 1
            right += 1

    return nums


if __name__ == '__main__':
    user_input = input('enter the number with comma: ')
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted),sep = ',')