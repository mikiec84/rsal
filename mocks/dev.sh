#!/bin/sh

# flask dev server (and allowing external access by habit for vm/container dev)

export FLASK_APP=srv.py
p=8080

flask run --host=0.0.0.0 --port=$p

