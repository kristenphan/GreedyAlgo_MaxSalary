# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_greater_or_equal(num1, num2):
    """
    This function takes in 2 strings num1 and num2 representing integer numbers (or -inf, see exception case below)
    The function returns True if the concatenation of num1 and num2 in this exact order
    is greater than the concatenation of num2 and num1.
    The function returns False otherwise.
    Exception: if num2 = -inf (a toy value - see function "largest_number"), return True
    Example:
    Input:
    num1 = 2
    num2 = 21
    Output: True because 221 > 212
    """
    # exception case
    if num2 == float('-inf'):
        return True

    if (num1 + num2) >= (num2 + num1):
        return True
    else:
        return False


def largest_number(numbers):
    """
    This function takes in a set integer numbers and returns the largest number possible out of this set
    """
    numbers = list(map(str, numbers))
    answer = ""
    while numbers:
        max = float('-inf')
        for number in numbers:
            if is_greater_or_equal(number, max):
                max = number
        answer += max
        numbers.remove(max)

    return int(answer)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
