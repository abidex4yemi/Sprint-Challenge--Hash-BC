#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    weights.sort()

    for i in range(length):
        diff = limit - weights[i]

        if diff < limit:
            print(diff)
            cached = hash_table_retrieve(ht, diff)
            if cached:
                return cached
            else:
                hash_table_insert(ht, diff, diff)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


print(get_indices_of_item_weights([6, 4, 10, 15, 16], 5, 21))
