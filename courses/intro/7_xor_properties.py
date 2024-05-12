# url: https://cryptohack.org/courses/intro/xor1/

"""
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 (A)
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e (B)
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 (C)
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf (D)
"""

# Therefore to find Key2, Key3, Flag:
# Key2 = Key1 ^ B
# Key3 = Key2 ^ C
# Flag = Key1 ^ Key3 ^ Key2 ^ D

A = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
B = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
C = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
D = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

KEY1 = A
KEY2 = bytes([a ^ b for a,b in zip(KEY1,B)])
KEY3 = bytes([a ^ b for a,b in zip(KEY2,C)])
FLAG = bytes([a ^ b ^ c ^ d for a,b,c,d in zip(KEY1,KEY3,KEY2,D)])

print(FLAG)