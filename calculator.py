import math

class Calculator:

    def __init__(self):
        self._result = 0
        self._temporary = None
    
    def set_result_zero(self):
        self._result = 0

    def reset_calculator(self):
        '''
            Usado unicamente cuando se toca el botón =
                Establece a la calculadora en su estado inicial.
        '''
        self.set_result_zero()
        self._temporary = None

    def set_temporary(self):
        aux = self._result
        self._temporary = aux

    def set_result(self,new_number):
        '''
            Setea la variable de instancia result, new_number : int
        '''
        self._result = new_number

    def get_result(self):
        return self._result

    def get_temporary(self):
        return self._temporary

    def first_add(self, number):
        self._result += number

    def first_substract(self, number):
        self._result -= number

    def first_multiplication(self, number):
        self.set_result(1)
        self._result *= number

    def sign_change(self):
        self._result *= -1

    def divide_by_one(self):
        try:
            self._result = 1 / self._result
        except ZeroDivisionError:
            pass

    def square_root(self):
        self._result = math.sqrt(self._result) if self._result >= 0 else 0

    def choose_temp_operation(self, operation, actual_number):
        show = True
        if operation == '+':
            self._temporary += actual_number

        elif operation == '-':
            self._temporary -= actual_number

        elif operation == 'x':
            self._temporary *= actual_number

        elif operation == '/':
            try:
                self._temporary /= actual_number
            except ZeroDivisionError:
                window['result'].update('Error:Zero division')
                show = False

        elif operation == '%':
            try:
                self._temporary %= actual_number
            except ZeroDivisionError:
                window['result'].update('Error:Zero division')
                show = False

        elif operation == '^':
            self._temporary = math.pow(self._temporary,actual_number)
        
        return show


    