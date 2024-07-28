# string.capitalize()                   Upper case the first letter in the sentence
capitalize: str = "trungtin"
print(f"capitalize() -> Original string: {capitalize} >> New string: {capitalize.capitalize()}")
     
# string.casefold()                     Make the string lower case
casefold: str = "TrungTintIntRung"
print(f"casefold() -> Original string: {casefold} >> New string: {casefold.casefold()}")
     
# string.center(length, character)      Returns a centered string
center: str = "trungtin"
print(f"center() -> Original string: {center} >> New string: {center.center(20, '-')}")
     
# string.count(value, start, end)       Returns the number of times a specified value occurs in a string
count: str = "t.ru.ngt.in"
print(f"count() -> Original string: {count} >> The dot show up {count.count('.')} times")
   
# string.encode(encoding=encoding, errors=errors): Returns an encoded version of the string
encode: str = "trungtin"
_encode: str = encode.encode(encoding="ascii", errors="ingore")
print(f"encode() -> Original string: {encode} >> New string: {_encode}")

# string.endswith(value, start, end)    Returns true if the string ends with the specified value
endwith: str = "hello trung tin"
_endwith: str = endwith.endswith("tin")
print(f"endswith() -> Original string: {endwith} >> New string: {_endwith}")

    
# string.expandtabs(tabsize)            Sets the tab size of the string 
# string.find(value, start, end)        Searches the string for a specified value and returns the position of where it was found 
# string.format(value1, value2...)      Formats specified values in a string
# string.format_map()                   Formats specified values in a string
# string.index(value, start, end)       Searches the string for a specified value and returns the position of where it was found 
# string.isalnum()                      Returns True if all characters in the string are alphanumeric  
# string.isalpha()                      Returns True if all characters in the string are in the alphabet  
# string.isascii()                      Returns True if all characters in the string are ascii characters  
# string.isdecimal()                    Returns True if all characters in the string are decimals
# string.isdigit()                      Returns True if all characters in the string are digits  
# string.isidentifier()                 Returns True if the string is an identifier
# string.islower()                      Returns True if all characters in the string are lower case 
# string.isnumeric()                    Returns True if all characters in the string are numeric  
# string.isprintable()                  Returns True if all characters in the string are printable  
# string.isspace()                      Returns True if all characters in the string are whitespaces
# string.istitle                        Returns True if the string follows the rules of a title"
# string.isupper                        Returns True if all characters in the string are upper case
# string.join(iterable)                 Converts the elements of an iterable into a string    
# string.ljust(length, character)       Returns a left justified version of the string
# string.lower()                        Converts a string into lower case
# string.lstrip(characters)             Returns a left trim version (left spaces removed) of the string
# string.maketrans(x, y, z)             Returns a translation table to be used in translations
# string.partition(value)               Returns a tuple where the string is parted into three parts
# string.replace(old, new, count)       Returns a string where a specified value is replaced with a specified value
# string.rfind(value, start, end)       Searches the string for a specified value and returns the last position of where it was found
# string.rindex(value, start, end)      Searches the string for a specified value and returns the last position of where it was found
# string.rjust(length, character)       Returns a right justified version of the string
# string.rpartition(value)              Returns a tuple where the string is parted into three parts
# string.rsplit(separator, maxsplit)    Splits the string at the specified separator, and returns a list
# string.rstrip(characters)             Returns a right trim version of the string
# string.split(separator, maxsplit)     Splits the string at the specified separator, and returns a list
# string.splitlines(keeplinebreaks)     Splits the string at line breaks and returns a list
# string.startswith(value, start, end)  Returns true if the string starts with the specified value
# string.strip(characters)              Returns a trimmed version of the string
# string.swapcase()                     Swaps cases, lower case becomes upper case and vice versa
# string.title()                        Converts the first character of each word to upper case
# string.translate(table)               Returns a translated string
# string.upper()                        Converts a string into upper case
# string.zfill(len)                     Fills the string with a specified number of 0 values at the beginning


