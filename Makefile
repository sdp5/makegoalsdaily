
.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: env
env:
	pip install -r requirements.txt

.PHONY: demo
demo:
	python manage.py runserver --settings=makedaily.settings.test --insecure

.PHONY: env-info
env-info:
	uname -a
	pip list

.PHONY: lint
lint:
	flake8 --ignore=E501,F401,F403,F405,F999 makedaily logtoday

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: run
run:
	python manage.py runserver
