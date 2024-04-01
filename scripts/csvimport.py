from csv import reader
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2SHA1PasswordHasher as hasher
# from app.models import


def user_import():
    with open("./app/static/csv/user.csv", mode='r', encoding='utf-8') as file:
        for row in reader(file):
            _, created = User.objects.get_or_create(
                username=row[0],
                first_name=row[1],
                last_name=row[2],
                email=row[3],
                password=hasher.encode(hasher(), row[4], hasher.salt(hasher())),
                is_staff=row[5],
            )
            print(created)


def run():
    user_import()
    print('Done')
