<!-- python -m autopep8 --max-line-length 60 --in-place --aggressive --aggressive ./**.py -->

# Dajngo Rest Framework JWT Auth and CRUD
Project made with the intention of showing how to make a simples API for user authentication and manipulation (CRUD).

## Install and run the project
```sh
# install
virtualenv --python=python3 .virenv
source ./virenv/bin/activate
pip install -r requirements.txt

# craete 1º super user
python manage.py createsuperuser

# run
cd djangoUserAuth
python manage.py runserver
```
