# 해쉬테

# 1. sum ascii code THEN % 8 = hash key (the place in the arr)
# 2.


import hashlib
class HashTable:
    def __init__(self, length = 8):
        self.hash_table = [[] for i in range(length)]

    def hash_function(self, key):
        return key % len(self.hash_table)      # for numeric keys

    def insert(self, key, value):
        # compute the hash
        hash_key = self.hash_function(key)

        # this means collision
        if self.hash_table[hash_key] is not None:
            # dictionary only allows for unique keys: so if same, change
            for i in self.hash_table[hash_key]:
                if i[0] == key:
                    i[1] = value
                    break
            # if key is not the same but the hash is! so [[1, 'a'], [9, 'b']]
            else:
                self.hash_table[hash_key].append([key, value])

        # key just doesnt exist.
        else:
            self.hash_table[hash_key].append([key, value])


    def get(self, key):
        hash_key = self.hash_function(key)

        if self.hash_table[hash_key] is None:
            raise KeyError()

        else:
            for i in self.hash_table[hash_key]:
                # i[0] is key and i[1] is value
                if i[0] == key:
                    print(i[1])
                    return i[1]


    def print(self):
        print(self.hash_table)


if __name__ == '__main__':
    ht = HashTable()
    # they have same key value. if then, chain em
    ht.insert(1,'a')
    ht.insert(9,'b')
    ht.get(1)
    ht.print()