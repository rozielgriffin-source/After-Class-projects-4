seat_numbers = [101, 104, 108, 112, 115, 120, 124, 128, 132, 137, 144, 148]
target_seat = 124


print("The Train Seat Finder")
print("Available Seats:", seat_numbers)
print("Seat to Find:", target_seat)

def binary_search(seats, target):
    low = 0
    high = len(seats) - 1
    steps = 0

    while low <= high:
        steps = steps + 1
        mid = (low + high) // 2
        print("Checking middle seat:", seats[mid])
        if seats[mid] == target:
            return mid, steps
        elif target < seats[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, steps


index, steps = binary_search(seat_numbers, target_seat)

print("Binary Search Result:")
if index != -1:
    print("Seat found at index:", index)
else:
    print("Seat not found.")

print("Steps Taken:", steps)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")

def recursive_binary_search(seats, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    print("Recursive check:", seats[mid])

    if seats[mid] == target:
        return mid
    elif target < seats[mid]:
        return recursive_binary_search(seats, target, low, mid - 1)
    else:
        return recursive_binary_search(seats, target, mid + 1, high)


recursive_index = recursive_binary_search(seat_numbers, target_seat, 0, len(seat_numbers) - 1)

print("Recursive Binary Search Result:")
if recursive_index != -1:
    print("Seat found at index:", recursive_index)
else:
    print("Seat not found.")

print("Recursive Time Complexity: O(log n)")
print("Space Complexity: O(log n) because of the call stack")

print("COMPLEXITY LADDER")

print("O(1): Directly checking one fixed seat")
print("O(log n): Binary search cuts the search space in half each time")
print("O(n): Checks each seat one by one")
print("O(n^2): Every seat is compared with every other seat")


print("=====SUMMARY=====")
print("Binary search will cut the search space in half each time.")
print("This is faster than checking each seat one by one or each seat individually, which is O(n).")