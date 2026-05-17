#162095204
from typing import List, Union

DIGITS = "0123456789"
BASE = 10


def decode_string(encoded_string: str) -> str:
    stack: List[Union[str, int]] = []
    current_string = ""
    current_number = 0
    
    for character in encoded_string:
        if character in DIGITS:
            current_number = current_number * BASE + int(character)
        elif character == '[':
            stack.append(current_string)
            stack.append(current_number)
            current_string = ""
            current_number = 0
        elif character == ']':
            repeat_count = stack.pop()
            previous_string = stack.pop()
            current_string = previous_string + current_string * repeat_count
        else:
            current_string += character
    
    return current_string


if __name__ == "__main__":
    try:
        input_line = input().strip()
        decoded_result = decode_string(input_line)
        print(decoded_result)
    except EOFError:
        print("")
