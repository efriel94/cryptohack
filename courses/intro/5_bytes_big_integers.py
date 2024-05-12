from Crypto.Util.number import *

#  opttion 1 - convert to long to bytes
bytes_msg = long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
print(bytes_msg.decode())

# option 2 - Convert the integer back into a bytes object
integer_value = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# convert bits into bytes
byte_array = integer_value.to_bytes((integer_value.bit_length() + 7) // 8, 'big')

# Convert the bytes object to a string assuming ASCII encoding
message = byte_array.decode('ascii')

print(message)
