

# Searches for the item in the array using
# binary search algorithm.
# Assumptions: The array is sorted
def binary_search(array, low, high, item):

    # Stop searching we have ran out of array!!!
    if low > high:
        return

    mid  = (low+high)/2
    guess = array[mid]

    # if our guess is less than our item
    # we need to look in the upper half of the array
    if guess < item:
        low = mid + 1
        print "low = %d"%(low)
        return binary_search(array,low,high,item)

    # if our guess is greater than our item
    # we need to look in the lower half of the array
    elif guess > item:
        high = mid - 1
        return binary_search(array,low,high,item)

    # we have found our item
    else:
       return guess


def main():

    # example sorted array ranging from 1..11
    example = range(1,20000)

    print "Performing binary search on %s"%(example)
    result = binary_search(example,0,len(example)-1,14000)
    print "The result is %d"%(result)


if __name__ == "__main__":

    main()
