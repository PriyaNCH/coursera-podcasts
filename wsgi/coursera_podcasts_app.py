from bottle import route, default_app, error, static_file, view

# @route('/name/<name>')
# def nameindex(name='Stranger'):
#     return '<strong>Hello, %s!</strong>' % name

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='/static')

@route('/')
@view('index')
def index():
	return dict

@error(404)
def error404(error):
	return 'Page Not found'

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()