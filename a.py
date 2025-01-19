str="1"
str_encoded= str.encode('utf_16','strict')
print("The encoded string is: ", str_encoded)
str_decoded=str_encoded.decode('utf_16', 'strict')
print("The decoded string is: ", str_decoded)        
print("b'\x1b'")