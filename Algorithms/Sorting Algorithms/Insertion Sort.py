def insertionsort(collection):
    for i in range(1, len(collection)):
        key = collection[i]
        j = i-1
        while j >= 0 and key < collection[j]:
            collection[j+1] = collection[j]
            j -= 1
        collection[j + 1] = key
    return collection


if __name__ == '__main__':
    user_input = input("Enter the number with comma: ")
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertionsort(unsorted), sep = ',')
