## implement hash table with collision handling using open addressing

table_size = 10
hash_table = [None] * table_size
DELETED = object()  
def hashing(key):
    return hash(key) % table_size

def insert(key, value):
    i=1
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None and hash_table[index] is not DELETED:
        if hash_table[index][0] == key:
            hash_table[index][1] = value
            return
        index = (index + 1) % table_size      # Linear probing
        # index = (index + i*i) % table_size  # Quadratic probing
        # i = i+1  #quadratic probing
        # if i == table_size:                 #in quadratic probing
        if index == original_index:
            print ("Hash table is full")
            return
    hash_table[index] = (key, value)

def search(key):
    i =1
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0] == key:
            return hash_table[index][1]
        index = (index + 1) % table_size      # Linear probing
        # index = (index + i*i) % table_size  # Quadratic probing
        # if i == table_size:                 #in quadratic probing
        if index == original_index:
            break
    return None

def delete(key):
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0] == key:
            hash_table[index] = DELETED
            return True
        index = (index + 1) % table_size
        if index == original_index:
            break
    return False
    
def display():
    for i, item in enumerate(hash_table):
        if item is DELETED:
            print("index", i, ": DELETED")
        print("index ", i, " : ", item)


print("*** begin *****")
display()
print("****************************")

insert("city1", "Delhi")
insert("city2", "London")
insert("city3", "New York")
print("*** after insert *****")
display()
print("*****search for city2****** : ", search("city2"))