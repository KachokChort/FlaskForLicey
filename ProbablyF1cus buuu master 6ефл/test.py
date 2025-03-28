from requests import get, post

print(get('http://localhost:5000/api/v2/users').json())  # получение всех работ
print(get('http://localhost:5000/api/v2/users/2').json())  # получение одной существующей в бд работы
print(get('http://localhost:5000/api/v2/users/12').json())  # неверный id
print(get('http://localhost:5000/api/v2/users/stroka').json())  # id = строка

