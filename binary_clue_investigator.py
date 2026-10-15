print("======== BINARY CLUE INVESTIGATOR ========\n")

x = 7
y = 7

print("PART 1: XOR Identity and Equality")
print("x is: ", x)
print("y is: ", y)
print("x ^ X =", x ^ x)
print("x ^ 0 =", x ^ 0)
 
if (x ^ y) == 0:
    print("Both numbers are equal")
else:
    print("Both numbers are different")

clues = [3, 5, 3, 5, 6]
xor_result = 0
 
for clue in clues:
    xor_result = xor_result ^ clue
 
print("PART 2: XOR Cancellation")
print("Clues:", clues)
print("Final XOR Result:", xor_result)
print("Repeated numbers cancel out, which will leave the single numbers remaining:", xor_result)

numbers = [4, 7, 4, 2, 7, 2, 9]
odd_number = 0
 
for number in numbers:
    odd_number = odd_number ^ number
 
print("PART 3: One Odd-Occurring Number")
print("Numbers:", numbers)
print("Odd-occurring number:", odd_number)

pair_numbers = [3, 9, 3, 5, 5, 7]
xor_of_two = 0
for number in pair_numbers:
    xor_of_two = xor_of_two ^ number
 
print("PART 4: XOR of Two Odd-Occurring Numbers")
print("Numbers:", pair_numbers)
print("XOR of two odd-occurring numbers:", xor_of_two)

rightmost_set_bit = xor_of_two & -xor_of_two
first_odd = 0
second_odd = 0
 
for number in pair_numbers:
    if number & rightmost_set_bit:
        first_odd = first_odd ^ number
    else:
        second_odd = second_odd ^ number
 
print("PART 5: Splitting by the Rightmost Set Bit")
print("Rightmost set bit:", rightmost_set_bit)
print("First odd-occurring number:", first_odd)
print("Second odd-occurring number:", second_odd)

print("\nBINARY CLUE INVESTIGATION SUMMARY\n")

print("XOR Identity: a ^ a = 0")
print("XOR with zero: a ^ 0 = a")
print("XOR Cancellation removes repeated pairs")
print("One odd-occurring number found:", odd_number)
print("The two odd-occuring numbers:", first_odd, "and", second_odd)