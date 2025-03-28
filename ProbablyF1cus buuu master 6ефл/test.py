from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())  # получение всех работ
print(get('http://localhost:5000/api/v2/users/2').json())  # получение одной существующей в бд работы
print(get('http://localhost:5000/api/v2/users/12').json())  # неверный id
print(get('http://localhost:5000/api/v2/users/stroka').json())  # id = строка

print(post('http://localhost:5000/api/v2/users',
           json={
               'job': 'Заголовок',
               'work_size': 5,
               'team_leader': 1,
               'collaborators': '5, 7',
               'is_finished': False
           }).json())

print(delete('http://localhost:5000/api/v2/users/5'))