#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    answer = ()
    # insert weights as key value pairs (weight: index)
    for i in range(0, length):
        hash_table_insert(ht, (weights[i]), i)
        
    print(ht.storage)
    
    # check hash table for (limit - weight)
    for j in range(0, length):
        # if we found two weights, break loop
        if len(answer) > 1:
            break
            
        # use limit - weight as key for lookup
        if hash_table_retrieve(ht, limit - weights[j]) is not None:
            answer = answer + (hash_table_retrieve(ht, limit - weights[j]),)
            
            # if there are only two weights of the same value and the limit is divisible by two,
            # then add the zero-th index to the answer tuple
            # we must do this because two weight values cannot be saved to the hash table, the values get overwritten
            if length is 2 and limit % length is 0:
                answer = answer + (0,)
                break
            
            
    
    if answer:
        print(answer)
        return answer
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
