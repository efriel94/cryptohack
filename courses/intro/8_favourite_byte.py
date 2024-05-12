# url: https://cryptohack.org/courses/intro/xorkey0/

from binascii import unhexlify

data_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
# data_decode = bytes.fromhex(data_hex)
data_decode = unhexlify(data_hex)

print(f"data_hex: {data_hex}")
print(f"data decoded: {data_decode}")

def single_xor(message: bytes, key: int):
    xor_result = b''
    for data in message:
        xor_result += bytes([data ^ key])
    try: 
        return xor_result.decode("utf-8")
    except:
        print("cannot decode!")


for bit in range(256):
    possible_result = single_xor(data_decode, bit)
    if "crypto" in possible_result:
        print(f"Key {bit} -> Result: {possible_result}")
        break