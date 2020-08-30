import PySimpleGUI as sg
from layout import create_layout
from calculator import Calculator
sg.theme('DarkBlue14')

def main():
    layout = create_layout()

    numbers = ('0','1','2','3','4','5','6','7','8','9')
    operations = ('+','-','*','/','%','^')


    number_string = ''
    all_string = ''
    operation = ''
    switch = True
    show = True
    catched_exception = False
    put_coma = True
    sign_change_made = False

    window = sg.Window('Basic Calculator on PySimpleGUI', layout, size = (250,450))

    calculate = Calculator()

    

    while True:
        event, values = window.read()

        if event in (None,'-EXIT-'):
            break

        if event in numbers:
            number_string += event
            all_string += event

            window['temp'].update(all_string)

            calculate.set_temporary()
            show = calculate.choose_temp_operation(operation,float(number_string))

            if show:
                window['result'].update(calculate.get_temporary())
            else:
                window['result'].update('Error:Zero division')

        if event == '-HELP-':
            pass
        
        if event == '-C-':
            number_string = ''
            all_string = ''
            operation = ''
            put_coma = True
            switch = True
            calculate.set_result_zero()
            window['temp'].update(number_string)
            window['result'].update(calculate.get_result())
        
        if event == '-CE-' and all_string:

            if not operation:
                all_string = ''
                number_string = ''

            if operation:
                if sign_change_made != True:
                    number_string = '0'
                    all_string = all_string[0 : all_string.rfind(operation)+1] + number_string
                else:
                    all_string = ''
                    number_string = ''
                    sign_change_made = False
                    calculate.set_result_zero()

            calculate.set_temporary()
            window['temp'].update(all_string)
            window['result'].update(calculate.get_result())
    

        if event == '-COMA-' and all_string[-1:] not in operations and put_coma:
            all_string += '.'
            number_string += '.'
            window['temp'].update(all_string)
            put_coma = False

        if event == '-SUM-' and all_string[-1:] not in operations:

            if switch:
                try:
                    calculate.first_add(float(number_string))
                    switch = False
                except ValueError:
                    catched_exception = True
            else:
                calculate.set_result(calculate.get_temporary())
                window['result'].update(calculate.get_result())

            all_string += '+' if catched_exception != True else ''
            operation = '+' if catched_exception != True else ''
            window['temp'].update(all_string if catched_exception != True else 'Please, insert a number.(•̀o•́)ง')
            catched_exception = False
            number_string = ''

        elif event == '-SUBSTRACT-' and all_string[-1:] not in operations:

            if switch:
                if all_string:
                    calculate.first_add(float(number_string))
                else:   #Vacío, entró por que primero tocó el menos (debe hacer el numero negativo) 
                    sign_change_made = True
                switch = False
            else:
                calculate.set_result(calculate.get_temporary())
                window['result'].update(calculate.get_result())
            
            all_string += '-'
            operation = '-'
            window['temp'].update(all_string)
            number_string = ''

        elif event == '-MUL-' and all_string[-1:] not in operations:

            if switch:
                try:
                    calculate.first_multiplication(float(number_string))
                    switch = False
                except ValueError:
                    catched_exception = True
            else:
                calculate.set_result(calculate.get_temporary())
                window['result'].update(calculate.get_result())

            all_string += 'x' if catched_exception != True else ''
            operation = 'x' if catched_exception != True else ''
            window['temp'].update(all_string if catched_exception != True else 'Please, insert a number.(•̀o•́)ง')
            catched_exception = False
            number_string = ''

        elif event == '-DIV-' and all_string[-1:] not in operations:

            if switch:
                try:
                    calculate.set_result(float(number_string))
                    switch = False
                except ValueError:
                    catched_exception = True
            else:
                calculate.set_result(calculate.get_temporary())
                window['result'].update(calculate.get_result())
            
            all_string += '/' if catched_exception != True else ''
            operation = '/' if catched_exception != True else ''
            window['temp'].update(all_string if catched_exception != True else 'Please, insert a number.(•̀o•́)ง')
            catched_exception = False
            number_string = ''

        elif event == '-MOD-' and all_string[-1:] not in operations:

            if switch:
                try:
                    calculate.set_result(float(number_string))
                    switch = False
                except ValueError:
                    catched_exception = True
            else:
                calculate.set_result(calculate.get_temporary())
                window['result'].update(calculate.get_result())

            all_string += '%' if catched_exception != True else ''
            operation = '%' if catched_exception != True else ''
            window['temp'].update(all_string if catched_exception != True else 'Please, insert a number.(•̀o•́)ง')
            catched_exception = False
            number_string = ''

        elif event == '-DIV1-' and all_string[-1:] not in operations:

            if switch:
                try:
                    calculate.set_result(float(number_string))
                    all_string = ''
                    all_string += '1/' + number_string
                    switch = False
                except ValueError:
                    catched_exception = True
            else:
                calculate.set_result(calculate.get_temporary())
                all_string += operation + '1/' + str(calculate.get_result())
  
            calculate.divide_by_one()
            calculate.set_temporary()
            window['temp'].update(all_string if catched_exception != True else 'Please, insert a number.(•̀o•́)ง')
            catched_exception = False
            window['result'].update(calculate.get_result())
            number_string = ''

        elif event == '-SQRT-' and all_string[-1:] not in operations:

            if switch:
                try:
                    calculate.set_result(float(number_string))
                    all_string = ''
                    all_string += '√' + number_string
                    switch = False
                except ValueError:
                    catched_exception = True
            else:
                calculate.set_result(calculate.get_temporary())
                all_string += operation + '√' + str(calculate.get_result())

            calculate.square_root()
            calculate.set_temporary()

            aux_bool = calculate.get_result() != 0
            all_string = all_string if aux_bool else 'That\'s a negative number(ಠ_ಠ)'
            window['temp'].update(all_string if catched_exception != True else 'Please, insert a number.(•̀o•́)ง')
            all_string = '' if aux_bool == False else all_string
            catched_exception = False
            window['result'].update(calculate.get_result())
            number_string = ''
        
        elif event == '-POT-' and all_string[-1:] not in operations:

            if switch:
                try:
                    calculate.set_result(float(number_string))
                    switch = False
                except ValueError:
                    catched_exception = True
            else:
                calculate.set_result(calculate.get_temporary())
                window['result'].update(calculate.get_result())

            all_string += '^' if catched_exception != True else ''
            operation = '^' if catched_exception != True else ''
            window['temp'].update(all_string if catched_exception != True else 'Please, insert a number.(•̀o•́)ง')
            catched_exception = False
            number_string = ''

        elif event == '-EQUAL-' and all_string[-1:] not in operations:
            aux = calculate.get_temporary()
            boolean = (aux != None)
            if boolean: #Significa que se realizaron operaciones 
                all_string += '='
                calculate.set_result(aux)
                window['result'].update(calculate.get_result())
            
            window['temp'].update(all_string if boolean else 'No operations were made(⌣́_⌣̀)')
            all_string = ''
            number_string = ''
            calculate.reset_calculator()
        
        string_size = len(all_string)
        if string_size > 24: #Maximo caracteres
            surplus = string_size - 24
            all_string = all_string[surplus:]
            window['temp'].update(all_string)

        if number_string == '' and put_coma == False:
            put_coma = True


    window.close()
if __name__ == "__main__":
    main()