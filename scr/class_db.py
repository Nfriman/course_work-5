from scr.function import open_data_base


class DBManager:
    """Класс для подключения к БД postgres и имеет методы для получения разных данных о вакансиях"""

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        employer_data = open_data_base(
            'SELECT employers_name, COUNT(*) FROM vacancies GROUP BY employers_name ORDER BY COUNT(*) DESC')
        return employer_data

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию"""
        vacancies_data = open_data_base('select employers_name, vacancies_name, salary, vacancies_url from vacancies')
        return vacancies_data

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        salary_avg = open_data_base('SELECT AVG(salary) FROM vacancies')
        return int(salary_avg[0][0])

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        vacancies_avg_salary = open_data_base(
            'SELECT employers_name, vacancies_name, salary, vacancies_url FROM vacancies WHERE salary > (select AVG('
            'salary) from vacancies)')
        return vacancies_avg_salary

    def get_vacancies_keyword(self):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        vacancies_key = open_data_base(
            "select employers_name, vacancies_name, salary, vacancies_url from vacancies where vacancies_name LIKE "
            "'Python%'")
        return vacancies_key
