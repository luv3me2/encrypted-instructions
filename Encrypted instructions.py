#162083365
from typing import List, Union

def decode_string(s: str) -> str:
    stack: List[Union[str, int]] = []
    current_string = ""
    current_number = 0
    
    for char in s:
        if char.isdigit():
            # Формируем число (может быть многозначным)
            current_number = current_number * 10 + int(char)
        elif char == '[':
            # Сохраняем текущую строку и число в стек
            stack.append(current_string)
            stack.append(current_number)
            # Сбрасываем для нового уровня
            current_string = ""
            current_number = 0
        elif char == ']':
            # Извлекаем число и предыдущую строку из стека
            num = stack.pop()
            prev_string = stack.pop()
            # Повторяем текущую строку num раз и добавляем к предыдущей
            current_string = prev_string + current_string * num
        else:
            # Обычный символ (буква)
            current_string += char
    
    return current_string


def main() -> None:
    try:
        line = input().strip()
        result = decode_string(line)
        print(result)
    except EOFError:
        print("")


if __name__ == "__main__":
    main()
