# Python already has a built-in dictionary object that serves as a Hash Table, this class is just for my own learning purpose

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, value):
        # Note that we only use integer keys for ease of use with the Hash Function

        hash_value = self.hash_function(key)

        # If the slot is empty
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value

        else:
            # If key already exists, replace old value
            if self.slots[hash_value] == key:
                self.data[hash_value] = value

            # If the existing key is not the key, find the next available slot for our key
            else:
                next_slot = self.rehash(hash_value)

                # Get to the next slot
                while self.slots[next_slot] != None and self.slots[next_slot] != key :
                    next_slot = self.rehash(next_slot)

                # Set new key, if None
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value

                # Otherwise replace old value
                else:
                    self.data[next_slot] = value


    def hash_function(self,key):
        # Remainder Method
        return key % self.size

    def rehash(self,old_hash):
        # For finding next possible positions
        return (old_hash+1) % self.size
    
    def get(self,key):    
        # Getting items given a key

        # Set up variables for our search
        start_slot = self.hash_function(key)
        data = None
        stop = False
        found = False
        position = start_slot
        
        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        return data

    # Special Methods for use with Python indexing
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

h = HashTable(5)
h[1] = 'one'
print(h[1])
h[1] = 'new one'
print(h[1])
print(h[5])



