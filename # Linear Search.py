# Linear Search
def linear_search(roll_numbers, target):
    for i, roll in enumerate(roll_numbers):
        if roll == target:
            return i
    return -1

# Sentinel Search
def sentinel_search(roll_numbers, target):
    roll_numbers.append(target)  # Add a sentinel at the end
    i = 0
    while roll_numbers[i] != target:
        i += 1
    roll_numbers.pop()  # Remove the sentinel
    if i < len(roll_numbers):
        return i
    return -1

# Binary Search (for sorted data)
def binary_search(roll_numbers, target):
    left, right = 0, len(roll_numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if roll_numbers[mid] == target:
            return mid
        elif roll_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Fibonacci Search (for sorted data)
def fibonacci_search(roll_numbers, target):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < len(roll_numbers):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, len(roll_numbers) - 1)

        if roll_numbers[i] < target:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif roll_numbers[i] > target:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and roll_numbers[offset + 1] == target:
        return offset + 1

    return -1

# Example usage:
roll_numbers_unsorted = [101, 103, 105, 107, 109]
roll_numbers_sorted = [101, 103, 105, 107, 109]

# Linear Search and Sentinel Search on unsorted data
print("Linear Search result:", linear_search(roll_numbers_unsorted, 105))
print("Sentinel Search result:", sentinel_search(roll_numbers_unsorted, 105))

# Binary Search and Fibonacci Search on sorted data
print("Binary Search result:", binary_search(roll_numbers_sorted, 105))
print("Fibonacci Search result:", fibonacci_search(roll_numbers_sorted, 105))