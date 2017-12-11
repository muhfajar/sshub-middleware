# sshub-middleware
Middleware between RFID login device with SSHub API

---
Prerequisite:
1. Virtualenv `pip install virtualenv`
2. python-dev (recommended: use python version 3.x)

How-to:
1. Create virtualenv (optional, if you don't want your system messy with application dependencies) `virtualenv env -p python3`
2. Activate virtualenv `source env/bin/activate`
3. Install all dependencies `pip install -r requirements.txt`
4. Install [Gunicorn](http://gunicorn.org/) `pip install gunicorn`
5. Migrate database `python manage.py migrate`
6. Create superuser `python manage.py createsuperuser`
7. Collect all static file `python manage.py collectstatic`
8. Run Gunicorn as daemon `gunicorn sshub_middleware.wsgi -b :4000 --daemon --reload`
9. If you want stop Gunicorn daemon, you can use `pkill gunicorn`
10. Done
