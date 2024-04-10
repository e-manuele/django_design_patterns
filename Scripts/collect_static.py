import os


def init():
    os.system('python manage.py collectstatic')


if __name__ == '__main__':
    init()
