## List are mutuable and dynamic

mix_list = ["hello","world",42,3.14,True]

print(f"item at index 1 : {mix_list[1]}")

nested_list = [["hello","world"],[1.0,2.0,3.0],[True,False]]
print(f"item at index 01 of nested list : {nested_list[0][1]}")

## tuple are immutable and static

tuple1 = (1)
print(type(tuple1))

tuple2 = ("hello", "world", 1.0, 2.0, False)
print(f"item at index 1 : ", tuple2[1])

nested_tuple = (("hello","world"),(1.0,2.0,3.0),(True,False))
print(f"item at index 01 of nested tuple : {nested_tuple[0][1]}")