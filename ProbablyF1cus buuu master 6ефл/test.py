from requests import get, post

# print(get('http://localhost:5000/api/jobs').json())  # получение всех работ
print(get('http://localhost:5000/api/jobs/2').json())  # получение одной существующей в бд работы
# print(get('http://localhost:5000/api/jobs/12').json())  # неверный id
# print(get('http://localhost:5000/api/jobs/stroka').json())  # id = строка
