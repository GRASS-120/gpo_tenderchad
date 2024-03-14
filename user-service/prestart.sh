#! /usr/bin/env bash

# Run migrations
alembic upgrade head

python3 app/initial_data.py