"""

"""

def linear_search(array, element_to_found):
    for elements in array:
        if element_to_found == elements:
            print "element was found it!"
            break
        else:
            print "element was not found it!"
            continue


def binary_search(array, element_to_found):
    first = 0
    last = len(array)-1
    middle = int(len(array)/2)

    if array[middle] == element_to_found:
        print "element was found it!"
    elif array[middle] > element_to_found:
        binary_search(array[first:middle-1], element_to_found)
    elif array[middle] < element_to_found:
        binary_search(array[middle+1:last], element_to_found)


def binary_search_without_recursive(array, element_to_found):
    first = 0
    last = len(array) - 1

    while first <= last:
        middle = (first + last) // 2
        if array[middle] == element_to_found:
            print "element was found it"
            break
        elif element_to_found < array[middle]:
            last = middle - 1
        else:
            first = middle + 1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 8, 10, 13, 17, 19, 32, 40, 50, 100, 110, 120, 3000, 4000, 5000]
    linear_search(arr, 2)
    binary_search(arr, 5000)
    binary_search_without_recursive(arr, 5000)
