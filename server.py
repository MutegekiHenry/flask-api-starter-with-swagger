import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS

from app.routes import api
from app.models import db


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, override="true")

def create_app(config_name):
    """ app factory """

    # import config options
    from config.config import app_config

    app = Flask(__name__)

    # allow cross-domain requests
    CORS(app)

    # use running config settings on app
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # register app with the db
    db.init_app(app)

    # initialize api resources
    api.init_app(app)

    # swagger
    app.config['SWAGGER'] = {
        'title': 'Backend API',
        'uiversion': 3
    }

    Swagger(app, template_file='api_docs.json')

    # handle default 404 exceptions with a custom response
    @app.errorhandler(404)
    def resource_not_found(exception):
        response = jsonify(dict(status='fail', data={
            'error': 'Not found', 'message': 'The requested URL was'
            ' not found on the server. If you entered the URL '
            'manually please check and try again'
        }))
        response.status_code = 404
        return response

    # both error handlers below handle default 500 exceptions with a custom
    # response
    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify(dict(status=error, error='Internal Server Error',
                                message='The server encountered an internal error and was'
                                ' unable to complete your request.  Either the server is'
                                ' overloaded or there is an error in the application'))
        response.status_code = 500
        return response

    return app


# create app instance using running config
app = create_app(os.getenv('FLASK_ENV'))

if __name__ == '__main__':
    app.run()
