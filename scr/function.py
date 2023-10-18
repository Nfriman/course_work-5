import requests
import psycopg2
from scr.config import config


class Parsing_hh:
    """ Класс для парсинга вакансий на сайте hh.ru """
    def __init__(self, employer_id):
        self.employer_id = employer_id  # id компаний для получения вакансий

        parms = {'employer_id': self.employer_id,
                 "per_page": 100}
        self.hh = requests.get('https://api.hh.ru/vacancies?only_with_salary=true', parms).json()

    def get_data(self):
        """метод для полученния данных о вакансиях и компанниях"""
        for index in self.hh['items']:
            if index['salary'] is None:
                salary = 0  # если не указана ЗП
            else:
                salary = index['salary']['from']  # ЗП

            data_recording(index['name'], salary, index['alternate_url'], index['employer']['name'])



def open_data_base(comand: 'str'):
    """Функция для получения дфнных из postegresql"""
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(comand)
            read = cur.fetchall()
            return read


def get_user():
    """Функция для взаимодействия с пользователем"""
    print("Для получения нужных вам данных выберите соотвествующую цифру\n"
          "1 - получает список всех компаний и количество вакансий у каждой компании\n"
          "2 - получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на "
          "вакансию\n"
          "3 - получает среднюю зарплату по вакансиям\n"
          "4 - получает список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
          "5 - получает список всех вакансий, в названии которых содержатся переданные в метод слова, "
          "например “python”\n")

    user_ansver = int(input('№: '))
    from scr.class_db import DBManager
    get_data = DBManager()
    if user_ansver == 1:
        return get_data.get_companies_and_vacancies_count()
    elif user_ansver == 2:
        return get_data.get_all_vacancies()
    elif user_ansver == 3:
        return get_data.get_avg_salary()
    elif user_ansver == 4:
        return get_data.get_vacancies_with_higher_salary()
    elif user_ansver == 5:
        return get_data.get_vacancies_keyword()
    else:
        return f'Нет такого ответа'


def create_table():
    """Функция для создания таблицы и его очистки таблицы"""
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS vacancies (vacancies_id serial,vacancies_name text,salary int,vacancies_url text, employers_name varchar(100), CONSTRAINT pk_vacancies1_vacancies1_id PRIMARY KEY (vacancies_id));")
            cur.execute('TRUNCATE TABLE vacancies RESTART IDENTITY')

    conn.close()

def data_recording(name, salary, url, em_name):
    """Функция для ввода данных в таблицы"""
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO vacancies (vacancies_name, salary, vacancies_url, employers_name) VALUES (%s, %s, '
                       '%s, %s)', (name, salary, url, em_name))
    conn.close()

