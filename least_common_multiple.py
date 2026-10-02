numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))

number1 = numberLargest
number2 = numberSmallest

while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

HCF = numberLargest
LCM = (number1 * number2) // HCF

print("LCM is : ", LCM)