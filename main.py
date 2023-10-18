from scr.function import Parsing_hh, get_user , create_table


id_company = (205152, 4290639, 3754394, 3584763, 873860, 21388, 3272475, 561525, 717220, 908642)  # id компаний для
# получения вакансий


if __name__ == '__main__':
    create_table()
    Parsing_hh(id_company).get_data()  # Получения вакансий и данных о компаниях
    print(get_user())   # функция для взаимодействия с пользователем