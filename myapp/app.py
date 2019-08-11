import os
from flask import Flask, render_template

from . import public

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
    SECRET_KEY='dev',
    # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/ping/')
    def pingpong():
        return 'pong!'

    @app.route('/')
    def index():
        return render_template('index.html')


    # Blueprints
    app.register_blueprint(public.views.blueprint)

    return app
