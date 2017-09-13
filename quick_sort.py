


def partition(array,left_array,right_array):

    pivot_index = len(array)/2
    pivot = array[pivot_index]

    for i in range(0,len(array)):

        if i == pivot_index:
            continue
        elif array[i] <= pivot:
            left_array.append(array[i])
        else:
            right_array.append(array[i])

    return pivot

def quick_sort(array):

    left_array = []
    right_array = []

    if len(array) < 2:
        return array

    pivot = partition(array,left_array,right_array)
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)






def main():

    example_array = [3,5,2,1,4,-5,-2,2,4]
    pivot_index = (len(example_array)/2 ) -1
    print example_array[pivot_index]
    print quick_sort(example_array)

if __name__ == "__main__":
    main()
