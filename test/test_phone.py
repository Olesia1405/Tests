import pytest
from hw_test.main import process_contacts, save_to_csv_stringio

@pytest.mark.parametrize("contacts_list, expected_result", [
    (
        [
            ["last_name", "first_name", "surname", "organization", "position", "phone", "email"],
            ["Иванов", "Иван", "Иванович", "ОАО Ромашка", "Инженер", "+7 999 123-45-67 доб. 891", "ivanov@example.com"],
            ["Петров", "Петр", "", "ЗАО Лотос", "Менеджер", "8(999)123-45-67", "petrov@example.com"],
            ["Иванов", "Иван", "", "ОАО Ромашка", "Инженер", "+7 999 123-45-67 доб. 892", "ivanov@example.com"],
        ],
        [
            ["last_name", "first_name", "surname", "organization", "position", "phone", "email"],
            ["Иванов", "Иван", "Иванович", "ОАО Ромашка", "Инженер", "+7(999)123-45-67  доб.891", "ivanov@example.com"],
            ["Петров", "Петр", "", "ЗАО Лотос", "Менеджер", "+7(999)123-45-67", "petrov@example.com"],
        ]
    ),
    (
        [
            ["last_name", "first_name", "surname", "organization", "position", "phone", "email"],
            ["Александров", "Александр", "Александрович", "ООО Плюс", "Директор", "", "alex@example.com"]
        ],
        [
            ["last_name", "first_name", "surname", "organization", "position", "phone", "email"],
            ["Александров", "Александр", "Александрович", "ООО Плюс", "Директор", "", "alex@example.com"]
        ]
    ),
])
def test_process_contacts(contacts_list, expected_result):
    result = process_contacts(contacts_list)
    assert result == expected_result


def test_save_to_csv_stringio():
    contacts = [
        ["last_name", "first_name", "surname", "organization", "position", "phone", "email"],
        ["Иванов", "Иван", "Иванович", "ОАО Ромашка", "Инженер", "+7(999)123-45-67  доб.891", "ivanov@example.com"],
        ["Петров", "Петр", "", "ЗАО Лотос", "Менеджер", "+7(999)123-45-67", "petrov@example.com"]
    ]
    expected_csv_content = (
        "last_name,first_name,surname,organization,position,phone,email\r\n"
        "Иванов,Иван,Иванович,ОАО Ромашка,Инженер,+7(999)123-45-67  доб.891,ivanov@example.com\r\n"
        "Петров,Петр,,ЗАО Лотос,Менеджер,+7(999)123-45-67,petrov@example.com\r\n"
    )
    csv_content = save_to_csv_stringio(contacts)
    assert csv_content == expected_csv_content
