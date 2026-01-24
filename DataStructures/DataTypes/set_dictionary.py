## dictionary => keys - immutable set : values - any type
dict1  = dict()
complex_dict = dict()
dict1 = {
    "user1_email": "marvel@galaxy.org",
    "user2_email": "maveric@galaxy.org"
}
print(f"user1 email : {dict1['user1_email']}")

complex_dict = { 
    "user1": {
        "name": "marvel",
        "email": "marvel@galaxy",
        "age": 30,
        "sex": "M",
        "address": {
            "street": "123 galaxy road",
            "city": "DEL",
            "State": "IND"
        }
    },
    "user2": {

        "name": "melody",
        "email": "maveric@galaxy",
        "age": 35,
        "sex": "F",
        "address": {
            "street": "10 avenue road",
            "city": "HYD",
            "State": "IND"
        }
    }
}

print(f"user1 city : {complex_dict['user1']['address']['city']}")
print(f"user2 address : {complex_dict['user2']['address']['city']}")

## set => mutable, unordered, unique items, no nested
s1 = set()
s1 = {"alpha", "beta", "gamma", "delta"}
print(s1)
i =0
for item in s1:
    print(f"item at {i} : {item}")
    i += 1