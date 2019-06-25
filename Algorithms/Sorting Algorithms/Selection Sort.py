def selection_sort(collection):
    for i in range(len(collection)):
        index = i
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[index]:
                index = j
        collection[index], collection[i] = collection[i], collection[index]
    return collection


if __name__ == '__main__':
    user_input = input('Enter the numbers with number: ').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(selection_sort(unsorted), sep=',')


