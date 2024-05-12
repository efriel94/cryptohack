from pwn import xor

out = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

partial_key = b'crypto{'

# Obtain the key by XORing the flag part with the corresponding part of the ciphertext
key = b''
for i in range(len(partial_key)):
    key += bytes([partial_key[i] ^ out[i]])
print(key)

# assuming the key is myXORkey so append y at the end 
key += b'y'

# Decrypt the remaining ciphertext using the obtained key
decrypted = b''
for i in range(len(out)):
    # since the key is shorter than the ciphertext, loop back round using mod operator
    decrypted += bytes([key[i % len(key)] ^ out[i]])

print(decrypted)