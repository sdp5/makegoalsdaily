#!/usr/bin/env bash

cd /workspace
export PYTHONPATH=/workspace;$PYTHONPATH

python3 manage.py initlogin
python3 manage.py runserver 0.0.0.0:8080
