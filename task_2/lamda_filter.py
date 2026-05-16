from typing import Callable, List

def filter_strings(strings: List[str], condition: Callable[[str], bool]) -> List[str]:
    """Принимает массив строк и возвращает новый массив, отфильтрованный по условию."""
    return [s for s in strings if condition(s)]

if __name__ == "__main__":
    test_strings = ["apple", "banana", "a", "hello world", "cat", "aircraft"]

    no_spaces = filter_strings(test_strings, lambda s: " " not in s)

    no_starts_with_a = filter_strings(test_strings, lambda s: not s.lower().startswith("a"))

    long_strings = filter_strings(test_strings, lambda s: len(s) >= 5)

    print("Без пробелов:", no_spaces)
    print("Без буквы 'a':", no_starts_with_a)
    print("Длина >= 5:", long_strings)
    
