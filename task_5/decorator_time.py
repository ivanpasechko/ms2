import time
from typing import Callable, Any

def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.6f} сек.")
        return result
    return wrapper

@timer_decorator
def sum_two_numbers(a: float, b: float) -> None:
    print(f"Результат сложения: {a + b}")

@timer_decorator
def sum_from_file(input_path: str, output_path: str) -> None:
    with open(input_path, 'r') as f:
        data = f.read().split()
        a, b = float(data[0]), float(data[1])
    
    result = a + b
    
    with open(output_path, 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    sum_two_numbers(5.5, 4.5)
    # Файлы должны находиться в рабочей директории скрипта
    sum_from_file("input.txt", "output.txt")