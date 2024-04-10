import os
import webbrowser


def init():
    path = os.getcwd()
    # C:\Users\Emanuele\PycharmProjects\portale

    os.chdir(path)
    # print(path)
    # print("makemigrations")

    # make_migrations =
    os.system('python manage.py makemigrations')
    # print("migrate")
    # migrate =
    os.system('python manage.py   migrate')

    # run_server =
    #os.system(' python manage.py runserver')


# if make_migrations:
#    if migrate:
#       if run_server:
#          webbrowser.open_new_tab("http://127.0.0.1:8000/index")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
