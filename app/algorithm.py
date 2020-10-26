import re
import sys

sys.setrecursionlimit(10**8)

# standard1 = "(1+4*(5-6)*10)*(6-4)"
# standard2 = "a-((b+c*d)/e)"
# standard3 = "1+2+3"


def is_recursive(expression):
    if "(" in expression or ")" in expression:
        return True
    return False


def is_recursive_maximaly(expression):
    temp = "[/*///+/)/(/-]"
    if re.search(temp, expression):
        return True

    return False


def add_plus_and_minus_to_digits(expression):
    num_of_brackets = 0
    digits = ["+", "-"]

    for i in expression:
        if i == "(":
            num_of_brackets += 1
        elif i == ")":
            num_of_brackets -= 1

        if num_of_brackets == 0 and i in digits:
            return []

    return ["*", "/"]


def split_expression(expression):
    digits = ["-", "+"]
    words = []
    znaks = []
    num_of_brackets = 0

    digits.extend(add_plus_and_minus_to_digits(expression))

    last_i = 0
    for index, i in enumerate(expression):
        if i == "(":
            num_of_brackets += 1
        elif i == ")":
            num_of_brackets -= 1
        elif num_of_brackets == 0 and i in digits:
            words.append(expression[last_i:index])
            znaks.append(i)

            last_i = index + 1

    words.append(expression[last_i:])

    for i in range(len(words)):
        if (words[i][0] == "(" and words[i][-1] == ")") and \
                (not is_recursive(words[i][1:-1]) or list(words[i]).index("(") < list(words[i]).index(")")):

            words[i] = words[i][1:-1]

    return words, znaks


def recursion_sum(expression):
    slugs, znaks = split_expression(expression)

    if is_recursive_maximaly(slugs[0]):
        result = recursion_sum(slugs[0])
    else:
        result = slugs[0]

    for i in range(1, len(slugs)):
        if is_recursive_maximaly(slugs[i]):
            result += recursion_sum(slugs[i])
            result += znaks[i-1]
        else:
            result += slugs[i]
            result += znaks[i-1]

    return result

#
# def print_tests():
#     CONST = 20
#     r1 = recursion_sum(standard1)
#     r2 = recursion_sum(standard2)
#     r3 = recursion_sum(standard3)
#
#     print(r1 + " " * (CONST - len(r1)), "> 1456-*10*+64-*")
#     print(r2 + " " * (CONST - len(r2)), "> abcd*+e/-")
#     print(r3 + " " * (CONST - len(r3)), "> 12+3+")
#
# print_tests()
