"""
Binary files store data in 0's and 1's that is machine readable.
 A byte is collection of 8-bits. One character stores one byte in the memory that is 8-bits.
  For example, the binary representation of character 'H' is 01001000 and convert this 8-bit binary string into decimal gives you 72
"""

binary_file = open("binary_file.bin",mode="wb+")
text = "Hello World"
encoded = text.encode("utf-8")
binary_file.write(encoded)
binary_file.seek(0)
binary_data=binary_file.read()
print("binary:",binary_data)
text=binary_data.decode("utf-8")
print("Decoded data:", text)
