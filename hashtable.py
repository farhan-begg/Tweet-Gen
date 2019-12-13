#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
            Running time: O(n) because all buckets and each value in bucket have to be accessed """
       
        # Collect all keys in each bucket  
        all_keys = []
        
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
       
        return all_keys


    def values(self):
        """Return a list of all keys in this hash table.
            Running time: O(n) because all buckets and each value in bucket have to be accessed """
       
        all_values = []

        # Loop through all buckets
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)

        # Collect all values in each bucket
        return all_values


    def items(self):
        """Return a list of all keys in this hash table.
            Running time: O(n) because all buckets and each value in bucket have to be accessed """
       
      
        # Collect all pairs of key-value entries in each bucket
        all_items = []
       
        for bucket in self.buckets:
            all_items.extend(bucket.items())
       
        return all_items


    def length(self):
        """Return a list of all keys in this hash table.
            Running time: O(n) because all buckets and each value in bucket have to be accessed """
       
        count = 0
               
        # Loop through all buckets
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            for item in bucket.items():
                count += 1

        return count


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n) Worst Case its the last item in the bucket Best Case one item in bucket O(1)"""

        
        # Find bucket where given key belongs    
        bucket = self.buckets[hash(key) % len(self.buckets)]
        
        # Check if key-value entry exists in bucket
        for key_item, value in bucket.items():
                if key_item == key:
                    return True
        
        return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n) Worst Case its the last item in the bucket Best Case one item in bucket O(1)"""
  
        bucket = self.buckets[hash(key) % len(self.buckets)]
       
        # Check if key-value entry exists in bucket
        for key_item, value in bucket.items():
            if key_item == key:           # <-- If found, return value associated with given key
                return value

        raise KeyError(f'Key not found: {key}')


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(n + n) -> O(n) find and replace both iterate through the list"""
        
        bucket = self.buckets[hash(key) % len(self.buckets)]

        if self.contains(key):
            # Check if key-value entry exists in bucket
            for cur_key, cur_value in bucket.items():
                # If found, update value otherwise insert given-key value into bucket
                if cur_key == key:                 
                    bucket.delete((cur_key, cur_value))   
                    bucket.append((key, value))
        else: 
            bucket.append((key, value))


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n + n) -> O(n) find and replace both iterate through the list""" 
        
        bucket = self.buckets[hash(key) % len(self.buckets)]
        
        item = bucket.find(lambda item: item[0] == key)

        # Check if key-value entry exists in bucket
        if item is not None:
        # If found, delete entry associated with given key
            bucket.delete(item)
        else:
        # Otherwise, raise error to tell user delete failed
            raise KeyError(f'Key not found: {key}')


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
