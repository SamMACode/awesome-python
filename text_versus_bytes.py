import array
import os
import sys, locale

# The str 'café' has four Unicode characters
string = 'café'
utf8_string = string.encode('utf8')
# length of string s: 4, utf8_string value: b'caf\xc3\xa9', utf8_string length: 5,
# decode from utf8: café
print(f"length of string s: {len(string)}, utf8_string value: {utf8_string}, "
      f"utf8_string length: {len(utf8_string)}, "
      f"decode from utf8: {utf8_string.decode('utf8')}")

cafe = bytes('café', 'utf_8')
# cafe value: b'caf\xc3\xa9', cafe[0]: 99, cafe[:1]: b'c'
print(f"cafe value: {cafe}, cafe[0]: {cafe[0]}, cafe[:1]: {cafe[:1]}")
cafe_array = bytearray(cafe)
# cafe array value: bytearray(b'caf\xc3\xa9'), cafe_arr[-1:] value: bytearray(b'\xa9')
print(f"cafe array value: {cafe_array}, cafe_arr[-1:] value: {cafe_array[-1:]}")

# builds a binary sequence by parsing pairs of hex digits optionally separated by spaces
byte_from_hex = bytes.fromhex('31 4B CE A9')
# bytes value: b'1K\xce\xa9', bytes[:1]: b'1'
print(f"bytes value: {byte_from_hex}, bytes[:1]: {byte_from_hex[:1]}")

# typecode 'h' creates an array of short integers (16 bits)
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
# These are the 10 bytes that represent the five short integers, octets value:
# b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
print(f"octets value: {octets}")

# coping with UnicodeEncodeError when call city.encode('cp437')
city = 'São Paulo'
print(f"utf_8 encode: {city.encode('utf_8')}, utf_16 encode: {city.encode('utf_16')}, "
      f"iso8859_1 value: {city.encode('iso_8859_1')}")
'''
Traceback (most recent call last):
  File "text_versus_bytes.py", line 35, in <module>
    city.encode('cp437')
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/encodings/cp437.py", line 12, in encode
    return codecs.charmap_encode(input,errors,encoding_map)
UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
'''
# city.encode('cp437')
open('cafe.txt', 'w', encoding='utf_8').write('café')
print(f"size of cafe.txt is: {os.stat('cafe.txt').st_size}")
line = open('cafe.txt').read()
print(f"read some data from cafe.txt, content: {line}")
os.remove('cafe.txt')

# Several settings affect the encoding defaults for I/O in Python
expressions = """
locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
"""
my_file = open('dummy', 'w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))
os.remove('dummy')
