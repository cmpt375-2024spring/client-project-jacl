from csv import reader
from django.contrib.auth.models import User
# from app.models import


def user_import():
    with open("./app/static/csv/user.csv", mode='r', encoding='utf-8') as file:
        for row in reader(file):
            _, created = User.objects.get_or_create(
                username=row[0],
                email=row[1],
                password=row[2],
            )
            print(created)


def run():
    user_import()
    print('Done')
