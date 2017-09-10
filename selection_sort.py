def find_smallest(array):

    if len(array) > 0:

        smallest = array[0]
        smallest_index = 0

        for i in range(1,len(array)):

            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i

    else:
        print "The array is empty."

    return smallest_index


def selection_sort(array):

    sorted_array = []
    for i in range(len(array)):
        next_smallest = find_smallest(array)
        sorted_array.append(array.pop(next_smallest))

    return sorted_array

def main():

    example = [5,4,2,5,3,100,4,2]
    print selection_sort(example)

if __name__ == "__main__":

    main()
