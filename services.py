import json


def write_json(calories_dict):
    with open('calories.json', 'w') as file:
        json.dump(calories_dict, file, indent=2, ensure_ascii=False)


def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def try_read_json_file(filename):
    try:
        return read_json(filename)
    except FileNotFoundError:
         return {}


HELP_MESSAGE = ('Привет! Я Сырный Король!' +
                '\nЯ подсчитываю калории. Вы можете установить лимит калорий в день и записывать уже съеденые.' +
                '\nДля использования введите команду: /kb' +
                '\nДля помощи используйте команду: /help' +
                '\nКак пользоваться:' +
                '\nНажмите кнопку калории.' +
                '\nНажмите кнопку "записать лимит".' +
                '\nКогда лимит калорий записан, нажмите "Записать калории", когда что нибудь скушали.' +
                '\nЕсли вы идете спать, нажмите кнопку сброс. Она сбросит съеденые калории за день.',
                '\nP.S. Пока что я не знаю как исправить кое какую проблему. Если вы пользуеться первый раз, то используйте после записи лимита командой /kb еще раз.')