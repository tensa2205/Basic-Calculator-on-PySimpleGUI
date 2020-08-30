def create_layout():
    import PySimpleGUI as sg
    output = [
        [sg.Text('',key = 'temp',background_color='white',text_color = 'black',size = (75,1),font= (None,11),auto_size_text=True)],
        [sg.Text('-'*50,text_color = 'black',background_color='white')],
        [sg.Text('0',key = 'result',background_color='white',text_color = 'black',size = (75,2),font= (None,16))]
    ]

    first_column = [
        [sg.Button(image_filename = 'images/help.png',key = '-HELP-'),sg.Button(image_filename = 'images/delete_all.png',key = '-C-'), sg.Button(image_filename = 'images/delete_temporary.png', key = '-CE-'), sg.Button(image_filename = 'images/mod.png',key = '-MOD-')]
    ]

    second_column = [
        [sg.Button(image_filename = 'images/division.png', key = '-DIV-'),sg.Button(image_filename = 'images/sqrt.png', key = '-SQRT-'), sg.Button(image_filename = 'images/pot.png', key = '-POT-'),sg.Button(image_filename = 'images/division_1.png', key = '-DIV1-')]
    ]

    vertical_column = [
        [sg.Button(image_filename = 'images/multiplication.png', key = '-MUL-')],
        [sg.Button(image_filename = 'images/substraction.png', key = '-SUBSTRACT-')],
        [sg.Button(image_filename = 'images/sum.png', key = '-SUM-')],
        [sg.Button(image_filename = 'images/equal.png', key = '-EQUAL-')]
    ]

    number_column = [
        [sg.Button(image_filename = 'images/7.png',key = '7'),sg.Button(image_filename = 'images/8.png',key = '8'),sg.Button(image_filename = 'images/9.png',key = '9')],
        [sg.Button(image_filename = 'images/4.png',key = '4'),sg.Button(image_filename = 'images/5.png',key = '5'),sg.Button(image_filename = 'images/6.png',key = '6')],
        [sg.Button(image_filename = 'images/1.png',key = '1'),sg.Button(image_filename = 'images/2.png',key = '2'),sg.Button(image_filename = 'images/3.png',key = '3')],
        [sg.Button(image_filename = 'images/0.png',key = '0'),sg.Button(image_filename = 'images/coma.png', key = '-COMA-'),sg.Button(image_filename = 'images/plus_minus.png',key = '-CONVERT-')]
    ]
    layout = [
        [sg.Column(output,size=(250,125),background_color='white')],
        [sg.Column(first_column)],
        [sg.Column(second_column)],
        [sg.Column(vertical_column, key = '-VC-'),sg.Column(number_column)],
        [sg.Button('',key ='-EXIT-',visible = False)]
    ]


    return layout