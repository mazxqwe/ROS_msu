
class Fib():
    def __init__(self, value):
        self.value = int(value) if value >= 0 else 0
        self.fib_value = None
    
    @staticmethod
    def fib_func(x):
        return 0 if x == 0 else 1 if x == 1 else Fib.fib_func(x - 1) + Fib.fib_func(x - 2)

    def get_data(self):
        self.fib_value = self.fib_func(self.value)

    def print_result(self):
        print(f'fib = {self.fib_value}')

