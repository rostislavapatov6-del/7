def error_handler(func):
    def wrapper(expression):
        try:
            result = func(expression)
            print("Результат:", result)
            return result
        except ZeroDivisionError:
            print("Помилка: ділення на нуль!")
        except SyntaxError:
            print("Помилка: неправильний математичний вираз!")
        except NameError:
            print("Помилка: невідома змінна!")
        except Exception as e:
            print("Виникла помилка:", e)

    return wrapper


@error_handler
def calculate(expression):
    return eval(expression)
