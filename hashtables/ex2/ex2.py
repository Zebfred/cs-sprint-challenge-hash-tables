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
    routes = {}
    for ticket in tickets:
        routes[ticket.source]  = ticket.destination

    
    route = [routes['NONE']]
    for it in range(len(tickets)-2):
        next = routes[route[it]]
        route.append(next)
        if it == len(tickets)-3:
            route.append('NONE')

    return route    

