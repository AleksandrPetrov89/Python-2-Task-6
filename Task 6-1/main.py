def entering_document_number():
    return input('\nВведите номер документа: ').strip()


def output_name_by_number(number, list1):
    """
    Вывод имени и типа документа с номером "number" из каталога.
    Если документа с таким номером нет - выводит соответствующее сообщение.
    Структура каталога: [{"type": "el", "number": "el", "name": "el"},
                      {"type": "el", "number": "el", "name": "el"}, ...]
    """
    for document in list1:
        if document["number"] == number:
            print(f'"{document["name"]}" имеет "{document["type"]}" с номером "{number}"')
            return f'"{document["name"]}" имеет "{document["type"]}" с номером "{number}"'
    else:
        print(f'Человек с номером документа "{number}" не найден!')
        return f'Человек с номером документа "{number}" не найден!'


def output_shelf_by_number(number, dict1):
    """
    Вывод номера полки на которой содержится искомый документ с номером "number".
    В таком случае функция возвращает "number".
    Если документа с таким номером нет - выводит соответствующее сообщение, функция возвращает None.
    Структура словаря: {'1': [], '2': [], '3': [], ...}
    """
    for shelf, elements in dict1.items():
        if number in elements:
            print(f'Документ с номером "{number}" находится на "{shelf}" полке!')
            return f'Документ с номером "{number}" находится на "{shelf}" полке!'
    else:
        print(f'Документ с номером "{number}" не найден!')
        return f'Документ с номером "{number}" не найден!'


def output_all_documents(list1):
    print()
    for document in list1:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def input_new_document():
    """
    Пользовательский ввод данных для создания нового документа.
    Функция возвращает список из трех элементов.
    """
    list1 = [input('\nВведите тип документа: ').strip(), input('Введите номер документа: ').strip(),
             input('Введите имя и фамилию: ').strip()]
    return list1


def shelf_check(dict1):
    """
    Пользовательский ввод номера полки и проверка, что такая полка существует в перечне полок "dict1".
    Цикл будет повторятся пока не будет указана существующая полка.
    Функция возвращает номер полки.
    """
    shelf = ''
    while dict1.get(shelf) is None:
        shelf = input('\nВведите номер полки, на которую нужно поместить документ:').strip()
        if dict1.get(shelf) is None:
            print(f'Полки с номером "{shelf}" не существует! Укажите другую полку! ')
    return shelf


def add_new_document(new_list, list1, dict1):
    """
    Добавляет новый документ в каталог "list1" и перечень полок "dict1", используя элементы из "new_list".
    "new_list" - список из трех элементов. Добавление в словарь с использованием функции "shelf_check()".
    """
    shelf = shelf_check(dict1)
    (dict1[shelf]).append(new_list[1])
    title_list = ["type", "number", "name"]
    list1.append(dict(zip(title_list, new_list)))
    return shelf


def del_el_doc(number, list1):
    for document in list1:
        if document["number"] == number:
            list1.remove(document)
            return True
    else:
        print(f'Человек с номером документа "{number}" не найден')
        return f'Человек с номером документа "{number}" не найден!'


def del_el_shelf(number, dict1):
    for elements in dict1.values():
        if number in elements:
            elements.remove(number)
            return True
    else:
        print(f'Документа с номером "{number}" нет на полках!')
        return f'Документа с номером "{number}" нет на полках!'


def delete_doc(number, list1, dict1):
    """
    Удаление документа с номером "number" из каталога и из перечня полок.
    """
    del_el_doc(number, list1)
    del_el_shelf(number, dict1)


def move_doc(dict1):
    """
    Перемещение документа, указанного пользователем, на выбранную пользователем полку.
    """
    number = None
    while number is None:
        print(f'\nКакой документ хотите переместить? ', end='')
        number = entering_document_number()
        if "не найден!" in output_shelf_by_number(number, dict1):
            number = None
    del_el_shelf(number, dict1)
    shelf = shelf_check(dict1)
    (dict1[shelf]).append(number)


def add_shelf(dict1):
    """
    Создание новой полки и добавление её в перечень полок. Номер создаваемой полки указывает пользователь.
    """
    shelf = input('\nВведите номер полки, которую хотите создать: ').strip()
    if dict1.get(shelf) is None:
        dict1[shelf] = []
        return True
    else:
        print(f'Полка с номером {shelf} уже существует!')
        return f'Полка с номером {shelf} уже существует!'


def main(list1, dict1):
    """
    Пользовательское меню.
    p – people – команда, которая спросит номер документа и
                выведет имя человека и тип документа, которому он принадлежит;
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    a – add – команда, которая добавит новый документ в каталог и в перечень полок,
              спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
    """
    while True:
        user_input = (input('\nВведите команду! ').strip()).lower()
        if user_input == 'p':
            output_name_by_number(entering_document_number(), list1)
        elif user_input == 's':
            output_shelf_by_number(entering_document_number(), dict1)
        elif user_input == 'l':
            output_all_documents(list1)
        elif user_input == 'a':
            add_new_document(input_new_document(), list1, dict1)
        elif user_input == 'd':
            delete_doc(entering_document_number(), list1, dict1)
        elif user_input == 'm':
            move_doc(dict1)
        elif user_input == 'as':
            add_shelf(dict1)
        elif user_input == 'q':
            break


if __name__ == '__main__':

    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
    directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }

    main(documents, directories)
