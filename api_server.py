from wsgiref.simple_server import make_server

import json


def api(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'application/json; charset=utf-8'),
        ('Access-Control-Allow-Origin', '*'),
    ]
    start_response(status, headers)

    return [json.dumps({'message':'hoge'}).encode("utf-8")]

with make_server('', 8080, api) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()

