message = [char for char in "label"]

letter_rep = [ord(letter) for letter in message]

xor_result = [letter^13 for letter in letter_rep]

print(xor_result)

result = "".join(chr(i) for i in xor_result)

print(result)