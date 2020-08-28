class Calculator:

    def __init__(self):
        self._result = 0
    
    def set_result(self):
        self._result = 0

    def get_result(self):
        return self._result

    def add(self, number):
        self._result += number
    
    def substract(self, number):
        self._result -= number

    def multiplication(self, number):
        self._result *= number

    def division(self, number):
        self._result /= number

    def mod(self, number):
        self._result %= number

    def sign_change(self):
        self._result *= -1
    