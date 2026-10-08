secret_code = 13
access_key = 9

def bits(number, width=4):
    return format(number & ((1 << width) - 1), f"0{width}b")


print("MY SECRET CODE BIT SCANNER\n")

print("Secret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key:", access_key, "Binary:", bits(access_key))

print("PART 1: Bits and Binary")
print("Binary numbers use only 0 and 1.")
print("Binary of Secret Code:", bits(secret_code))
print("Binary of Access Key:", bits(access_key))

and_result = secret_code & access_key
or_result = secret_code | access_key

print("PART 2: AND and OR")
print("Result of AND:", and_result, "Binary:", bits(and_result))
print("Result of OR:", or_result, "Binary:", bits(or_result))
print("AND only returns 1 for positions where both bits are 1.")
print("OR will return 1 for positions where at least one of the bits are 1.")

not_result = (~secret_code) & 0b1111
xor_result = secret_code ^ access_key

print("PART 3: NOT and XOR")
print("NOT Secret Code within 4 bits:", not_result, "Binary:", bits(not_result))
print("XOR Result:", xor_result, "Binary:", bits(xor_result))
print("XOR will return 1 for each position where the bits are different.")

left_shift = secret_code << 1
right_shift = secret_code >> 1

print("PART 4: Left Shift and Right Shift")
print("Left Shift Result:", left_shift, "Binary:", bits(left_shift, 5))
print("Right Shift Result:", right_shift, "Binary:", bits(right_shift))
print("Left shift will move bits to the left. Right shift will move bits to the right.")

xor_check = secret_code ^ 1

print("PART 5: Odd or Even with XOR")
print("Secret Code XOR 1:", xor_check)

if xor_check == secret_code - 1:
    print("The secret code is odd because XOR with 1 reduced it by 1.")
else:
    print("The secret code is even because XOR with 1 did not change its value.")

bit_count = secret_code.bit_count()

print("PART 6: Counting Bits")
print("Number of 1 bits in Secret Code:", bit_count)

print("SECRET CODE SCAN SUMMARY\n")

print("Secret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key:", access_key, "Binary:", bits(access_key))
print("AND:", and_result)
print("OR:", or_result)
print("NOT within 4 bits:", not_result)
print("XOR:", xor_result)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)
print("Single Bits Count:", bit_count)