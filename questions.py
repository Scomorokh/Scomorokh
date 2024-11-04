import json
DATAFILE = "data.json"
# Структура квиза
quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Какой из следующих типов данных в Python используется для хранения текста?',
        'options': ['int', 'float', 'str', 'list'],
        'correct_option': 2
    },
    {
        'question': 'Какой оператор используется для проверки равенства двух значений в Python?',
        'options': ['=', '==', '!=', '>='],
        'correct_option': 1
    },
    {
        'question': 'Какой метод используется для добавления элемента в конец списка в Python?',
        'options': ['append()', 'insert()', 'extern()', 'add()'],
        'correct_option': 0
    },
    {
        'question': 'Какой из следующих вариантов является правильным способом определения функции в Python?',
        'options': ['function myFunction():', 'def myFunction():', 'define myFunction():', 'func myFunction():'],
        'correct_option': 1
    },
    {
        'question': 'Какой из следующих циклов используется для перебора элементов в списке?',
        'options': ['if', 'while', 'for', 'switch'],
        'correct_option': 2
    },
    {
        'question': 'Какой из следующих методов используется для чтения всех строк из файла в Python?',
        'options': ['read()', 'readline()', 'readlines()', 'readall()'],
        'correct_option': 2
    },
    {
        'question': 'Какой из следующих операторов используется для обработки исключений в Python?',
        'options': ['try-except', 'catch', 'handle', 'error'],
        'correct_option': 0
    },
    {
        'question': 'Какой из следующих вариантов является правильным способом создания объекта класса в Python?',
        'options': ['myObject = ClassName()', 'myObject = new ClassName()', 'myObject = create ClassName()', 'myObject = ClassName'],
        'correct_option': 0
    }
]

with open(DATAFILE, 'w') as outfile:
    json.dump(quiz_data, outfile)