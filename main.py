import re
import csv
from io import StringIO


def process_contacts(contacts_list):
    phone_pattern = re.compile(
        r'(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})')
    extension_pattern = re.compile(r'\s*\(*(доб.)\s*(\d+)\)*\s*')

    contacts_dict = {}
    for contact in contacts_list[1:]:
        full_name = ' '.join(contact[:3]).split()
        last_name, first_name, *surname = (full_name + [""])[:3]
        key = (last_name, first_name)

        phone = contact[5]
        if phone:
            phone = phone_pattern.sub(r'+7(\2)\3-\4-\5', phone)
            phone = extension_pattern.sub(r' \1\2', phone)

        if key not in contacts_dict:
            contacts_dict[key] = [last_name, first_name, surname[0], contact[3], contact[4], phone, contact[6]]
        else:
            for i in range(3, 7):
                if not contacts_dict[key][i]:
                    contacts_dict[key][i] = contact[i]

    return [contacts_list[0]] + list(contacts_dict.values())


def save_to_csv(file_name, contacts):
    with open(file_name, "w", newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(contacts)


def save_to_csv_stringio(contacts):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(contacts)
    output.seek(0)
    return output.getvalue()
