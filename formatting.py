# we can do this with format() method and % operator
#first one is old method % operator
num=int(input("Number:"))
character=input("Character:")
letter=input("Letter:")
print("Entered %f"%num)
print("Entered %.5d"%num)
print("Entered %s %s" %(character,character))
print("Octal format: %o" %num)
print("Hexadecimal format: %x" %num)
print("Char: %c" %letter)

# %d for decimal 
# %f for float
# %s for string
# %i for integer (%d and %i works same)
# %o for octal 
# %x for hexadecimal
# %X for hexadecimal (shows letter uppercase)
# %c for char (to show 1 character)

#second one is new one format()
username="hasanozdem1r"
age=22
status="Student"
country="Turkey"
print("My Github username is {0}, I am a {1} from {2} and my age is {3}".format(username,status,country,age))
print("My Github username is {:s}, I am a {:s}".format(username,12))

# {:s} for string 
# {:d} for decimal
# {:c} for char
# {:o} for octal
# {:x} for hex (with lowercase)
# {:X} for hex (with uppercase)
# {:b} for binary 
