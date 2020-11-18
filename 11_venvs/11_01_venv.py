'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.

'''
#Lab done in terminal. Bellow is a copy of the terminal.


  Using cached click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Django==3.1.3
  Using cached Django-3.1.3-py3-none-any.whl (7.8 MB)
Collecting Flask==1.1.2
  Using cached Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting itsdangerous==1.1.0
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2==2.11.2
  Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe==1.1.1
  Using cached MarkupSafe-1.1.1.tar.gz (19 kB)
Collecting pytz==2020.4
  Using cached pytz-2020.4-py2.py3-none-any.whl (509 kB)
Collecting sqlparse==0.4.1
  Using cached sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting Werkzeug==1.0.1
  Using cached Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Using legacy 'setup.py install' for MarkupSafe, since package 'wheel' is not installed.
Installing collected packages: asgiref, click, pytz, sqlparse, Django, MarkupSafe, Jinja2, itsdangerous, Werkzeug, Flask
ls
    Running setup.py install for MarkupSafe ... done
Successfully installed Django-3.1.3 Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 asgiref-3.3.1 click-7.1.2 itsdangerous-1.1.0 pytz-2020.4 sqlparse-0.4.1
WARNING: You are using pip version 20.2.3; however, version 20.2.4 is available.
You should consider upgrading via the '/Users/Igor/Documents/CodingNomads/virtual_test/virtual_test/my_second_env/bin/python3 -m pip install --upgrade pip' command.
(my_second_env) Edna-Longorias-iMac:virtual_test Igor$ ls
requirements.txt	virtual_test
(my_second_env) Edna-Longorias-iMac:virtual_test Igor$ cd virtual_test/
(my_second_env) Edna-Longorias-iMac:virtual_test Igor$ cd my_second_env/
(my_second_env) Edna-Longorias-iMac:my_second_env Igor$ ls
bin		include		lib		pyvenv.cfg
(my_second_env) Edna-Longorias-iMac:my_second_env Igor$ pip freeze
asgiref==3.3.1
click==7.1.2
Django==3.1.3
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
pytz==2020.4
sqlparse==0.4.1
Werkzeug==1.0.1
(my_second_env) Edna-Longorias-iMac:my_second_env Igor$ ls
bin		include		lib		pyvenv.cfg
(my_second_env) Edna-Longorias-iMac:my_second_env Igor$ cd lib
(my_second_env) Edna-Longorias-iMac:lib Igor$ ls
python3.9
(my_second_env) Edna-Longorias-iMac:lib Igor$ cd ..
(my_second_env) Edna-Longorias-iMac:my_second_env Igor$ python3
Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> quit()
(my_second_env) Edna-Longorias-iMac:my_second_env Igor$ ls
bin		include		lib		pyvenv.cfg
(my_second_env) Edna-Longorias-iMac:my_second_env Igor$ deactivate
Edna-Longorias-iMac:my_second_env Igor$
