def show_how_it_works(func):
    def my_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional argments:', args)
        print('Keywod argumets:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return my_function

def add_two_numbers(a, b):
    return a + b

add_two_numbers(1, 8)

# 最後の課題の問題17で追加したコード
if __name__ == "__main__":
    decolated_func = show_how_it_works(add_two_numbers)
    print(decolated_func(1, 8))
