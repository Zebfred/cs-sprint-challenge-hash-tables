def intersection(arrays):

    """
    YOUR CODE HERE
    """
    # Your code here
    length = len(arrays)
    a_dict = {}
    for array in arrays:
        for num in array:
            if num not in a_dict:
                a_dict[num] = 1
            else:
                a_dict[num] += 1
    result = []

    for item in list(a_dict.items()):
        if item[1] == length:
            result.append(item[0])

    return result
#some existing change


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
