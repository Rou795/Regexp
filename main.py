import csv
from contact import Contact

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)
contacts = []

if __name__ == '__main__':
    for idx, line in enumerate(contact_list):
        if idx != 0:
            contacts.append(Contact())
            row = ' '.join(line)
            contacts[idx - 1].set_from_line(line)

# поиск контактов одних и тех же людей

    for idx_1 in range(len(contacts)):
        for idx_2 in range(len(contacts)):
            if idx_1 != idx_2:
                if contacts[idx_1] == contacts[idx_2]:
                    contacts[idx_1].merge(contacts[idx_2])
    contacts.sort(key=lambda x: x.get_lastname())
    new_contacts = []
    for idx in range(1, len(contacts)):
        if contacts[idx - 1] != contacts[idx]:
            new_contacts.append(contacts[idx - 1])

    with open("phonebook.csv", "w", encoding='cp1251') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows([contact.contact_in_list() for contact in new_contacts])
