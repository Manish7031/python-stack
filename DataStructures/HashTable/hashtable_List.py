## hash table implemntation using list

table_size = 10
hash_table = [[] for _ in range(table_size)]  # Create a list of empty lists for chaining

def hashing(key):
    return hash(key) % table_size

def insert(key, value):
    index = hashing(key)
    for item in hash_table[index]:
        if item[0] == key:
            item[1] = value  # Update existing key
            return
    hash_table[index].append([key, value])  # Insert new key-value pair

def search(key):
    index = hashing(key)
    for item in hash_table[index]:
        if item[0] == key:
            return item[1]
    return None

def delete(key):
    index =  hashing(key)
    for i, item in enumerate(hash_table[index]):
        if item[0] == key:
            del hash_table[index][i]
            return True
    return False
    

def display():
    for i, item in enumerate(hash_table):
        print("bucket ", i, " : ", item)

display()
insert("name", "Alice")
insert("age", 30)
insert("city", "New York")
print("*** after insert *****")
display()
print("search for name: ", search("name"))




