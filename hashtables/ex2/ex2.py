#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    #iniate dic
    routes = {}
    # for loop for ticket
    for ticket in tickets:
        # makes routes have the source and destination for a given ticket
        routes[ticket.source]  = ticket.destination

    #NONE object for certain routes
    route = [routes['NONE']]

    for it in range(len(tickets)-2):
        # adds to the hash table for each ticket
        next = routes[route[it]]
    
        route.append(next)
    
        if it == len(tickets)-3:
    
            route.append('NONE')

    return route    

