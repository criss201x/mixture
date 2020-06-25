import falcon
from wsgiref import simple_server
import resources

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
cuadrangular = resources.CuadrangularResource()

app.add_route('/cuadrangular', cuadrangular)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()