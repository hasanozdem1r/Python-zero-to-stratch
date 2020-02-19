#Thanks for documentation to FreeCodeCamp
#Dictionaries 101: A Detailed Visual Introduction
"""
Keys: a key is a value used to access another value. Keys are the equivalent of "indices" in strings, lists, and tuples. In dictionaries, to access a value, you use the key, which is a value itself.
Values: these are the values that you can access with their corresponding key.
"""
dict1={"Gino": 15, "Nora": 30}
"""
Keys have to be unique within one dictionary.
Keys have to be immutable(değişmez).
If the key is a tuple, it can only contain strings, numbers or tuples.
Lists cannot be keys because they are mutable. This is a consequence of the previous rule.
"""
nameWithNumbers={"Hasan":1, "David":2, "Janise":3, "Michael":4, "Hilary":5}

#access values using keys   <variable>[<key>]
print(nameWithNumbers["Hasan"])
print(nameWithNumbers["Michael"])
try:
    print(nameWithNumbers["Jack"])
except Exception:
    print("KeyError")
#Tip: If you try to access a key that does not exist in the dictionary, you will get a KeyError

#Add Key-Value Pairs
nameWithNumbers["Jack"]=6
print(nameWithNumbers)

#Modify a Key-Value Pair
nameWithNumbers["Jack"]=0
print(nameWithNumbers)

#Deleting a Key-Value Pair
del nameWithNumbers["Jack"]
print(nameWithNumbers)

#Check if a Key is in a Dictionary
print("Jack" in nameWithNumbers.keys()) #to check keys
print(1 in nameWithNumbers.values()) #to check values

#Length of a Python Dictionary
print(len(nameWithNumbers))

#Iterate over the Keys
for name in nameWithNumbers:
    print(name)

#Iterate over the Key-Value Pairs
for nameNo in nameWithNumbers.items():
    print(nameNo)

#Assign Keys and Values to Individual Variables
for key, value in nameWithNumbers.items():
	print("Key:", key, "; Value:", value)

# Iterate over the Values
for element in nameWithNumbers.values():
	print(element)
print("Methods")
#Dictionary Methods
dictA={1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f"}
dictB={1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f"}
#.clear()  --> This method removes all the key-value pairs from the dictionary.
dict1.clear()
print(dict1)

#.get(<key>, <default>) --> This method returns the value associated with the key
print(dictA.get(1),"Not Found")
print(dictA.get(10),"Not Found")

#.pop(<key>, <default>) --> This method removes the key-value pair from the dictionary and returns the value.
print(dictB.pop(2))
print(dictB)

#.update(<other>) --> This method replaces the values of a dictionary with the values of another dictionary only for those keys that exist in both dictionaries.
dictA.update({1:"b"})
print(dictA)
