def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('sem8\\book.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.rstrip())


def add_data() -> None:
    """Добавляет информацию в справочник"""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('sem8\\book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone_num}')


def search(contacts, info):
    """Находит в списке записи по определенному критерию поиска"""
    return [contact for contact in contacts if info in contact.lower()]


def find_data() -> None:
    """Печатает результат поиска по справочнику"""
    with open('sem8\\book.txt', 'r', encoding='utf-8') as file:
        contacts = [line.rstrip() for line in file]
    contact_to_find = input('Введите, что хотите найти: ').lower()
    current_results = search(contacts, contact_to_find)
    while len(current_results) > 1:
        print("Найдено несколько записей:")
        for i, contact in enumerate(current_results, 1):
            print(f"{i}. {contact}")
        print("Пожалуйста, уточните запрос.")
        contact_to_find = input('Введите уточненный запрос: ').lower()
        current_results = search(current_results, contact_to_find)
    if len(current_results) == 1:
        print("Найдена одна запись:")
        print(current_results[0])
        edit_or_delete(current_results[0])
    else:
        print("Запись не найдена.")


def edit_or_delete(contact) -> None:
    """Предлагает редактировать или удалить контакт"""
    choice = input("Введите 'e' для редактирования или 'd' для удаления: ")
    if choice == 'e':
        edit_contact(contact)
    elif choice == 'd':
        delete_contact(contact)
    else:
        print("Некорректный выбор.")
        return


def edit_contact(contact) -> None:
    """Редактирует выбранный контакт"""
    add_data()
    delete_contact(contact)
    print("Контакт успешно отредактирован.")


def delete_contact(contact) -> None:
    """Удаляет выбранный контакт"""
    with open('sem8\\book.txt', 'r', encoding='utf-8') as file:
        contacts = [line.rstrip() for line in file]
    updated_contacts = [c for c in contacts if c != contact]
    with open('sem8\\book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(updated_contacts))

