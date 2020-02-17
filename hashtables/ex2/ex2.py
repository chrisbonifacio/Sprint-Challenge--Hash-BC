#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        
    def __repr__(self):
        return f"[source: {self.source}, dest: {self.destination}]"


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    route = []
    # build hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    # get the first ticket, source of "NONE", destination should be "LAX"
    current = "NONE"
    
    while True:
        route.append(hash_table_retrieve(hashtable, current))
        current = hash_table_retrieve(hashtable, current)
        if current is "NONE":
            route.pop()
            break
        
    print("ROUTE", route)
    
    return route
        