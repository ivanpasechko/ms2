def is_palindrome(text: str) -> bool:
    """Проверяет, является ли строка палиндромом (игнорируя регистр и пробелы)."""
    clean_text = "".join(text.split()).lower()
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    print(is_palindrome("А роза упала на лапу Азора"))  
    print(is_palindrome("hello"))   
