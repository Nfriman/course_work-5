import requests
import psycopg2


class Parsing_hh:
    """ Класс для парсинга вакансий на сайте hh.ru """

    def __init__(self, employer_id):
        self.employer_id = employer_id  # id компаний для получения вакансийв

        parms = {'employer_id': self.employer_id,
                 "per_page": 100}
        self.hh = requests.get('https://api.hh.ru/vacancies?only_with_salary=true', parms).json()

    def get_data(self):
        """метод для полученния данных о вакансиях и компанниях"""
        with psycopg2.connect(host="localhost", database="course_work_5", user="admi", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute('TRUNCATE TABLE vacancies RESTART IDENTITY')
                for index in self.hh['items']:
                    if index['salary'] is None:
                        salary = 0  # если не указана ЗП
                    else:
                        salary = index['salary']['from']  # ЗП

                    cur.execute(
                        'INSERT INTO vacancies(vacancies_name, salary, vacancies_url, employers_name) VALUES (%s, %s, '
                        '%s, %s)',
                        (index['name'], salary, index['alternate_url'], index['employer']['name']))
                    cur.execute('SELECT * FROM vacancies')
        conn.close()


def open_data_base(comand: 'str'):
    """Функция для получения дфнных из postegresql"""
    with psycopg2.connect(host="localhost", database="course_work_5", user="admi", password="1234") as conn:
        with conn.cursor() as cur:
            cur.execute(comand)
            read = cur.fetchall()
            return read
