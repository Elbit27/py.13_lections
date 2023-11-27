# Базы данных(БД) - набор взаимосвязанных данных
# Атребуты - столбики
# Записи, кортежи - строчки



# Типы СУБД:

#     Файл серверные: Microsoft Access
#     Клиент серверные: MySQL, PostgreSQL...
#     Встраиваемые: SQLite

# PostgreSQL - Система управления базами данных(СУБД/DBMS)
# Это ряд программ и инструментов позволяющих создовать БД, управлять ею и манипулировать данными внутри(CRUD)

# Postgres - сама база данных, она объектно реляционная, то есть данные хранятся в виде таблиц, и таблицы имеют связи между собой

# SQL (Structured Query language) - декларативный язык структурированных завпросов, он применяется для создания и получения данных при помощи запросов в БД

# --------------------------------
# Типы полей в Postgres

# Numeric Types(числовые типы)
    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2.147... to 2.147...
    # с. bigint(8 bytes) -> ...
    # d. real (4 bytes) -> число с плавающей точкой, вещественное 
    # e. serial (4 bytes) -> integer, auto-increment

# Character types(Символьные типы(строковые)):
    # a. varchar(кол-во символов) -> если мы укажеи 50 символов, а заполним только 10, то остальные будут свободны. Макс 255
    # b. char(кол-во символов) -> если мы укажеи 50 символов, а заполним только 10, то остальные будут заполнены пробелом. Макс 255
    # с. text() -> неогр кол-во символов

# Boolen Type
    # a. boolean(1 bytes) -> True/False

# date -> календарная дата (год.месяц.день)

# location -> координатная точка (x, y) - (245, -12)

# enumerate types:
    # ('a', 'b', 'c')   
    # CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad');

# ----------------------------------------------

# команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# команда для входа
# exit
# \q

# команда для входа в своего юзера 
# psql

# создание суперюзера
# CREATE ROLE username SUPERUSER LOGIN PASSWORD '1';

# изменение пароля
# ALTER USER username WITH PASSWORD '1';

# создание бд
# CREATE DATABASE 'name';

# \du - все юзеры
# \l - список всех бд
# \dt - все таблицы (нужно подлючиться к бд заранее)
# \d 'name' - подробная информация про таблицу (нужно подлючиться к бд заранее)
# \c 'name' - команда для подколючения к бд

# -------------------------------------


# Команда для получения данных
# SELECT (columns)* FROM <table>;

# ORDER BY: Позволяет нам сортировать выодящие данные по убыванию или возрастанию.  ASC(по возрастанию) и DESC(по убыванию)
# Cинтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# LIMIT: ставит ограничение в кол-во получаемых данных

# WHERE: используется для фильтрации по полям. будут выводится только те данные которые соответсвуют условию оператора WHERE
# Cинтаксис: SELECT <row> FROM <tablename> WHERE  <row> = 'чему либо';

# LIKE: Выводит результат который соответсвует введенному шаблону для строк. Чувствителен к регистру
# ILIKE: тоже самое только не зависит от регистра
# Cинтаксис: SELECT <row> FROM <tablename> WHERE  <row> LIKE/ILIKE 'чему либо';

# AND оператор и, для множетсвенных условий 
# IN: WHERE <row> in (1,2,3,4);

# SELECT product_name, unit_price, units_in_stock, (unit_price * units_in_stock) as sum  FROM products ORDER BY sum DESC LIMIT 10;






# --------------------------------------------------------------------------------------------


# Экспорт БД(дамп):
# pg_damp -U <user name>  -d 'dname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dname> -f <filename>


# -------------------------------------------------------

# Команда для создания таблиц
# CREATE TABLE <tableName> (
#     <column> <type>,
# )


# CREATE TABLE films (
#     code char(5),
#     title varchar(100),
#     date date,
#     genre varchar(50),
#     budget integer,
#     country varchar(50),
#     id setial
#     ); 


# Команда для удаления данных 
# DELETE FROM <table> 




# DROP TABLE <name>; - Удаление таблицы

# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# INSERT INTO films (code, title, budget, date, genre, country) VALUES
# ('AU56', 'Lord of the rings', 100000000, '2001-06-12', 'fantasy', 'USA'),
# ('KRIE', 'Hangout', 10000000, '20010-06-12', 'comedy', 'USA'),
# ('QWER', 'Zita and Gita', 1000000, '1999-06-12', 'drama', 'India'),
# ('GRM2', 'Green Mile', 100000, '1997-06-12', 'drama', 'USA'),
# ('qwe1', 'House of Dragon', 10000000, '2022-01-01', 'fantasy', 'USA');




# -------------------------------------------------------------------
#  Ограничения:
#     1. NOT NULL - обязательно к заполнению
#     2. UNIQUE - то что будет хранитьмя только уникальные данные 
#     3. CHECK -> CHECK  age > -1 - ограничение проверуи на условие
#     4 - для установки идентификатора данных в таблице
#     5 для установки связей между таблицами



# CREATE TABLE weather (
# elburs27(# id serial PRIMATY KEY,
# elburs27(# city varchar(100) NOT NULL,
# elburs27(# temp_lo int NOT NULL temp_lo > -150,
# elburs27(# temp_hi int NOT NULL temp_hi < 100,
# elburs27(# prcp real, 
# elburs27(# data data NOT NULL );



# ----------------------------------------------------------------------------

# Виды связей между таблицами(relations):
#     1. Один к одному (One to One)- человек и паспорт
#        в одну из таблиц добавляется поле fk и дается ограничение  unique
#     2. Один ко многим (One to Many) - человек и баковские карты
#        в таблицу много (банковские карты) доб. после fk  
#     3. Много ко многим (Many to Many) -  Студенты и преподы 
#        создается вспомогательная 3ья таблица со связями











