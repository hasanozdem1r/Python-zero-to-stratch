#People called this like a f-string because you have to use before string f letter.
#fstring can be used after Python 3.6
name="Python"
version=3.67
creator="Guido van Rossum"

# there is no difference as for Python. Both of them String 
mars=f"Hello World"
world="Hello Mars"
print(type(mars)) # this is string
print(type(world)) # this is string

# can accept to give parameter inside of print func.
print(f"{mars} I am from Mars")
print(f"Ooh welcome :) {world}")
# can accept to give different data types
print(F"I created {name} and now you using version {version} my name is {creator}")

#you can call also method
print(F"I feel I am big that's why I wrote my name big letters. {name.upper()}")

#you can use multiline but you have to add each line F. If you don't add F letter. It doesn't work.
message=f"Hello {name}"\
    f" Your version {version}"\
    f" Your creator {creator}"
print(message)