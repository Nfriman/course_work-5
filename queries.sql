-- SQL-команды для создания таблиц
CREATE TABLE vacancies2
(
    vacancies_id serial,
    vacancies_name text,
    salary int,
    vacancies_url text,
    employers_name varchar(30),

    CONSTRAINT pk_vacancies2_vacancies_id PRIMARY KEY (vacancies_id)
);

-- Получает список всех компаний и количество вакансий у каждой компании
SELECT employers_name, COUNT(*) FROM vacancies GROUP BY employers_name ORDER BY COUNT(*) DESC;

-- Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
select employers_name, vacancies_name, salary, vacancies_url from vacancies;

-- Получает среднюю зарплату по вакансиям
SELECT AVG(salary) FROM vacancies;

-- Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
SELECT employers_name, vacancies_name, salary, vacancies_url FROM vacancies
WHERE salary > (select AVG(salary) from vacancies;

-- Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
select employers_name, vacancies_name, salary, vacancies_url from vacancies where vacancies_name LIKE 'Python%'

 -- Добавления данных в таблицу
INSERT INTO vacancies(vacancies_name, salary, vacancies_url, employers_name) VALUES (%s, %s, %s, %s),
(index['name'], salary, index['alternate_url'], index['employer']['name']))



