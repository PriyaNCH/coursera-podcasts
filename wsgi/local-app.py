import bottle
from bottle import run,TEMPLATE_PATH
from coursera_podcasts_app import application
import os 

bottle.debug(True)
run(application,host='localhost',port=9000,reloader=True)