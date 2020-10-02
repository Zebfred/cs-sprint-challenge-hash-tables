def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #iniate dic
    cache = {}
    #for loop that takes an item from the weight's list
    for it in range(len(weights)):
        # if item from weight is in cache and the item from weight 
        # is equal to the value in the cache
        if (weights[it] in cache) and (weights[it] == cache[weights[it]][1]):
        # return the key of that item in cache
            return (it, cache[weights[it]][0])

        # cache[weights[it]] is assigned the var of item from weight and limit - weight value 
        cache[weights[it]] = (it, limit-weights[it]) 
    # the cache is sorted 
    cache_sorted = sorted(cache.items(), reverse=True, key=lambda x: x[1][0])

    #for loop that takes item from the sorted cache
    for item in cache_sorted:
        #if item meets correct conditions
        if item[1][1] in cache:
            # makes the tuple that were looking for
            answer = (item[1][0], cache[item[1][1]][0])
            return answer
    # if the conditions are not met return NONE
    return None
