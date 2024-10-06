
.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: env
env:
	pip3 install -r requirements.txt

.PHONY: demo
demo:
	python3 manage.py runserver 0.0.0.0:8080 --settings=makegoalsdaily.settings.test --insecure

.PHONY: env-info
env-info:
	uname -a
	pip list

.PHONY: initlogin
initlogin:
	python3 manage.py initlogin

.PHONY: lint
lint:
	flake8 --ignore=E501,F401,F403,F405,F999 makegoalsdaily logtoday

.PHONY: migrations
migrations:
	python3 manage.py makemigrations

.PHONY: migrate
migrate:
	python3 manage.py migrate --noinput

.PHONY: run
run:
	python3 manage.py runserver

.PHONY: test
test:
	python3 manage.py test tests.functional logtoday
