from requests import get

print(get('http://localhost:5000/api/jobs').json()) # получение всех работ
print(get('http://localhost:5000/api/jobs/2').json()) # получение одной существующей в бд работы
print(get('http://localhost:5000/api/jobs/12').json()) # неверный id
print(get('http://localhost:5000/api/jobs/stroka').json()) # id = строка

print(post('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок',
                 'work_size': 5,
                 'team_leader': 1,
                 'collaborators': '5, 7',
                 'is_finished': False}).json())

print(get('http://localhost:5000/api/jobs').json())
