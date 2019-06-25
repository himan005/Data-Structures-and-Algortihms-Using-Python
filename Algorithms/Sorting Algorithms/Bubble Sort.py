def bubble_sort(collection):
    for i in range(len(collection)-1):
        swapped = False
        for j in range(0, len(collection)-i-1):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped:
            break
    return collection


if __name__ == '__main__':
    user_input = input("Enter number separated by comma: ").strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted), sep=',')
