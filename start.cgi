#!/usr/bin/python3
try:
    from wsgiref.handlers import CGIHandler
    from __init__ import app

    CGIHandler().run(app)
except Exception as err:
    print("Content-Type: text/html\n\n")
    print(err)
