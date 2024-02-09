# stock market django
 
py -m venv venv

pip install django
pip freeze

django-admin startproject stocks 

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py startapp quotes