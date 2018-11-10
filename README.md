# seq-webapp
Web app for analyzing characters

For now the stack is following:
- Python3.6
- web server: Django
- database: Sqlite (comes with python)
- background tasks: Celery worker with Redis as message broker
- UI: django admin web interface

## How to run it locally

**Please Note:** All following commands are assumed to be run from `code/char_analyzer` directory.

1. Make sure that you install [redis](https://redis.io/) and run it at default port (`6379`, that is)
1. Install dependencies: `pip install -r ../../requirements.txt`
1. Create database schema: `python manage.py migrate`
1. Create django superuser (to access django admin): `python manage.py createsuperuser`
1. In terminal1 run development server: `cd code/char_analyzer; python manage.py runserver`
1. In terminal2 run celery worker (that will run calculations in background): `cd code/char_analyzer; celery -A char_analyzer worker --loglevel=info`
1. In browser go to http://127.0.0.1:8000/admin. There at http://127.0.0.1:8000/admin/core/job/ you can add new files and run calculations on them (from "Actions" dropdown menu in listing page)
