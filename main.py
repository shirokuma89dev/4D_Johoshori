def find_matching_bracket_index(bracket_string, num):
    MAX_SIZE = 128
    stack = [0 for _ in range(MAX_SIZE)]
    stack_pointer = 0

    for index in range(len(bracket_string)):
        char = bracket_string[index]
        if char == "(":
            stack[stack_pointer] = index
            stack_pointer += 1
        elif char == ")":
            stack_pointer -= 1
            if stack_pointer < 0:
                return None
            if stack[stack_pointer] == num:
                return index
            if index == num:
                return stack[stack_pointer]

    return None


bracket_string = "((()(()())))"
num = 3

matching_bracket_index = find_matching_bracket_index(bracket_string, num)
print(
    num,
    "番目の括弧に対応する括弧は",
    matching_bracket_index,
    "番目の",
    bracket_string[matching_bracket_index],
    "です。",
)
