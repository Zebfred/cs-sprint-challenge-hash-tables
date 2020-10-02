def intersection(arrays):

    """
    YOUR CODE HERE
    """
    # Your code here
    # length of array
    length = len(arrays)
    #iniate dictionay
    a_dict = {}

    #takes a list from the lists 
    for array in arrays:
        #takes a num from the list
        for num in array:
            # if num not in the dic
            if num not in a_dict:
                #then assign it a key
                a_dict[num] = 1
            # else add it value 
            else:
                a_dict[num] += 1
    # iniate list called result            
    result = []

    # for item in the list created from the dic
    for item in list(a_dict.items()):
        # if item is equal to the length
        if item[1] == length:
            # append item to the result
            result.append(item[0])

    return result
#some existing change


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
