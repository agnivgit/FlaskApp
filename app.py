from flask import Flask, request
import logging
import os

logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)

# Enabling DEBUG mode based on flask app env
if os.environ.get('FLASK_ENV') == 'dev':
    app.logger.info("Environment is development, setting DEBUG On")
    os.environ['FLASK_DEBUG'] = '1'

elif os.environ.get('FLASK_ENV') != 'dev':
    app.logger.info("Environment is not development")
    os.environ['FLASK_DEBUG'] = '0'

# Api function
@app.route('/', methods = ['GET', 'POST']) 

def index():
    if request.method == 'GET':
        app.logger.info('Processing get request')
        if request.content_type == 'application/json':
            return '{"message": "Hello, World"}\n'
        else:
            return '<p>Hello, World</p>\n' 
            
    elif request.method == 'POST':
        app.logger.info('Processing post request')
        return ""         

if __name__ == "__main__":
    app.run()  