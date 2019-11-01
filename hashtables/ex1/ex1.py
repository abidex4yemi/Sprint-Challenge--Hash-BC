#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    result = []

    for i in range(length):
        hash_table_insert(ht, weights[i], weights[i])

    for i in range(length):
        diff = limit - weights[i]

        cached = hash_table_retrieve(ht, diff)
        if cached:
            result.append(i)
    if len(result):
        print(result[::-1])
        return result[::-1]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
