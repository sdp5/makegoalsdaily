#!/usr/bin/env bash

cd /workspace
export PYTHONPATH=/workspace;$PYTHONPATH

make migrate
make initlogin
make demo
