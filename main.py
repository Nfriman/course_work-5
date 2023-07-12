from scr.function import Parsing_hh, get_user, create_table


id_company = (205152, 4290639, 3754394, 3584763, 873860, 21388, 3272475, 561525, 717220, 908642)  # id компаний для
# получения вакансий
a = 2
if __name__ == '__main__':
    print("Для создания таблицы в postgresql необходимо указать следующее:")
    user_database = input('Укажите название базы данных: ')
    user_admi = input('Имя пользователя в postgresql: ')
    user_password = input('Пароль пользователя: ')
    create_table(user_database, user_admi, user_password)  # вызов функции для создания таблицы
    Parsing_hh(id_company, user_database, user_admi, user_password)  # Получения вакансий и данных о компаниях
    print(get_user())   # функция для взаимодействия с пользователем