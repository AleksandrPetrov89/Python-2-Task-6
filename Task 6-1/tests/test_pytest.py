import pytest

import main

list_1 = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

dict_1 = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

fixture = ["123", "346747", "arfaeg"]


@pytest.mark.parametrize("input_text", fixture)
def test_entering_document_number(monkeypatch, input_text):
    monkeypatch.setattr('builtins.input', lambda x: input_text)
    assert main.entering_document_number() == input_text


fixture = [
    ("2207 876234", list_1, '"Василий Гупкин" имеет "passport" с номером "2207 876234"'),
    ("3446567", list_1, 'Человек с номером документа "3446567" не найден!')
]


@pytest.mark.parametrize("number, list1, result", fixture)
def test_output_name_by_number(number, list1, result):
    assert main.output_name_by_number(number, list1) == result


fixture = [
    ("2207 876234", dict_1, 'Документ с номером "2207 876234" находится на "1" полке!'),
    ("10006", dict_1, 'Документ с номером "10006" находится на "2" полке!'),
    ("3446567", dict_1, 'Документ с номером "3446567" не найден!')
]


@pytest.mark.parametrize("number, dict1, result", fixture)
def test_output_shelf_by_number(number, dict1, result):
    assert main.output_shelf_by_number(number, dict1) == result


fixture = [
    ("1", dict_1),
    ("2", dict_1),
    ("3", dict_1)
]


@pytest.mark.parametrize("input_text, dict1", fixture)
def test_shelf_check(monkeypatch, input_text, dict1):
    monkeypatch.setattr('builtins.input', lambda x: input_text)
    assert main.shelf_check(dict1) == input_text


fixture = [
    ("1", ["passport", "8007 457812", "Иван Иванов"], list_1, dict_1),
    ("2", ["invoice", "45345 785847", "Петр Петров"], list_1, dict_1),
    ("3", ["insurance", "12 354", "Сидр Сидоров"], list_1, dict_1),
]


@pytest.mark.parametrize("input_text, new_list, list1, dict1", fixture)
def test_add_new_document(monkeypatch, input_text, new_list, list1, dict1):
    number_documents = len(list1)
    num_doc_on_shelf = len(dict1[input_text])
    assert new_list[1] not in dict1[input_text]
    monkeypatch.setattr("main.shelf_check", lambda x: input_text)
    assert main.add_new_document(new_list, list1, dict1) == input_text
    assert len(list1) == number_documents + 1
    assert list1[number_documents] == {"type": new_list[0], "number": new_list[1], "name": new_list[2]}
    assert new_list[1] in dict1[input_text]
    assert len(dict1[input_text]) == num_doc_on_shelf + 1


fixture = [
    ("2207 876234", list_1, True),
    ("3446567", list_1, 'Человек с номером документа "3446567" не найден!'),
    ("12 354", list_1, True)
]


@pytest.mark.parametrize("number, list1, result", fixture)
def test_del_el_doc(number, list1, result):
    number_documents = len(list1)
    assert main.del_el_doc(number, list1) == result
    if result is True:
        assert len(list1) == number_documents - 1


fixture = [
    ("2207 876234", dict_1, True, "1"),
    ("3446567", dict_1, 'Документа с номером "3446567" нет на полках!', "1"),
    ("12 354", dict_1, True, "3")
]


@pytest.mark.parametrize("number, dict1, result, shelf", fixture)
def test_del_el_shelf(number, dict1, result, shelf):
    num_doc_on_shelf = len(dict1[shelf])
    if result is True:
        assert number in dict1[shelf]
    assert main.del_el_shelf(number, dict1) == result
    if result is True:
        assert number not in dict1[shelf]
        assert len(dict1[shelf]) == num_doc_on_shelf - 1


fixture = [
    ("4", dict_1, True),
    ("2", dict_1, 'Полка с номером 2 уже существует!'),
    ("7", dict_1, True)
]


@pytest.mark.parametrize("shelf, dict1, result", fixture)
def test_add_shelf(monkeypatch, shelf, dict1, result):
    if result is True:
        assert shelf not in dict1.keys()
    monkeypatch.setattr('builtins.input', lambda x: shelf)
    assert main.add_shelf(dict1) == result
    assert shelf in dict1.keys()
