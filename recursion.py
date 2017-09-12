


def sum_array(array):

    if len(array) == 0:
        return 0

    return array[0]+sum_array(array[1:])

def length(array):

    if array == []:
        return 0
    return 1+length(array[1:])


def _max(a,b):
    if a > b:
        return a
    return b

def max_number(array):

    mid = (len(array)/2) - 1

    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return _max(array[0],array[1])

    return _max(max_number(array[:mid+1]),max_number(array[mid+1:]))

def alternate_max_number(array):

    print array
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = alternate_max_number(array[1:])
    return array[0] if array[0] > sub_max else sub_max

def main():
    print sum_array([1,2,3]) == sum([1,2,3])
    print sum_array(range(1,100)) == sum(range(1,100))
    print sum_array([]) == sum([])
    print length([1,2,3]) == len([1,2,3])
    print length(range(1,100)) == len(range(1,100))

    print max_number([1,11000,3,500,2,34,50,9000])
    print alternate_max_number([1,11000,3,500,2,34,50,9000])
if __name__ == "__main__":
    main()
